import numpy as np
# l = [1,2,3]
# arr = np.array(l)
# print(arr)
# my_mat = [[1,2,3],[2,3,4],[5,6,7]]
# np_mat = np.array(my_mat) #it will convert a nested list to a two dimensional array or matrix(3X3)
# print(np_mat)

# np.arange() --1
'''
arr2 = np.arange(0,10) 
print(arr2)
'''
# np.arange() --2
'''
# arr3 = np.arange(0,10,2) 
# print(arr3)
'''

# np.zeros() --1
'''
# arr4 = np.zeros(5) #it will create an array of zeros of length 5
# print(arr4)
'''
# np.zeros() --2
'''
arr5 = np.zeros((5,5))
print(arr5)
'''
#np.ones()
'''
arr6 = np.ones((2,4))
print(arr6)
'''

#np.linspace(a,b,n) -- Return evenly spaced numbers over a specified interval.
'''
arr7 = np.linspace(0,10,100)
print(arr7)
'''

#np.eye() -- return a two-dimensional array with ones (1) on the diagonal and zeros (0) elsewhere
'''
arr8 = np.eye(4)
print(arr8) #prints a 2-d array of size 4X4
'''

#np.random
'''
arr9 = np.random.randint(1,10,3)
print(arr9)
'''

#max,min,argmax,argmin

'''
randarr = np.random.randint(1,50,20)
print("arr: ",randarr)
maxel = randarr.max()
print(f"The Maximum value in the array is {maxel}")
max_el_ind = randarr.argmax()
print(f"The Maximum value {maxel} located at index {max_el_ind}")
minel = randarr.min()
print(f"The Minimum value in the array is {minel}")
min_el_ind = randarr.argmin()
print(f"The Maximum value {minel} located at index {min_el_ind}")
'''

#slicing of an array
'''
mtx = np.array([[1,2,3],[4,5,6],[7,8,9]])
# if you want a sub matrix of mtx, you can use slicing as bellow. 
sub_mtx = mtx[1:,0:]
print(sub_mtx)
'''

# conditional selection of arrays.
arr_a = np.arange(0,11)
print(arr_a[arr_a>5])