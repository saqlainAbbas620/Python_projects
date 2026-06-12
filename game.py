import random as Rnd
from dinosay import dinoprint, DINO_TYPE
import cowsay
print(" Guess Number ".center(60,'='))

List = list(DINO_TYPE.keys())

dino_name = Rnd.choice(List)
message = f"""Hi I am {dino_name} and You guess the Correct Number.
 Enter Y (Yes) if You play this game Again and See my other friends"""

cowsay.cow("HELLOOOOOOO")
print("\nLet check your Guess.Guess the Number from 1 to 100:\n")

while True:

    dino_name = Rnd.choice(List)
    message = f"""Hi I am {dino_name} and You guess the Correct Number.
    Enter Y (Yes) if You play this game Again and See my other friends"""
    random_no = Rnd.randint(1,100)

    guess_no = int(input("Guess the Number:"))
    while guess_no != random_no:
        if guess_no > random_no:
            if abs(guess_no - random_no) < 5:
                print("Almost correct Guess")
            elif abs(guess_no - random_no) < 10:
                print("It High")
            else:
                print("It Too High")
        elif guess_no < random_no:
            if abs(guess_no - random_no) < 5:
                print("Almost correct Guess")
            elif abs(guess_no - random_no) < 10:
                print("It Low")
            else:
                print("It Too Low")
        guess_no = int(input("Please Guess the Number again:"))
        if guess_no == random_no:
            break
        
    print(dinoprint(message=message, body=DINO_TYPE[dino_name]))
    num = input().lower()
    if num == 'yes' or num == 'y':
        print('Start Another Round:')
    else:
        cowsay.cow("BYE BYE")





