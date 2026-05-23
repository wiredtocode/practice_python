class myClass:
    x=5

p1 = myClass()
print(p1.x)


#all classses has built in method call  __init__ which will always executed when a class is initiateed


class myClass2:
    def __init__(self):
        print("sawatdeekap")


p2 = myClass2()


#setting default in the init parameter


class myClass3:
    def __init__(self,name,age=20):    #self is refering to the object created
        self.name=name       #self.name attach to the object , name just live in hear temporaryly

        self.age=age

p3=myClass3("amanda")
p4=myClass3("goji",99)