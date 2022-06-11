
import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    user = user.lower()



    if user in ["Rock", "rock", "r", "R"]:
        user = "r"
    elif user in ["Paper", "paper", "p", "P"]:
        user = "p"
    elif user in ["Scissors", "scissors", "s", "S"]:
        user = "s"
    else:
        print ("Invalid Choice. Please choose again.")
        exit()    

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You and the computer have both chosen {}. It's a tie.".format(computer)

    # rock > scissors, scissors > paper, paper > rock
    if is_win(user, computer):
        return "Player({}) : CPU ({}). You won! Congrats!".format(user, computer)
    
    return "Player({}) : CPU ({}). You Lost. Maybe Next Time, Buddy".format(user, computer)


def is_win(player, opponent):
    #return True if the player beats the opponent

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


print(play())
