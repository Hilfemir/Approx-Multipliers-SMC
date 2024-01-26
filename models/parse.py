import re

log_ops = {
	"|" : 4,
	"&" : 2,
	"^" : 6
	}

class Parser(object):
	def __init__(self):
		self.input_bits = 0 #number of input bits
		self.input_names = [] #names of the 2 input variables in the verilog file

		self.output_bits = 0 #number of output bits
		self.output_name = "O" #name of the output variable in the verilog file

		self.channel_count = 100 #number of broadcast channels

		self.op_sequence = [] #sequence of operations used in logic gates

		#mappings of names in verilog files to names in UPPAAL files
		self.PIxy = {}
		self.POy = {}

	####################################################################

	def print_status(self):
		print(f'input bits: {self.input_bits}')
		print(f'output bits: {self.output_bits}')
		print(f'number of bc channels: {self.channel_count}')

		print("\nMappings:")
		print(self.PIxy)
		print(self.POy)

		print("\nLogical operator sequence:")
		print(self.op_sequence)

	####################################################################

	def io_decs(self, line):
		"""Checks for input/output declarations in the verilog file and
		parses them accordingly.
		"""
		global input_bits, output_bits

		re_pat = r'(input|output)\s\[([0-9]+)\:0\]\s([a-zA-Z]+);'
		match = re.match(re_pat, line)

		if match is None:
			return

		if match.group(1) == "output":
			self.output_bits = int(match.group(2)) + 1
			self.output_name = match.group(3)

		else: #input
			self.input_bits = int(match.group(2)) + 1
			self.input_names.append(match.group(3))

	####################################################################

	def signal_assignments(self, line):
		"""Checks for signal assignments in the verilog file and
		parses them accordingly.
		"""
		re_pat = r'assign (sig_[0-9]+)\s*=\s*(.*?)\s(.*?)\s(.*?);'
		match = re.match(re_pat, line)

		if match is None:
			return
		
		self.channel_count += 1

		op = match.group(3)
		self.op_sequence.append(log_ops[op])

	####################################################################
		
	def PIxy_mapping(self):
		partA = {f'{self.input_names[0]}[{i}]' : f'PIxy[{i}]' for i in range(self.input_bits)}
		partB = {f'{self.input_names[1]}[{i}]' : f'PIxy[{i+8}]' for i in range(self.input_bits)}
		
		partA.update(partB)
		
		self.PIxy = partA
	
	####################################################################

	def POy_mapping(self):
		self.POy = {f'{self.output_name}[{i}]' : f'POy[{i}]' for i in range(self.output_bits)}

	####################################################################
		
	def generate_global_dec(self):
		"""loads up the global_dec UPPAAL template and updates it with the data obtained from
		the verilog input file.
		"""
		with open("./templates/global_dec_template.up") as f:
			global_dec = f.readlines()

		for i, line in enumerate(global_dec):
			line = line.strip()
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
				num_sequence = ", ".join([str(i) for i in list(range(self.input_bits*2+self.output_bits, self.input_bits*2+self.output_bits*2))])
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

		print("".join(global_dec))

	####################################################################
		
	def generate_files(self):
		#global declarations file
		self.generate_global_dec()


def main():
	parser = Parser()

	with open("./verilog/mul8u_LK8.v") as f:
		for line in f:
			#input/output declarations
			parser.io_decs(line)

			#signal assignment
			parser.signal_assignments(line)

	parser.PIxy_mapping()
	parser.POy_mapping()

	#parser.print_status()
	parser.generate_files()

if __name__ == "__main__":
    main()