print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to King's Island.")
print("Your mission is to find the treasure without getting seen.\n") 
left_right = input("You are at a cross road. Where do you want to go? left or right?\n\n")
if left_right == "right":
  print("\nYou fell into a hole and there is nobody to save you. Game over.")
elif left_right == "left":
  wait_swim = input("\nYou've come to a lake. There is an island in the middle of the lake. Will you wait for the boat or swim?\n\n")
  if wait_swim == "swim":
    print("\nYou get attacked by an angry trout. Game Over.")
  elif wait_swim == "wait":
    door = input("\nYou arrive at the island unharmed. There is a castle with 3 entrances. Which one do you choose? front, side or back?\n\n")
    if door == "front":
      print("\nGuards saw you sneeking in. You are in prison. Game over.")
    elif door == "side":
      print("\nA villager saw you and snitched for reward. Game over.")
    elif door == "back":
      final_door = input("\nYou successfully got in the inner rooms. There are 2 doors. One is full of the king's beasts and other one is the precious treasure you seek for. Which room do you choose? right or left?\n\n")
      if final_door == "right":
        print("\nYou found the treasure. You WON")
      elif final_door == "left":
        print("\nUnfortunately unfed beasts devoured you. Game over.")