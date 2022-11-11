from art import logo
#Print the starting logo
print(logo)
#get name and bids
name_bids = {}
def add_bidder():
  winner = ""
  current_bid = 0
  name = input("What is your name?\n")
  bid = int(input("What is your bid?\n"))
  name_bids[f"{name}"] = bid
  add_new_user = input("Are there any others who want to bid? yes/no\n")
  if add_new_user == "yes":
    add_bidder()
  elif add_new_user == "no":
    for person in name_bids:
      if name_bids[f"{person}"] > current_bid:
        current_bid = name_bids[f"{person}"]
        winner = person
    print(f"\nTonight's winner is {winner} with the highest bid of {current_bid}$")  
add_bidder()
