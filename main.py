# game repo
import random
'''
1  for snake
-1 for water
0 for gun
'''
computer  = random.choice([-1, 1, 0])
youstr = input("Enter your Choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reverdict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youdict[youstr]

print(f"You Choose {reverdict[you]}\nComputer Choose {reverdict[computer]}")

if(computer == you):
    print("its a draw")

else:
   
    if(computer == -1 and you == 1):
       
       print("You Win")

    elif(computer == -1 and you == 0):
        print("You Lose")

    elif(computer == 1 and you == -1):
        print("You Lose")

    elif(computer == 1 and you == 0):
        print("You Win")

    elif(computer == 0 and you == -1):
        print("You Win")

    elif(computer == 0 and you == 1):
        print("You Lose")

    else:
        print("Something Went wrong")