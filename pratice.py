# x=int(input("Enter first number: "))
# y=int(input("Enter second number:"))
# print(x*y)

# s1, s2, s3 = input("Enter three names").split()
# print('Name1:', s1)
# print('Name2:', s2)
# print('Name3:', s3)

# x="welcome to nepal"
# y=x.split()
# print(y)

# txt="hello, my name in Julia, I am from france"
# x=txt.split(',')
# print(x)

# a,b,c=input("Enter your name:").split()
# print("Name1:",a)
# print("Name2:",b)
# print("Name3:",c)

# list=[]
# n=int(input("Enter no. of items in list: "))
# for i in range(n):
#     x=float(input("Enter next number:"))
#     list.append(x)
# print(list)

# totalMoney = 1000
# quantity = 3
# price = 450
# # result="I have {} dollars so I can buy {} for {} dollars"
# # print(result.format(totalMoney,quantity,price))
# print(f"I have {totalMoney} dollars so I can buy {quantity} for {price} dollars")

#WHILE LOOP:
# i=0
# while not (1<=i<=100):
#     i=int(input("Entern a number between 1 and 100: "))
# print("Valid number.")

#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum
# def func(a,b):
#     mul=a*b
    
#     if mul<=1000:
#         return mul
#     else:
#         sum=a+b
#         return sum

# result=func(20,30)
# print("The result is", result)

#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
# previous_num=0
# for i in range(10):
    
#     sum=previous_num+i
#     print("Current number: ",i,"Previous Number: ",previous_num, "Sum: ",sum)
#     previous_num=i

# Write a program to accept a string from the user and display characters that are present at an even index number.
# str=input("Enter a string:")
# size=len(str)
# for i in range(0, size-1, 2):
#     print(str[i])

# Write a program to remove characters from a string starting from zero up to n and return a new string.
# s="sunita"
# n=int(input("Enter the number of lellers to remove:"))
# if not n<len(s):
#         n=int(input("Enter the number of lellers to remove:"))        
# else:
#         print(s[n:])
        
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# def func(list):
#     if list[0]==list[-1]:
#         return True
#     else:
#         return False

# list=[10,20,30,20,10]
# lst=func(list)
# print(lst)

# Iterate the given list of numbers and print only those numbers which are divisible by 5
# lst=[10,20,33,46,55]
# for i in lst:
#     if i % 5==0:
#         print(i)

#Write a program to find how many times substring “Emma” appears in the given string.
# str="Emma is a good girl. Emma is a writer"
# str1=print(str.count("Emma"))

#Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# n=int(input("Enter no. of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("\n")

#Logical operator
# age=15
# income=10000
# if age>=18 or income>=15000:
#     print("Eligible")
# else:
#     print("Not eligible")

# a=True
# b=False
# if not a:
#     print("My name is a")
# if not b:
#     print("My name is b")

# #Comparison operator
# print(bool(3>9)==False)

#Create a new list from two list using the following condition
#Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
# lst1=[10,20,25,30,35]
# lst2=[40,45,60,75,90]
# result=[]
# for i in lst1:
#     if i%2 !=0:
#         result.append(i)
# for i in lst2:
#     if i%2==0:
#         result.append(i)
# print(result)

x=10
y=11
print(x is not y)