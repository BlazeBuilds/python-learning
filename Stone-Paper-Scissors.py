
import random 

d={1:"stone",2:"paper",3:"Scissors"}


user=int(input("Enter the choice "))
computer=random.randint(1,3)
print(computer)

print("You : ",user)
print("Computer : ",computer)
if(user==1 and computer==2):
    print("You lost ")

elif(user==1 and computer==3):
    print("You won ")    
elif(user==2 and computer==1 ) :
    print("You won")
elif(user==2 and computer==3) :
    print("You lost ")
elif(user==3 and computer==1)    :
    print("You lost ")
elif(user==3 and computer==2):
    print("You win ")
else:
    print("DRAW")    


    #First project
    
