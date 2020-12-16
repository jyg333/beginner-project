#how to pick a random English word?
import random
import string
from word import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters =set(word)
    #set means gathering, to get unique  particle that isn`t overlapped
    #automatically delete overlapping
    alphabet = set(string.ascii_uppercase)

    used_letters = set() #what the user has guessed
    user_letter= input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user-user_letter)
    elif user_letter in used_letters:
        print("You already used that chracter.Plesas input another word.")
    else:
        print('invalid chracter. Please try again.')

hangman()
# user_input= input('type something: ')
# print(user_input)