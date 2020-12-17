#how to pick a random English word?
import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
    #at first i tried I wrote return word, in 12 lines
    #after wrote return word.upper it work
def hangman():
    word = get_valid_word(words)
    word_letters =set(word)
    #set means gathering, to get unique  particle that isn`t overlapped
    #automatically delete overlapping
    alphabet = set(string.ascii_uppercase)

    used_letters = set() #what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives >0:
        #letters uesd
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        #what this dot join does is it turns this list into or interval
        #into s sting seperated by whatever the string is before dot join
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1 #teake away a life if wrong
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You already used that chracter.Plesas input another word.")
        else:
            print('invalid chracter. Please try again.')

        #get here when len(word_letters) == 0
    if lives == 0:
        print('You die')
    else:
        print('You guessed the word', word, '!!')
hangman()
# user_input= input('type something: ')
# print(user_input)
