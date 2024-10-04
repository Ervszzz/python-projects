import random
import os

def ask_for_input():
    while True:
        user_input = input('Enter a letter:')
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')

def print_correct_guesses(correct_guesses):
    print(f'The word is: {"".join(correct_guesses)}')

def main():
    input('Press Enter to start the game...')
    print('=' * 35)
    print('Welcome to the Hangman Game!')
    print('You have 5 lives to guess the word.')
    print('=' * 35)
    lives = 5
    word_list = []

    with open(os.path.join(os.path.dirname(__file__), 'random_words.txt'), 'r') as file:
        word_list = file.read().split()
        
    random_word = random.choice(word_list).lower()
    blanks = ['_' for _ in random_word]
    print(f'The word is: {''.join(blanks)}')

    while lives > 0:
        user_input = ask_for_input()
        if user_input not in random_word:
            lives -= 1
            print(f'You have {lives} lives left.')
        else:
            if user_input in blanks:
                print('You already guessed that letter.')
            else:
                print('Correct!')
                for index, char in enumerate(random_word):
                    if char == user_input:
                        blanks[index] = char

        print_correct_guesses(blanks)

        if '_' not in blanks:
            print('*' * 35)
            print('YOU WON THE GAME!')
            print('*' * 35)
            exit()
    else:
        print('=' * 35)
        print(f'YOU LOST THE GAME! The word was: {random_word}')
        print('=' * 35)
        exit()

if __name__ == '__main__':
    main()
