


def add(*vectors):
	return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def main():
	vectors = [(1, 2), (2, 4), (3, 6), (4, 8)]
	print(add(*vectors))


if __name__ == '__main__':
	main()