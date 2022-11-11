import random
from words import word_list
from art import logo
from art import stages

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You already guessed this letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    if guess not in display:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if not lives > 0:
        end_of_game = True
        print("You lose.")