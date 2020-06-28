import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses word 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # what's in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed


   # getting user input
user_letter = input('Guess a letter: ').upper()
if user_letter in alphabet - used_letters:
  used_letters.add(user_letter)
  if user_letter in word_letters:
    word_letters.remove(user_letter)





user_input = input('Type something..')
print(user_input)




    


    
