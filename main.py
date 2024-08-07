import random
# python snake_water_gun.py


'''
1 for Snake
-1 for Water
0 for Gun
'''
computer= random.choice([-1,0,1])
youstr = input('Enter the choice: ')
youDict={"S":1,"W":-1,"G":0}
reversDict ={1:"Snake",-1:"Water",0:"Gun"}

you = youDict[youstr]
# if youstr in youDict:
    # you = youDict[youstr]

print(f" you choise  {reversDict[you]}\n computer choise {reversDict[computer]}")

if (computer == you):
    print("Its a Draw!!")
else:
    if (computer == -1 and you ==1):
        print("You Win!")
    elif (computer ==-1 and you ==0):
        print("You Lost!")
    elif (computer ==1 and you ==-1):
        print("You lose!")
    elif (computer == -1 and you == 0):
        print("you win!")

    elif (computer == 0 and you == 1):
         print("you Lose!")

    else:

       print("Somthing went worng!")





