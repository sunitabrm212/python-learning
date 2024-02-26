#array
# from array import*
# arr=array('i',[1,2,3,4,5])
# print(type(arr))
# arr.append(7)
# print(arr)

#array asking from user

from array import *
n=int(input("Enter the size of array: "))
arr=[]
for i in range(n):
    x=int(input("Enter the next number: "))
    arr.append(x)
print(arr)
