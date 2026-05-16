#define a decorator function that wraps another function

def deco(func):
    def inner():
        return func().upper()
    return inner



@deco      #placed here to make it more readable
def myfunc():
    return "Hello world"


print(myfunc())