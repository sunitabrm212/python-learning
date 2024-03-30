#a type of function which takes func as an argument and returns a func
#decorates the initial func/ changes the behaviour of existing function during compiling
#adding things is done in wrapper (inner) function
# def decorators(func):
#     def wrapper():
#         print("Transaction started!!")
#         func()
#         print("Transaction ended!!")
#     return wrapper

# @decorators
# def hello():
#     print("Internal transactions going on...")
# hello()



 

def decorators(func):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrapper

@decorators
def div(a,b):
    print(a/b)
    
div(2,4)


# def div(a,b):
#     print(a/b)

# def decorators(func):
#     def wrapper(a,b):
#         if a>b:
#             a,b=b,a
#         return func(a,b)
#     return wrapper

# div=decorators(div)
# div(2,4)