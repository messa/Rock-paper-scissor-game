
import random

#this function takes players option and checks if it's correct and one of rock, paper or scissors
def is_valid_play(option):
    if option.lower() == "rock" or a.lower() == "paper" or a.lower() == "scissors":
        return True

#this function is print in the end of game when player doesn't want to play anymore
def endgame():
    print("The end.")

#this function compares player's and computer's option and returns the result of the comparsion
def evaluate(player, computer):
    #player wins
    if player == "rock" and computer == "scissors" or player == "scissors" and computer == "paper" or player == "paper" and computer == "rock":
        return "win"

    #its a tie
    elif player == "rock" and computer == "rock" or player == "scissors" and computer == "scissors" or player == "paper" and computer == "paper":
        return "tie"

    #computer wins
    elif player == "scissors" and computer == "rock" or player == "paper" and computer == "scissors" or  player == "rock" and computer == "paper":
        return "loss"

    #just for checking programming errors
    else:
        print("Seems like there is an error - please tell the author. ")

#start process
while True:
    question = input("Wanna play rock/paper/scissors? type yes/no and hit enter: ")
    question_low = question.lower()

    #player chose yes
    if question_low == "yes":
        choice_player = input("Rock, scissors or paper? ")
        choice_player_low = choice_player.lower()

        #loop if player input something else than rock/paper/scissors
        while is_valid_play(choice_player_low) != True:
            choice_player = input("I dont understand. Please type rock, paper or scissors: ")
            choice_player_low = choice_player.lower()

        #computer generates an option
        choice_computer = random.choice(["rock", "scissors", "paper"])
        print("Computer chose", choice_computer)
        if evaluate(choice_player_low, choice_computer) == "win":
            print("You won!")
        elif evaluate(choice_player_low, choice_computer) == "tie":
            print("Its a tie!")
        elif evaluate(choice_player_low, choice_computer) == "loss":
            print("You lost!")

    #player chose no
    elif question_low == "no":
        endgame()
        break

    #player answers something else than yes or no
    else:
        print("I dont understand. Please type yes or no: ")
