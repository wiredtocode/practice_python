def upIt(func):
    def inner(x):
        return func(x).upper()
    return inner



@upIt
def a_func(x):
    return f"A {x} is added as argument" 

print(type(a_func("job")))

print(a_func("job"))