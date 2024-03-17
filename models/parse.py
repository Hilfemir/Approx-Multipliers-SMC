from importlib.metadata import distribution
from math import dist
from os import replace
import re
import argparse

log_ops = {
	"|" : 4,
	"&" : 2,
	"^" : 6,
	"NAND" : 3,
	"NOR" : 5,
	"XNOR" : 7,
	"NOT" : 0,
	"SET" : 8
	}

class SignalAssign(object):
	def __init__(self, params):
		self.params = params
		
		self.id = ""
		
		self.in1 = ""
		self.in2 = ""

		self.out = ""

		self.change_in1 = ""
		self.change_in2 = ""
		self.change_out = ""

		self.op = ""

	####################################################################

	def __repr__(self):
		ret = f"id: {self.id}\n"
		ret += f"input: {self.in1}, {self.in2}\n"
		ret += f"output: {self.out}\n"
		ret += f"change channels: {self.change_in1}, {self.change_in2}, {self.change_out}\n"

		return ret

	####################################################################

	@staticmethod
	def parse_input_sig(sig: str, PIxy_mapping: dict, POy_mapping: dict) -> tuple:
		"""Determines whether the input signal is an output of a different gate or if it's one
		of the original input bits and returns the correct presentations.
		"""
		pattern1 = r'^sig_([0-9]+)$' #eg. sig_221
		pattern2 = r'^[A-Z]\[[0-9]+\]$' #eg. A[1]
		ret_id = ""
		ret_channel = ""

		#signal is an output of a different gate
		if match := re.match(pattern1, sig):
			ret_id = match.group(1)
			ret_channel = f"change[{ret_id}]"

		elif match := re.match(pattern2, sig):
			if sig.startswith("O"):
				ret_id = POy_mapping[sig]
			else:
				ret_id = PIxy_mapping[sig]

			if num_match := re.search(r"[0-9]+", ret_id):
				ret_channel = f"change[{num_match[0]}]"
		
		return ret_id, ret_channel

	####################################################################

	def parse_params(self, PIxy_mapping: dict, POy_mapping: dict, output_signals: dict, latest_id: str, chan_size=1000):
		#determine whether id is signal id or output bit index
		if self.params[0].startswith("O"):
			self.id = str(int(latest_id) + 1)
		else:
			self.id = self.params[0].split('_')[-1]

		#output signal id
		if self.id in output_signals:
			self.out = f"POy[{output_signals[self.id]}]"
		elif self.params[0].startswith("O"):
			if match := re.match(r'O\[([0-9]+)\]', self.params[0]):
				self.out = f'POy[{match.group(1)}]'
		else:
			self.out = self.id

		#output broadcast channel
		self.change_out = f"change[{self.id}]"

		#input signal ids and broadcast channels
		if self.params[1] == self.params[3]:
			self.in1, self.change_in1 = self.parse_input_sig(self.params[1], PIxy_mapping, POy_mapping)
			self.in2, _ = self.parse_input_sig(self.params[3], PIxy_mapping, POy_mapping)
			self.change_in2 = f"change[{chan_size-1}]"
		else:
			self.in1, self.change_in1 = self.parse_input_sig(self.params[1], PIxy_mapping, POy_mapping)
			self.in2, self.change_in2 = self.parse_input_sig(self.params[3], PIxy_mapping, POy_mapping)

		#log. operation
		self.op = self.params[2]

	####################################################################

	def generate_gate(self, id: int) -> str:
		return f"g{self.id} = gate2({id}, {self.in1}, {self.in2}, {self.out}, {self.change_in1}, {self.change_in2}, {self.change_out});\n"

#################################################################################
#################################################################################
#################################################################################

