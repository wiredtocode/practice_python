#define a decorator function that 

def deco(func):
    def inner():
        return func().upper()
    return inner



@deco
def myfunc():
    return "Hello world"


print(myfunc())