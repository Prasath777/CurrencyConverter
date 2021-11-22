import random
def play():
    print("r for rock, s for scissors, p for paper")
    user_choice= input("enter your choice: ").lower()
    computer_choice= random.choice(['r','p','s'])
    print("computer chose "+ computer_choice)
    if(user_choice==computer_choice):
        print("It's a tie")
    elif win(user_choice,computer_choice):
        print("You won")
    else:
        print("You lost")

def win(player, opponent):
    if(player=='r'and opponent=='s') or (player=='s'and opponent=='p') or (player=='p'and opponent=='r'):
        return True
    return False

play()