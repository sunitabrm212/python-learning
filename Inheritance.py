# # #Inheritance allows the process of inheriting the features of parent class to a child class
# # #Parent Class is also called as super class and child class as sub class
# # #multilevel inheritance

# # class A:
# #     def feature1(self):
# #         print("Feature 1")
# #     def feature2(self):
# #         print("Feature 2")
# # a1=A()
# # a1.feature1()
# # class B(A):
# #     def feature3(self):
# #         print("Feature 3")
# # b1=B()
# # b1.feature2()

# # class C(B):  #Class C act as a multi level inheritance by inheriting class B(parent) and class A(grand-parent)
# #     def feature4():
# #         print("Feature 4")
# # c=C()
# # c.feature3()

# #Multiple inheritance means Class C inheriting from class A and B but both A and B are independent class not inheriting from one another.
# class A:
#     def __init__(self):
#         print("in A init")
#     def ftr1(self):
#         print("Feature A ")
#     def ftr2(self):
#         print("Feature 2")
# class B():
#     def __init__(self):
#         print("in B init")
#         # super().__init__()#calling the init of superclass A
    
#     def ftr1(self):
#         print("Feature B")
# class C(A,B): #C is inheriting feature of both class A and B.(Multiple inheritance)
#     def __init__(self):
#         print("in C init")
#         super().__init__()
#     def ftr4():
#         print("Feature 4")
# #Method Resolution Order (MRO) starting from left to right. takes the left class first

# c1=C()
# c1.ftr1()

class OTTSubscription:
    def __init__(self,id,plan,total_payment):
        self.id=id
        self.plan=plan
        self.payment=total_payment
    def subscribe(self):
        print(f"Subscriber with {self.id} id subscribed with {self.plan} plan")
    def unsubscribe(self):
        print(f"Subscriber with {self.id}id subscribed with {self.plan} plan")

class premium(OTTSubscription):
    def __init__(self,id,plan,total_payment,screens):
        super().__init__(id,plan,total_payment)
        self.max_screens=screens
    def set_screen(self,screens):
        self.max_screens=screens
        print(f"maximum screen set to {self.max_screens} in premium plan")

p=premium(1,"monthly",1200,1)
p.set_screen(4)
