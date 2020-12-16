# youtuber = "khalid"
#
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
# adj =input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")
# madlib = f"Computer programing is so {adj} It makes me so excited\
# all the time because I love to {verb1}. Stay hydrate and {verb2} like you are {famous_person}"
#
# print(madlib)

# guess game

import random

def guess(x):
    random_number =  random.randint(1, x)
    guess  = 0 #never zero
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry guess again .Too low")
        elif guess > random_number:
            print("Sorry, guess again .Too high")

    print(f"Congrats. You have guessd the number {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low  != high:
            guess = random.randint(low ,high)
        else:
            guess = low #could also be high b/c low =high
        feedback = input(f'Is {guess} too high (H), too low(L) or correct (C): '). lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'Yah The computer guess your number, {guess}, correctly')

computer_guess(1000) #choose range to 1000
