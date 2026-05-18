#a decorators can be called multiple time

def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myFunc():
    return "hello world"

@changecase
def my_other_func():
    return "hello malaysia"


print(myFunc())
print(my_other_func())


