from matplotlib import collections
from matplotlib.pyplot import polar
from vector_drawing import *
from math import cos, pi
from vectors import to_cartesian


def main():
	polar_coords = [(cos(x*pi/100.0), 2*pi*x/1000.0) for x in range(0, 1000)]
	vectors = [to_cartesian(p) for p in polar_coords]
	draw(Polygon(*vectors, color=green))


if __name__ == '__main__':
	main()