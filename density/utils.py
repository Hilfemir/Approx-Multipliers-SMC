from pathlib import Path
from numpy.typing import NDArray

from pairs import Pairs


def find_data_file(dirname: str, filename: str | None = None) -> str:
	if filename is None:
		filename = '*.pkl'
	try:
		file_path = list(Path(dirname).glob(f"{filename}"))[0]
	except Exception as e:
		raise e

	return file_path

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

def fig_setup(ax, x: NDArray, y: NDArray, xmin: int, xmax: int, ymin: int, ymax: int):
	#labels
	ax.set_xlabel(r"x")
	ax.set_ylabel(r"y")

	#axis setup
	ax.set_xlim(xmin, xmax)
	ax.set_ylim(ymin, ymax)

def bins_setup(bins: int, binsx: int | None, binsy: int | None) -> list[int, int]:
	ret = [bins, bins]
	if binsx is not None:
		ret[0] = binsx

	if binsy is not None:
		ret[1] = binsy

	return ret