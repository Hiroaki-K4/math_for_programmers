


from numpy.lib.npyio import savez_compressed


def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def translate(translation, vectors):
	return [add(translation, v) for v in vectors]

def main():
	vectors = [(0, 0), (0, 1,), (-3, -3)]
	print(translate((1, 1), vectors))

if __name__ == '__main__':
	main()