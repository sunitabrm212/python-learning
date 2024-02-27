#star pattern

# n=int(input("Enter the no. of pattern:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#123 in traingle pattern

# n=int(input("Enter the no. of pattern:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
from numpy import *
# A=arange(1,10).reshape(3,3) #array shortcut creating
# B=arange(5,14).reshape(3,3)
# print(A)
# result=zeros(9,int).reshape(3,3)
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j]+=A[i][k]*B[k][j]

# print(result)

A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
B=[
    [5,6,7],
    [8,9,10],
    [11,12,13]
]
result=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range (len(B)):
            result[i][j]+=A[i][k]*B[k][j]

for i in result:
    print(i)
      