# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# __name__ variable

# import demo
# print(__name__)
# so the main function will be appeared only if it is called or else content in demo will not be displayed in calc
# import demo
# print("It's time to make tea")


#name variable in main function
from demo import add
def fun1():
    add()
    print("fun 1")
def fun2():
    print("fun 2")

def main():
    fun1()
    fun2()
main()
