from gamedata import data
from random import choice
from art import logo, vs

def get_random_account():
  """Returns a random account from data list"""
  return choice(data)
def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
def play():
  score = 0
  A = get_random_account()
  B = get_random_account()
  print(logo)
  game_should_continue = True
  while game_should_continue:
    A = B
    B = get_random_account()
    while A == B:
      B = get_random_account()
    print(f"Compare A: {format_data(A)}")
    print(vs)
    print(f"Against B: {format_data(B)}")
    guess = input("Guess who has more followers? A or B\n").lower()
    a_follower_count = A["follower_count"]
    b_follower_count = B["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

play()