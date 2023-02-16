with open("Input/Names/invited_names.txt") as names:
    for name in names:
        with open("Input/Letters/starting_letter.txt", "r") as letter:
            named_letter = letter.read().replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/{name}", "w") as final_letter:
                final_letter.write(named_letter)