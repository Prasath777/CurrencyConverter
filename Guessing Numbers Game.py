import random

def guess(x):
        random_no=random.randint(1,x)
        user_guess=0
        while user_guess!=random_no:
            user_guess=int(input(f"Guess a number between 1 and {x}: "))
            if user_guess>x or user_guess<0:
                print("Number out of range")
            elif user_guess<random_no:
                print("Incorrect, guess is too low")
            elif user_guess>random_no:
                print("Incorrect, guess is too high")
        print(f"Congrats, you guessed the number {random_no} correctly")


def computer_guess(x):
         low=1
         high=x
         guessed_no=0
         feedback=""
         while feedback!='c':
             guessed_no=random.randint(low,high)
             feedback=input(f"Say whether number {guessed_no} is correct, high or low: " ).lower()
             if feedback == 'h':
                 high=guessed_no-1
             elif feedback == 'l':
                 low=guessed_no+1

         print(f"Congrats, you got it right, it was number {guessed_no}")
computer_guess(10)
