import numpy as np
def matrix_dot_vector(a, b):
	a = np.array(a)
	b = np.array(b)
	#print(f"matrix: {a}")
	#print(f"vector: {b}")
	if a.shape[1] != b.shape[0]:
		return -1
	return np.dot(a, b)