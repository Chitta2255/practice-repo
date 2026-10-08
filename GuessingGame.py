#Guessing Game:
import random

def Play_Game():
    Luckynum = random.randint(1, 100)
    while True:
        User_num = int(input("Enter Your Number:"))
        if User_num == Luckynum:
            print("You Won!,Congratulations")
            break
        elif User_num < Luckynum:
            print("Too Low!")
        else:
            print("Too High!")
Play_Game()