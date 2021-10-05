from numpy.lib import ufunclike
from vector_drawing import *
from random import uniform
from math import sqrt


def subract(v1, v2):
	return (v1[0] - v2[0], v1[1] - v2[1])

def length(v):
	return sqrt(v[0] ** 2 + v[1] ** 2)

def distance(v1, v2):
	return length(subract(v1, v2))

def perimeter(vectors):
	distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)]) for i in range(0, len(vectors))]
	return sum(distances)

def main():
	dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]
	print(perimeter(dino_vectors))

	for n in range(-12, 15):
		for m in range(-14, 13):
			if distance((n, m), (1, -1)) == 13 and n > m > 0:
				print((n, m))

if __name__ == '__main__':
	main()