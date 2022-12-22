import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

# r > s, s > p, p > r

    if is_win(user, computer):
            return("You won!")
    if not is_win(user, computer):
            return("Boo, You Lost!") 
    if user == computer:
        print("It's a tie")
        play()
    

def is_win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())