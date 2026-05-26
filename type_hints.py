
"""

Docstring is used to document a function, a module or a class

#type hints are run by mypy before compling with python complier to cather the type error 
#python is interpreted not compiled


"""




from typing import List,Union,Optional



def calculate_area_rectangle(h:int, w:int)->int:
    """
    this function takes in h and width representing the height and width of the rectangle in integer 
    and it returns the area of the rectangle in integer


    """

    return h*w


print(calculate_area_rectangle(3,4))



numbers :List[int] = ["dd",2,3,4]

print(numbers)


def a_function(a: Union [int,str])-> Union [int, str]:
        """
        this function takes in a parameter of integer or string and then  returns integer or string
        
        """
        print(a)

a_function("sdjnd")

#if could be integer or none 

def a_function_none(a: Optional[int])->Optional[int]:
      """
      this function takes in integer or none and returns integer or none 
      
      """
      print(a)



a_function_none(2323)
