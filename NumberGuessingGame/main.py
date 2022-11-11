from art import logo
from random import randint

def numofattempts(difficulty):
  if difficulty == "hard":
    return 5
  elif difficulty == "medium":
    return 7
  elif difficulty == "easy":
    return 9

def play():
  answer = randint(0, 100)
  print(logo)
  print("Welcome to the number guessing game!")
  difficulty = input("Which difficulty do you want to choose? easy/medium/hard\n")
  attempts = numofattempts(difficulty)
  print(f"You have {attempts} attempts")
  is_game_over = False
  while not is_game_over and attempts > 0:
    guess = int(input("Guess: "))
    if guess == answer:
      print(f"You got it! Number was {answer}.")
      is_game_over = True
    elif guess > answer:
      print("Too high")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < answer:
      print("Too low")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
  play_again = input("Wanna play again? yes/no\n")
  if play_again == "yes":
    play()
  elif play_again == "no":
    print("Goodbye")

play()