from pathlib import Path
from numpy.typing import NDArray

from pairs import Pairs


def find_data_file(dirname: str, filename: str | None = None) -> Path:
	if filename is None:
		filename = '*.pkl'
	try:
		file_path = list(Path(f"../in/{dirname}").glob(f"{filename}"))[0]
	except Exception as e:
		raise e

	return file_path


def get_save_path(path: str | None, data_path: Path, graph_type: str) -> Path:
	"""graph_type: either 'singular', 'heatmap' or 'bit_flips'
	"""
	if graph_type not in ['singular', 'heatmap', 'bit_flips']:
		raise ValueError("Error: graph_type has to be either 'singular', 'heatmap' or 'bit_flips'.")
	
	suff_options = {
		'singular' : '_singular.png',
		'heatmap' : '_heatmap.png',
		'bit_flips' : '_bit_flips.png'
		}
	
	suffix = suff_options[graph_type]

	if path is not None:
		if not path.endswith(suffix):
			path += suffix

		filename = path
	else:
		filename = data_path.name[:-4]
		filename += suffix

	dest = Path(filename)
	return dest


def axis_setup(
		data: Pairs,
		xmin: int | None,
		xmax: int | None
		) -> tuple[int, int]:
	if xmin is None:
		xmin = data.get_min_val()

	if xmax is None:
		xmax = data.get_max_val()
	
	return xmin, xmax


def get_range(x: NDArray, y: NDArray, xmin: int, xmax: int, ymin: int, ymax: int) -> tuple[int, int, int, int]:
	if xmin is None:
		xmin = x.min()

	if xmax is None:
		xmax = x.max()

	if ymin is None:
		ymin = y.min()

	if ymax is None:
		ymax = y.max()

	return xmin, xmax, ymin, ymax


def fig_setup(ax, x: NDArray, y: NDArray, xmin: int, xmax: int, ymin: int, ymax: int, title: str):
	#labels
	ax.set_xlabel(r"Hodnota vstupu X", fontsize=11)
	ax.set_ylabel(r"Hodnota vstupu Y", fontsize=11)

	#axis setup
	ax.set_xlim(xmin, xmax)
	ax.set_ylim(ymin, ymax)

	if title is not None:
		ax.set_title(title)


def bins_setup(bins: int, binsx: int | None, binsy: int | None) -> list[int]:
	ret = [bins, bins]
	if binsx is not None:
		ret[0] = binsx

	if binsy is not None:
		ret[1] = binsy

	return ret