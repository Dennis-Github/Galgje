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
    word_letters = set(word)  # what's already been guessed
    alphabet = set(string.ascii_uppercase)

    


    
