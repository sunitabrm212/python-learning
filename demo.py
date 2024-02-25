# import calc
# a=9
# b=3
# c=calc.mul(a,b)
# print(c)

# print("Hello"+__name__)
# def main():
#     print ("Hello")
#     print("Karina Musi!")

# if __name__ == "__main__":
#     main()

#name variable in main function

def add():
    print("result 1",__name__)

def sub():
    print("resutl 2")

def main():
    add()
    sub()

if __name__=="__main__": #if name value is equla to main then func will be called.
     main()