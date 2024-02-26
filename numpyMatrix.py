from numpy import *

arr=array([
           [1,2,3],
           [4,5,6]
])
print(arr.dtype) #checks the type
print(arr.ndim) #dimension
print(arr.shape) #shows rows and column
print(arr.size) #no of elements

#to convert 2D array into 1D
arr1=arr.flatten()
print(arr1)

#converting 2D array into 3D
# arr1=array([
#             [1,2,3,4,5,6],
#             [7,8,9,3,2,1]
# ])
# arr2=arr1.reshape(2,2,3)
# print(arr2)

#Matrices
#converting array into matrix
arr3=array([
    [3,4,5,8],
    [9,7,6,8]
])
m=matrix(arr3)
print(m)

#another way of converting into matrix as input
#inserting into inverted colon and separated by semi-colon which indicates 2 row 3 col
m=matrix('1 2 3; 4 5 6')
print(m)

print(m.diagonal()) #getting diagonal
print(m.min())
print(m.max())

#matrix addition
m1=matrix('1 2 3; 4 5 6')
m2=matrix('2 3 5; 7 8 9')
m3=m1+m2
print(m3)

#matrix multiplication
m1=matrix('1 2 3; 4 5 6')
m2=matrix('2 3; 7 8; 3 6')
m3=m1*m2
print(m3)