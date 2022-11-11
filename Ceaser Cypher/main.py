from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#ciphering function
def caesar(plain_text, shift_amount, which_way):
  cipher_text = ""
  for letter in plain_text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift_amount
      elif direction == "decode":
        new_position = position - shift_amount
      cipher_text += alphabet[new_position]
    else:
      cipher_text += letter
  print(f"The final text is {cipher_text}.")

#print the starting logo
print(logo)
#Keep going or not
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(plain_text=text, shift_amount=shift, which_way=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")