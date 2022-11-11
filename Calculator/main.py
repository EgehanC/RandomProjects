from art import logo
print(logo)

def add(a, b):
  return a + b
def subtrack(a ,b):
  return a - b
def multiply(a, b):
  return a * b
def divide(a, b):
  return a / b

operations = {
              "+": add,
              "-": subtrack,
              "*": multiply,
              "/": divide
             }
def calculator():
  a = float(input("What is the first number?: "))
  #print the operations
  for op in operations:
    print(op)
  try_again = True
  
  while try_again == True:
    operation = input("Which operation above you want to perform?: ")
    b = float(input("What is the second number?: "))
    calculation = operations[operation]
    answer = calculation(a, b)
    print(f"{a} {operation} {b} = {answer}")
    #ask the user what they want to do
    i = input(f"If you want to continue calculation with {answer} type c, if you want to restart type r, if you want to stop type s")
    if i == "c":
      a = answer
    elif i == "r":
      try_again = False
      calculator()
    else:
      try_again = False
calculator()