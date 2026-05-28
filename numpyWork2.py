"""
Variables 
data types

"""

import numpy as np

print(np.__version__)


my_list  = [ 1,2,3,4,5  ]

print(my_list*2)

#array = np.array ([1,2,3,4])

#print(array*2)


array = np.array([['A','B','C'],
                  ['D','E','F'],
                  ['G','H','I']])

print(type(array))

print(array.ndim)

