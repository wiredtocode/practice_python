#type hints are run by mypy before compling with python complier to cather the type error 
#python is interpreted not compiled




from typing import List,Union,Optional

def calculate_area_rectangle(h:int, w:int)->int:

    return h*w


print(calculate_area_rectangle(3,4))



numbers :List[int] = ["dd",2,3,4]

print(numbers)


def a_function(a: Union [int,str]):

        print(a)

a_function("sdjnd")

#if could be integer or none 

def a_function_none(a: Optional[int]):
      print(a)

a_function_none(2323)
