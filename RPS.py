#rock paper sicor
import random

def play():
    user = input("What`s your choice?'r' for rock, 'p' for paper, 's' for sissor: \n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'You won'

    return 'You lost!'
def is_win(player, opponent):
    #return ture if player wins
    #r > s, s> paper, p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent =='p') or(player == 'p' and opponent == 'r'):
        return True


print(play())
print(play())
