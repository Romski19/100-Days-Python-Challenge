# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()

with open("Input/Names/invited_names.txt", "r") as names:
    all_names = names.readlines()

for names in all_names:
    strip_names = names.strip()
    with open(f"Output/ReadyToSend/{strip_names}.txt", "w") as new_letters:
        new_content = content.replace("[name]", f"{strip_names}")
        new_letters.write(new_content)