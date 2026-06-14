import numpy as np

rng=  np.random.default_rng()

float_array = rng.random((3,4))

print(float_array)


int_array = rng.integers(low=5,high=50,size=5)


int_matrix= rng.integers(-10,11,size=(2,5))

print(int_matrix)

int_matrix[int_matrix<0]= 0

print(int_matrix)