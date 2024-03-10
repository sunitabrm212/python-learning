#Object Oriented Programing
# everthing in python is an object, with attributes and methods
# class is a blue print for object

# class Computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
        
        
#     def config(self):
#         print("Config is ",self.cpu,self.ram)
    

# com1=Computer('i5',8)
# com2=Computer('i7',16)
# # Computer.config(com1)
# com1.config()
# com2.config()

#constructor creates heap memory for objects.
#self works as a pointer for objects.
# class Computer:
#     def __init__(self): 
#         self.name="Sunita"
#         self.age=23
  

#     def compare(self,other): #two para: who is calling, whom to compare
#         if self.age==other.age:
#             return True
#         else:
#             return False
        
# c1=Computer()
# c2=Computer()
# c1.name
# c2.name
# c1.age=30
# if c1.compare(c2):
#     print("They are same")
# else:
#     print("They are different")

#2 Variables in OOP: instance and static/class variable
#variable inside init is called instance, they can be changed
#variable outside init is called class variable, they will be same for all objects

#memory has namespace and it (namespace) is an area where you create and store object/variable: class namespace, object namespace
# class Car:
#     wheels=4
#     def __init__(self):
#         self.mil=10
#         self.brand="Rover Range"
# c1=Car()
# c2=Car()
# c1.mil=8
# Car.wheels=5 #to update class variable we need to call class name as it it class namespace
# print(c1.mil,c1.brand,c1.wheels)
# print(c2.mil,c2.brand,c2.wheels)

#Types of methods in OOP
#Instance method, class method and static method

#Instance method
# class Student:
#     school='Telusko'

#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avg(self):   #instance method
#         return (self.m1+self.m2+self.m3)/3
# s1=Student(20,30,40)
# s2=Student(35,45,55)
# print(int(s1.avg()))

#Class method
# class Student:
#     school='Telusko'

#     @classmethod
#     def info(cls):
#         return cls.school
    
#     @staticmethod
#     def info1():
#         print("This is a static method.")

# s1=Student()
# print(Student.info())
# Student.info1()

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop() #creating an object of inner class inside outer class
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand='Acer'
            self.cpu='i7'
            self.ram=16
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('Asika',1)
s2=Student('Akash',2)
s1.show()
s2.show()
#lap1=Student.Laptop() #creating an object of inner class outside outer class
# print(s1.lap.brand)

