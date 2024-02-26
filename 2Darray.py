#numpy 
from numpy import *
# arr=array([1,2,3,4,5.0])
# print(arr)
# print(arr.dtype)

#numpy
arr=linspace(1,15,20) #it takes start,stop and parts as arguments.
print(arr)

#arange
arr1=arange(1,15,2) # it takes start, stop and steps as arguments.
                   # here it will skip the second elements
print(arr1)

#logspace
arr2=logspace(1,40,5)
print(arr2)

#zeros
arr3=zeros(5, int) #size of array 5 and by default all values to be 0
print(arr3)

#zeros
arr3=ones(5)
print(arr3) #by default the output is in float value so data type should be mentioned.

#adding 5 in each value using loop
arr4= array([1,2,3,4,5])
print(arr4)
arr5=[]

for i in arr4:
    result=i+5
    arr5.append(result)
print(arr5)

#adding in numpy
arr4=arr4+5
print(arr4)
print(sin(arr4))
print(max(arr))
print(min(arr4))

#array concetenation
a=array([1,2,3,4,5])
b=array([6,7,8,9,10])
c=concatenate([a,b])
print(c)

#copying an array in python #aliasing
ar=array([6,7,8,9])
arr=ar
print(ar)
print(arr)
print(id(ar))
print(id(arr))

#shallow copying, same array with different memory address. array dependent so if updated one other will be update too.
arr=ar.view()
ar[1]=1
print(ar)
print(arr)
print(id(ar))
print(id(arr))

#deep copying, array not linked so if one array updated another will not get affected.
arr=ar.copy()
ar[1]=3
print(ar)
print(arr)
print(id(ar))
print(id(arr))