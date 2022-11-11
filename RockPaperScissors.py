import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
your_choice = int(input("What are you going to chose?\n Type 0 for rock, 1 for paper, 2 for scissors."))
print(list[your_choice])
computers_choice = random.randint(0, 2)
print(list[computers_choice])
if your_choice >=3 or your_choice <0:
  print("You typed an invalid number. Try Again.")
elif your_choice == 0 and computers_choice == 2:
  print("You win!")
elif your_choice == 2 and computers_choice == 0:
  print("You lose.")
elif your_choice > computers_choice:
  print("You win!")
elif your_choice > computers_choice:
  print("You lose.")
elif your_choice == computers_choice:
  print("It's a draw.")