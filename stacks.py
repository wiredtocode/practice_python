#STACKS
#LIFO

#Push add an element on the stack
#POP remove an element from the stack
#peak see  the top element
#isEmpty check

#real world undo and redo 
#browser
#Function call stack

stack=[]

stack.append("book A")
stack.append("book B")
stack.append("book C")


top_element= stack[-1]
print(top_element)

removed= stack.pop()

print(removed)
print(stack)