from numpy.lib import ufunclike
from vector_drawing import *
from random import uniform


def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def translate(translation, vectors):
	return [add(translation, v) for v in vectors]


def scale(scalar, v):
	return (scalar * v[0], scalar * v[1])


def random_r():
	return uniform(-3, 3)


def random_s():
	return uniform(-1, 1)


def main():
	u = (-1, 1)
	v = (1, 1)
	possibilities = [add(scale(random_r(), u), scale(random_s(), v)) for i in range(0, 500)]
	draw(Points(*possibilities))


if __name__ == '__main__':
	main()