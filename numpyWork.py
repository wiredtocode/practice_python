import numpy as np

a= np.array([1,2,3]) #1D array 
b= np.array([[1,2],[3,4]])  #2 D array


#print(b)


zeros =np.zeros((2,3))


ones= np.ones((2,3))

#print(ones)
i = np.eye(10)

#print(i)

arr=  np.arange(0,10,2)    #print from 0 to 10 with increment of 2

lin = np.linspace(0,1,5)

#print(lin)

#print(arr)

rand = np.random.rand(3)

#print(rand)




#===============================================================================================================
#Array attribute

arr = np. array([[1,2,3], [4,5,6],[7,8,9],[10,11,12]])

print(arr.shape)
print(arr.size)
print(arr.dtype)   #int64 or int32
print(arr.ndim)  #always 2 if keep adding to the tuple


arr_3d = np.array([
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]

    ],
    [
        [13,14,15],
        [16,17,18],
        [19,20,21]
    ]
])



print(arr_3d.ndim)