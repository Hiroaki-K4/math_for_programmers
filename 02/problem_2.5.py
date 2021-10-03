from vector_drawing import *


def main():
	tmp_list = []
	for i in range(-10, 11):
		y = i ** 2
		tmp_list.append((i, y))
	draw(Points(*tmp_list), grid=(1, 10), nice_aspect_ratio=False)


if __name__ == '__main__':
	main()