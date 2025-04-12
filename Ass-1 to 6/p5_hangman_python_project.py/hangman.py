import random
from words import words
from hangman_visual import lives_visual_dict
import string

#in this function we well get random words until we get a valid word(no hyphen or space)
def get_valid_word(words):
    word = random.choice(words)  
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)  # Random word mil gaya like 'PYTHON'
    word_letters = set(word)      # Word ke unique letters ka set like ['P', 'Y', 'T', 'H', 'O', 'N']
    alphabet = set(string.ascii_uppercase)  # A-Z letters ka set
    used_letters = set()          # User ne kya kya guess kiya hai

    lives = 7  # Total 7 chances

    # Game ka loop continue hai jab tak word_letters ki length 0 nahi hoti ya lives 0 nahi hoti
    while len(word_letters) > 0 and lives > 0:
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # '-' for letters not yet guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        # getting user input
        # input() function se jo bhi input aata hai wo string hota hai, isliye upper() use karte hain
        user_letter = input('Guess a letter: ').upper()
    
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()