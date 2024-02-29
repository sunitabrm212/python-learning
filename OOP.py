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
class Computer:
    def __init__(self): 
        self.name="Sunita"
        self.age=23
  

    def compare(self,other): #two para: who is calling, whom to compare
        if self.age==other.age:
            return True
        else:
            return False
        
c1=Computer()
c2=Computer()
c1.name
c2.name
c1.age=30
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")
