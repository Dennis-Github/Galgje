import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # puts '-' for letters not yet guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word!')

        elif user_letter in used_letters:
            print('\nYou have already used that letter!')

        else:
            print('\nThat is not a valid character!')
 
   # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
       print('You died! The word was', word)
    else:
       print('YAY! Well done! You guessed the word, congratulations!', word, '!!')

print('Welcome to Hangman! Have fun!')            

if __name__ == '__main__':
    hangman()
