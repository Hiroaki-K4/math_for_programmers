from matplotlib import collections
from vector_drawing import *


def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def main():
	dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)]
	draw(Points(*dino_vectors))
	draw(Points(*dino_vectors), Segment((6, 4), (3, 1)))
	draw(Points(*dino_vectors), Polygon(*dino_vectors))
	dino_vectors2 = [add((-1.5, -2.5), v) for v in dino_vectors]
	draw(Points(*dino_vectors, color=blue), Polygon(*dino_vectors, color=blue), Points(*dino_vectors2, color=red), Polygon(*dino_vectors2, color=red))
	draw(Points((2, 2), (-1, 3)), Segment((2, 2), (-1, 3), color=red))

if __name__ == '__main__':
	main()