class Parser(object):
	def __init__(self):
		self.input_bits = 0 #number of input bits
		self.input_names = [] #names of the 2 input variables in the verilog file

		self.output_bits = 0 #number of output bits
		self.output_name = "O" #name of the output variable in the verilog file

		self.channel_count = 1000 #number of broadcast channels

		self.latest_id = '0' #id of the last added signal assignment (gate)

		self.op_sequence = [] #sequence of operations used in logic gates
		self.signals = [] #list of signal assignments

		self.output_signals = {} #dict of the signals that represent the output bits
		self.output_zeros = [] #list of output bits that are always 0 (not computed by the mult.)

		self.max_int = 32768 #upper bound of some int values in the UPPAAL file

		#mappings of bit indexes in verilog files to bit indexes in UPPAAL files
		self.PIxy = {}
		self.POy = {}

		#parts of the final UPPAAL/xml file
		self.out_files = []

	####################################################################

	def io_decs(self, line: str):
		"""Checks for input/output declarations in the verilog file and
		parses them accordingly.
		"""
		line = line.strip()
		
		re_pat_in1 = r'input\s\[([0-9]+)\:0\]\s([a-zA-Z]+);'
		re_pat_in2 = r'input\s\[([0-9]+)\:0\]\s([a-zA-Z]+),\s*([a-zA-Z]+);'
		re_pat_out = r'output\s\[([0-9]+)\:0\]\s([a-zA-Z]+);'

		if match := re.match(re_pat_in1, line):
			self.input_bits = int(match.group(1)) + 1
			self.input_names.append(match.group(2))

		elif match := re.match(re_pat_in2, line):
			self.input_bits = int(match.group(1)) + 1
			self.input_names.extend([match.group(2), match.group(3)])

		elif match := re.match(re_pat_out, line):
			self.output_bits = int(match.group(1)) + 1
			self.output_name = match.group(2)

			self.max_int = pow(2, self.output_bits)

	####################################################################
			
	def prev_signal_in_params(self, prev_signal: SignalAssign) -> tuple[str, str, str]:
		in1 = prev_signal.in1
		in2 = prev_signal.in2

		reversed_PIxy = {value : key for key, value in self.PIxy.items()}
		reversed_POy = {value : key for key, value in self.POy.items()}

		if in1 in reversed_PIxy:
			in1 = reversed_PIxy[in1]
		elif in1 in reversed_POy:
			in1 = reversed_POy[in1]
		else:
			in1 = f"sig_{in1}"

		if in2 in reversed_PIxy:
			in2 = reversed_PIxy[in2]
		elif in2 in reversed_POy:
			in2 = reversed_POy[in2]
		else:
			in2 = f"sig_{in2}"

		op = prev_signal.op

		return in1, in2, op

	####################################################################

	def signal_assignments(self, line: str):
		"""Checks for signal assignments in the verilog file and
		parses them accordingly.
		"""
		line = line.strip()

		#eg. assign sig_118 = !(sig_115 & B[3]);
		negated_gate_pat = r'assign\s+(sig_[0-9]+)\s*=\s*!\((.*?)\s(.*?)\s(.*?)\);'

		#eg. assign sig_118 = sig_115 & B[3];
		gate_pat = r'assign\s+(sig_[0-9]+)\s*=\s*(.*?)\s(.*?)\s(.*?);'

		#eg. assign O[7] = sig_203 ^ sig_199;
		out_pat = r'assign\s+(O\[[0-9]+\])\s*=\s*(.*?)\s(.*?)\s(.*?);'

		#eg. assign O[5] = A[0] & B[0];
		out_pat2 = r'assign\s+(O\[[0-9]+\])\s*=\s*([A-Z]+\[[0-9]+\])\s+([&^|])\s+([A-Z]+\[[0-9]+\])\s*;'

		#eg. assign O[8] = O[0];
		out_pat3 = r'assign\s+(O\[[0-9]+\])\s*=\s*O\[([0-9]+)\]\s*;'

		#eg. assign O[2] = B[0];
		out_pat4 = r'assign\s+(O\[[0-9]+\])\s+=\s*([A-Z]+\[[0-9]+\])\s*;'

		#eg. assign O[15] = sig_335;
		out_pat5 = r'assign\s+(O\[[0-9]+\])\s*=\s*sig_([0-9]+)\s*;'

		#eg. assign sig_182 = ~sig_203;
		neg_pat = r'assign\s+(sig_[0-9]+)\s*=\s*~\s*(.*?)\s*;'

		#eg. assign sig_182 = sig_179;
		same_sig_pat = r'assign\s+(sig_[0-9]+)\s*=\s*(sig_[0-9]+)\s*;'

		if match := re.match(negated_gate_pat, line):
			op = match.group(3)

			neg_ops = {
				"&" : "NAND",
				"|" : "NOR",
				"^" : "XNOR"
				}
			
			op = neg_ops[op]
			groups = list(match.groups())

		elif match := re.match(gate_pat, line):
			op = match.group(3)
			groups = list(match.groups())

		elif match := re.match(out_pat, line):
			op = match.group(3)
			groups = list(match.groups())

		elif match := re.match(out_pat2, line):
			op = match.group(3)
			groups = list(match.groups())

		elif match := re.match(out_pat3, line):
			prev_out = f'POy[{match.group(2)}]'
			prev_signal = next(x for x in self.signals if x.out == prev_out)
			
			in1, in2, op = self.prev_signal_in_params(prev_signal)

			groups = [match.group(1), in1, op, in2]

		elif match := re.match(out_pat4, line):
			groups = [match.group(1), match.group(2), "SET", match.group(2)]
			op = "SET"

		elif match := re.match(out_pat5, line):
			id = match.group(2)
			prev_signal = next(x for x in self.signals if x.id == id)

			#multiple signals mapped to the same output
			if prev_signal.out.startswith("PO"):
				in1 = f"sig_{prev_signal.in1}" if not prev_signal.in1.startswith("PI") else prev_signal.in1
				in2 = f"sig_{prev_signal.in2}" if not prev_signal.in2.startswith("PI") else prev_signal.in2
				groups = [match.group(1), in1, prev_signal.op, in2]
				op = prev_signal.op

			else:
				prev_signal.out = self.POy[match.group(1)]
				return #does not create a new gate, just updates an existing one

		elif match := re.match(neg_pat, line):
			groups = [match.group(1), match.group(2), "NOT", match.group(2)]
			op = "NOT"

		elif match := re.match(same_sig_pat, line):
			groups = [match.group(1), match.group(2), "SET", match.group(2)]
			op = "SET"

		elif line.startswith("assign sig"):
			raise Exception(f"Error: Unknown Signal assign Expression.\n{line}")
		
		else:
			return
		
		self.op_sequence.append(log_ops[op])

		signal = SignalAssign(groups)
		signal.parse_params(self.PIxy, self.POy, self.output_signals, self.latest_id)

		self.signals.append(signal)

		self.latest_id = signal.id

	####################################################################
		
	def output_assignments(self, line: str):
		"""Checks for assignments of signals to output bits in the verilog file
		and parses them accordingly.
		"""
		line = line.strip()

		#eg. assign O[1] = sig_100;
		sig_pat = r'assign\s+O\[([0-9]+)\]\s+=\s+sig_([0-9]+)\s*;'

		#eg. assign O[2] = 1'b0;
		zero_pat = r"assign\s+O\[([0-9]+)\]\s+=\s+1'b0\s*;"

		if match := re.match(sig_pat, line):
			self.output_signals[match.group(2)] = f"POy[{match.group(1)}]"
		
		elif match := re.match(zero_pat, line):
			self.output_zeros.append(int(match.group(1)))

	####################################################################
		
	def PIxy_mapping(self):
		partA = {f'{self.input_names[0]}[{i}]' : f'PIxy[{i}]' for i in range(self.input_bits)}
		partB = {f'{self.input_names[1]}[{i}]' : f'PIxy[{i+self.input_bits}]' for i in range(self.input_bits)}
		
		partA.update(partB)
		
		self.PIxy = partA
	
	####################################################################

	def POy_mapping(self):
		self.POy = {f'{self.output_name}[{i}]' : f'POy[{i}]' for i in range(self.output_bits)}

	####################################################################
		
	def update_signals(self):
		for sig in self.signals:
			if sig.in1.startswith("PO"):
				input_signal = next(x for x in self.signals if x.out == sig.in1)
				sig.change_in1 = input_signal.change_out
			
			if sig.in2.startswith("PO"):
				try:
					input_signal = next(x for x in self.signals if x.out == sig.in2)
				except:
					print(sig)

				sig.change_in2 = input_signal.change_out

			if sig.in1 in self.output_signals.keys():
				sig.in1 = self.output_signals[sig.in1]

			if sig.in2 in self.output_signals.keys():
				sig.in2 = self.output_signals[sig.in2]

	####################################################################
		
	def generate_global_dec(self) -> str:
		"""loads up the global_dec UPPAAL template and updates it with the data obtained from
		the verilog input file.
		"""
		with open("./templates/global_dec_template.xml") as f:
			original = f.readlines()

		global_dec = original

		for i, line in enumerate(original):
			line = line.strip()
			#max int value
			if line == "const int MAX_INT = 65536;":
				global_dec[i] = f"const int MAX_INT = {self.max_int};\n"

			#number of input bits
			if line == "const int NIB_MUL2 = 4;":
				global_dec[i] = f"const int NIB_MUL2 = {self.input_bits * 2};\n"

			#number of output bits
			elif line == "const int NOB_MUL2 = 4;":
				global_dec[i] = f"const int NOB_MUL2 = {self.output_bits};\n"

			#max possible number of bits for any 2 input numbers
			elif line == "const int NIB_ANY = 4;":
				global_dec[i] = f"const int NIB_ANY = {self.input_bits * 2};\n"

			#max possible number of bits for any output number
			elif line == "const int NOB_ANY = 4;":
				global_dec[i] = f"const int NOB_ANY = {self.output_bits};\n"

			#number of broadcast 'change' channels
			elif line == "broadcast chan change[1000];" and self.channel_count > 1000:
				global_dec[i] = f"broadcast chan change[{self.channel_count}];\n"

			#max number of inner nodes
			elif line == "const int MAX_INNER_NODES = 1000;" and self.channel_count > 1000:
				global_dec[i] = f"const int MAX_INNER_NODES = {self.channel_count};\n"

			#max number of gates
			elif line == "const int MAX_INNER_GATES = 1000;" and self.channel_count > 1000:
				global_dec[i] = f"const int MAX_INNER_GATES = {self.channel_count};\n"

			#input bits indexing
			elif line == "const int PIxy[NPI] = {0,1,2,3};":
				num_sequence = ", ".join([str(i) for i in list(range(self.input_bits * 2))])
				global_dec[i] = f"const int PIxy[NPI] = {{{num_sequence}}};\n"

			#output bits indexing (accurate multiplier)
			elif line == "const int POx[NPO] = {4,5,6,7};":
				num_sequence = ", ".join([str(i) for i in list(range(self.input_bits*2, self.input_bits*2+self.output_bits))])
				global_dec[i] = f"const int POx[NPO] = {{{num_sequence}}};\n"

			#output bits indexing (inaccurate multiplier)
			elif line == "const int POy[NPO] = {8,9,10,-1};":
				num_sequence = list(range(self.input_bits*2+self.output_bits, self.input_bits*2+self.output_bits*2))
				for index in self.output_zeros:
					num_sequence[index] = -1

				num_sequence = ", ".join([str(i) for i in num_sequence])
				global_dec[i] = f"const int POy[NPO] = {{{num_sequence}}};\n"

			#logical operator sequence size
			elif line == "const int NCOM = 7;":
				op_count = len(self.op_sequence) + 1
				global_dec[i] = f"const int NCOM = {op_count};\n"

			#logical operator sequence
			elif line == "tOp tbl_op[NCOM] = {2, 2, 4, 2, 2, 0, 1};":
				self.op_sequence.append(1)
				seq = ", ".join([str(s) for s in self.op_sequence])
				global_dec[i] = f"tOp tbl_op[NCOM] = {{{seq}}};\n"

		return "".join(global_dec)

	####################################################################
		
	def generate_tmul2_any(self) -> str:
		"""loads up the tmul2_any UPPAAL template and updates it with the data obtained from
		the verilog input file.
		"""
		with open("./templates/tmul2_any_template.xml") as f:
			original = f.readlines()

		tmul2_any = original

		for i, line in enumerate(original):
			line = line.strip()

			#bits array assignments
			if line == "void f(){":
				file_index = i+1
				ttbl_index_delta = 1

				#generate one line for each bit starting from MSB
				for j in range(self.output_bits-1, -1, -1):
					tmul2_any.insert(file_index, f"    if(POx[{j}]>=0) bits[POx[{j}]]=ttbl[bin2dec()][{j+ttbl_index_delta}];\n")
					file_index += 1
					ttbl_index_delta += 2

		return "".join(tmul2_any)

	####################################################################
		
	def generate_tmul2_tb_exhaust(self) -> str:
		"""loads up the tmul2_tb_exhaust UPPAAL template and updates it with the data obtained from
		the verilog input file.
		"""
		with open("./templates/tmul2_tb_exhaust_template.xml") as f:
			original = f.readlines()

		tmul2_tb_exhaust = original

		for i, line in enumerate(original):
			line = line.strip()

			#bits array assignments
			if line == "void f(){":
				file_index = i+1

				for j in range(self.input_bits):
					tmul2_tb_exhaust.insert(file_index, f"    bits[PIxy[{j}]] = getBit({j}, input);\n")
					file_index += 1

		return "".join(tmul2_tb_exhaust)

	####################################################################
		
	def generate_system_dec(self) -> str:
		"""loads up the system_dec UPPAAL template and updates it with the data obtained from
		the verilog input file.
		"""
		#prepare the gates
		gates = []
		for i, sig in enumerate(self.signals):
			gate = sig.generate_gate(i)
			gates.append(gate)

		with open("./templates/system_dec_template.xml") as f:
			original = f.readlines()

		system_dec = original

		for i, line in enumerate(original):
			line = line.strip()

			if line == "//mul2Atb = tmul2_tb_nondet(PIxy[0], PIxy[3], DLY_MUL2, COVERAGE_RATIO);":
				system_dec[i] = f"//mul2Atb = tmul2_tb_nondet(PIxy[0], PIxy[{self.input_bits-1}], DLY_MUL2, COVERAGE_RATIO);\n"

			if line == "//gates":
				file_index = i + 1
				for gate in gates:
					system_dec.insert(file_index, gate)
					file_index += 1

		#composition
		for gate in gates:
			name = gate.split(" ")[0]
			system_dec.append(f"{name},\n")

		system_dec[-1] = system_dec[-1][:-2] + ";\n"

		system_dec.append("</system>\n")

		return "".join(system_dec)

	####################################################################

	def generate_tmul2_tb_random(self, distribution: str) -> str:
		"""loads up the tmul2_tb_random UPPAAL template and updates it with the data obtained from
		user's input arguments.
		distribution opts: ['uni_ini', 'same_triang', 'beta_uni', 'triang_beta', 'gamma_2norm', 'triang_weibull', 'same_uni', 'const_norm']
		"""
		if distribution == "uni_uni":
			comment = "    //Both inputs uniform distribution\n"
			replacement =  "    input_a = fint(random(0,imax));\n\n"

			replacement += "    input_b = fint(random(0,imax));\n"

		elif distribution == "same_triang":
			comment = "    //Both inputs same number - triangular dist. (eg. isqrt algo)\n"
			replacement =  "    input_a = fint(random_tri(-10,10,imax));\n\n"

			replacement += "    input_b = input_a;\n"

		elif distribution == "beta_uni":
			comment =  "    //Betavariate dist. and (slightly deformed) uniform dist. (eg. ellipse midpoint algo)\n"
			replacement =  "    input_a = fint(random_beta(0.5, 5.0));\n"
			replacement += "    input_a = input_a * 40;\n\n"

			replacement += "    input_b = fint(random(-10,imax));\n"
			replacement += "    if(input_b &lt; 0) { input_b = fint(random(2,15)); }\n"

		elif distribution == "triang_beta":
			comment = "    //Triangular dist. and betavariate dist. (eg. AKS primality test)\n"
			replacement =  "    input_a = fint(random_tri(-50,70,450));\n"
			replacement += "    if(input_a &gt; imax-1) { input_a = fint(random(0,150)); }\n\n"

			replacement += "    input_b = fint(random_beta(2.0,2.0));\n"
			replacement += "    input_b = input_b * 255;\n"

		elif distribution == "gamma_2norm":
			comment = "    //Gammavariate and two normal distributions (eg. Sieve of Pritchard algo.)\n"
			replacement =  "    input_a = fint(random_gamma(1.0,0.8));\n"
			replacement += "    input_a = input_a * 7;\n\n"

			replacement += "    input_b = fint(random(0,imax));\n"
			replacement += "    if(input_b &gt; 100 and input_b &lt; 175) { input_b = fint(random(0,75)); }\n"
			replacement += "    if(input_b &gt;= 175 and input_b &lt; 200) { input_b = fint(random(200,imax)); }\n"

		elif distribution == "triang_weibull":
			comment = "    //Triangular and weibullvariate distribution (eg. ElGamal Signature algo.)\n"
			replacement =  "    input_a = fint(random_tri(0,0,350));\n"
			replacement += "    if(input_a &gt; 255) { input_a = fint(random(0,50)); }\n\n"

			replacement += "    input_b = fint(random_weibull(1.7,1.7));\n"
			replacement += "    input_b = input_b * 60;"
			replacement += "    if(input_b &gt; 255) { input_b = fint(random(0,25)); }\n"

		elif distribution == "same_uni":
			comment = "    //Both inputs same number, uniform distribution (eg. Circle Point by point algo.)\n"
			replacement =  "    input_a = fint(random(2,imax));\n\n"

			replacement += "    input_b = input_a;\n"

		elif distribution == "const_norm":
			comment = "    //Constant 2 and normal distribution (eg. Bresenham line algorithm)\n"
			replacement =  "    input_a = 2;\n\n"
			replacement += "    input_b = fint(random_normal(50, 30));\n"
			replacement += "    if(input_b &lt; 0) { input_b = fint(random(100,imax)); }\n"
			
		with open("./templates/tmul2_tb_random_template.xml") as f:
			original = f.readlines()

		tmul2_tb_random = original

		for i, line in enumerate(original):
			line = line.strip()

			if line == "//Distribution":
				tmul2_tb_random[i] = comment
				tmul2_tb_random.insert(i+1, replacement)

		return "".join(tmul2_tb_random)

	####################################################################

	def append_template(self, path: str):
		"""Loads up a template for part of the xml file that requires no
		changing. Appends it to the out_files list.
		"""
		with open(path) as f:
			ret = f.readlines()

		ret = "".join(ret)
		self.out_files.append(ret)

	####################################################################
		
	def generate_parts(self, distribution: str):
		"""Takes all the templates one by one and prepares them for the final
		file generation.
		"""
		#global declarations file
		self.out_files.append(self.generate_global_dec())

		#tmul2_any file
		self.out_files.append(self.generate_tmul2_any())

		#tmul2_tb_exhaust file
		self.out_files.append(self.generate_tmul2_tb_exhaust())

		#tmul2_tb_nondet file
		self.append_template("./templates/tmul2_tb_nondet_template.xml")

		#tmul2_tb_random file
		self.out_files.append(self.generate_tmul2_tb_random(distribution))

		#syncPrimary file
		self.append_template("./templates/syncPrimary_template.xml")

		#eval_diff file
		self.append_template("./templates/eval_diff_template.xml")

		#gate2 file
		self.append_template("./templates/gate2_template.xml")

		#system declarations file
		self.out_files.append(self.generate_system_dec())

		#queries
		self.append_template("./templates/queries_template.xml")


