def deco(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return inner

@deco
def a_func(name_of_gf,name_of_her_cat):
    return f"i love you {name_of_gf} and {name_of_her_cat}"


print(a_func("jennifer","mimi"))