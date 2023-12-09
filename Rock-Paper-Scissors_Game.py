print("---------------ROCK PAPER SCISSORS------------------------")
print()
print("please read this instructions before you start the game")
print("you need to type your choice whether it is rock paper or scissors then based on computer's choice it will display result . Enjoy your game....")
print()
import random
def game():
    user_choice= str(input("Choose between rock paper and scissors: "))
    print("you chose: " ,user_choice)
    choices=["rock","paper","scissors"]
    computer_choice= random.choice(choices)
    print("computer chose: ",computer_choice)
    if user_choice==computer_choice:
        print("Its a tie")
    elif user_choice=="rock"and computer_choice== "scissors":
        print("Yay!! you win")
    elif user_choice=="scissors" and computer_choice=="paper":
        print("Yay!! you win")
    elif user_choice=="paper" and computer_choice=="rock":
        print("Yay!! you win")
    else:
        print("Sorry... you lost ,computer wins")       
    print()
    wish= str(input("Do you want to play again if yes type yes else type no :"))
    if (wish=="yes"):
       game() 
    else:
        print("Thanks for playing!!")

game()