def main():
	################################################################
	#parse input arguments
	argparser = argparse.ArgumentParser(
	                    prog='parse.py',
	                    description='Generate .xml UPPAAL files from verilog templates.')
	
	argparser.add_argument('filepath')
	argparser.add_argument('--noout', action="store_true", default=False, help="Don't save the output plot.")
	argparser.add_argument(
		'--distribution', '-d', 
		default="uni_uni",
		help="Distributions of numbers from the random number generator.",
		choices=['uni_ini', 'same_triang', 'beta_uni', 'triang_beta', 'gamma_2norm', 'triang_weibull', 'same_uni', 'const_norm']
		)
	args = argparser.parse_args()

	path = args.filepath
	out_path = f"./out/{path.split('/')[-1][:-2]}.xml"

	distribution = args.distribution

	################################################################
	#parse the input verilog file
	parser = Parser()

	with open(path) as f:
		for line in f:
			#input/output declarations
			parser.io_decs(line)

	parser.PIxy_mapping()
	parser.POy_mapping()

	with open(path) as f:
		for line in f:
			#signal assignments
			try:
				parser.signal_assignments(line)
			except Exception as e:
				print(e)
				return

			#output assignments
			parser.output_assignments(line)

	parser.update_signals()

	#generate parts of the output file
	parser.generate_parts(distribution=distribution)

	#write output to xml file
	if not args.noout:
		output = "\n".join(parser.out_files)
		with open(out_path, "w") as f:
			f.write(output)

if __name__ == "__main__":
    main()