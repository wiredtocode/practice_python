#counter, dificulities 

import random 


var= random.randint(1,100)

print(var)
num=0

counter =0 
guesses=0


difficulties=int(input("choose a dificulities level 1,2 or 3:"))

    
print("\n")
if difficulties==1:
    guesses=5
elif difficulties==2:
    guesses=3
elif difficulties==3:
    guesses =1




while num !=var :
    try:
        num= int(input("***Guess the number*** :"))
    except:
        print(f"you have a {ValueError}")
        continue


   
    counter+=1
    guesses-=1
   
    if num>var and guesses !=0:
        print( "too high") 
        print(f"you got {guesses} guesses left")
        print("keep guessing---:()")
        

    elif num<var and guesses !=0:
        print("too low")
        print(f"you got {guesses }  guesses left")
        print("keep guessing---:()")
        
    elif num == var:
        print("you got it")
        print(f"you guessed {counter} times")
        break
    else:
        print("that was all wrong")
        
        print("Oh no, you have run out of guesses please try again ")
        break


    
