
import random

def is_valid_play(a):
    if a.lower() == "rock" or a.lower() == "paper" or a.lower() == "scissors":
        return True

def endgame():
    print("The end.")

def evaluate(player, computer):
    if player == "rock" and computer == "scissors":
        return "win"
    elif player == "scissors" and computer == "paper":
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
        print("Seems like there is an error - please tell the author. ")


while True:
    question = input("Wanna play rock/paper/scissors? type yes/no and hit enter: ")
    question_low = question.lower()
    if question_low == "yes":
        choice_player = input("Rock, scissors or paper? ")
        choice_player_low = choice_player.lower()
        while is_valid_play(choice_player_low) != True:
            choice_player = input("I dont understand. Please type rock, paper or scissors: ")
            choice_player_low = choice_player.lower()

        choice_computer = random.choice(["rock", "scissors", "paper"])
        print("Computer chose", choice_computer)
        if evaluate(choice_player_low, choice_computer) == "win":
            print("You won!")
        elif evaluate(choice_player_low, choice_computer) == "tie":
            print("Its a tie!")
        elif evaluate(choice_player_low, choice_computer) == "loss":
            print("You lost!")
    elif question_low == "no":
        endgame()
    else:
        print("I dont understand. Please type yes or no: ")
