
import random

def is_valid_play(a):
    while a not in ["rock", "scissors", "paper"]:
        choice_player = input("I dont understand. Please type rock, scissors or paper: ")

def endgame():
    print("The end.")

def evaluate(player, computer):
    if player == "rock" and computer == "scissors":
        return "win"
    elif  == "scissors" and computer == "paper":
        return "win"
    elif player == "paper" and computer == "rock":
        return "win"

    elif player == "rock" and computer == "rock":
        return "tie"
    elif player == "scissors" and computer == "scissors":
        return "tie"
    elif player == "paper" and computer == "paper":
        return "tie"

    elif player == "scissors" and computer == "rock":
        return "loss"
    elif player == "paper" and computer == "scissors":
        return "loss"
    elif player == "rock" and computer == "paper":
        return "loss"
    else:
        print("Seems like there is an error - please tell Kim. ")


while True:
    question = input("Wanna play rock/scissors/paper? type yes/no and hit enter: ")
    if question == "yes":
        choice_playere = input("Rock, scissors or paper? ")
        is_valid_play(choice_playere)
        choice_computere = random.choice(["rock", "scissors", "paper"])
        print("Computer choose", choice_computere)
        if evaluate(choice_playere, choice_computere) == "win":
            print("You won!")
        elif evaluate(choice_playere, choice_computere) == "tie":
            print("Its a tie!")
        elif evaluate(choice_playere, choice_computere) == "loss":
            print("You lost!")
    elif question == "no":
        break
    else:
        print("I dont understand. Please type yes or no: ")
