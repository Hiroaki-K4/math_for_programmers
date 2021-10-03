from matplotlib import collections
from matplotlib.pyplot import axes, grid
from vector_drawing import *


def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def translate(translation, vectors):
	return [add(translation, v) for v in vectors]


def main():
	dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
	(-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
	(-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]
	translations = [(12*x, 10*y)
					for x in range(-5,5)
					for y in range(-5,5)]
	dinos = [Polygon(*translate(t, dino_vectors), color=blue) for t in translations]
	draw(*dinos, grid=None, axes=None, origin=None)


if __name__ == '__main__':
	main()