
#go to demo file and delete its ccontent

"""
with open("demofile.txt", 'r') as f:
    print(f.read())

with open("demofile.txt",'w') as f:
    f.write("opps , i deleted everything and overwrite it ")


with open("demofile.txt", 'r') as f:
    print(f.read())


"""

with open("nonexistedfile.txt", 'w') as f:
    f.write("A new file ")
    
try:

    with open("demofile.txt",'x') as f:
        f.write("write ")

except:
    print("something gone wrong ")