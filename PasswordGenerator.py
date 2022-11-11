#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

list = []
i = 0
j = 0
k = 0
while i < nr_letters:
  i += 1
  list.append(letters[random.randint(0, len(letters)-1)])
while j < nr_numbers:
  j += 1
  list.append(numbers[random.randint(0, len(numbers)-1)])
while k < nr_symbols:
  k += 1
  list.append(symbols[random.randint(0, len(symbols)-1)])
random.shuffle(list)
password = ""
for char in list:
  password += char
print(f"Your password is {password}")
