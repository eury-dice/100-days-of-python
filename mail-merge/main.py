# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

LETTER_TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
NAMES_FILE_PATH = "./Input/Names/invited_names.txt"
OUTPUT_PATH = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"

names = []

with open(NAMES_FILE_PATH) as file:
    for name in file.readlines():
        names.append(name.strip())

with open(LETTER_TEMPLATE_PATH) as file:
    starting_letter_content = file.read()
for name in names:
    LETTER_PATH = (OUTPUT_PATH + "letter_for_" + name + ".txt").replace(" ", "_")
    with open(LETTER_PATH, "w") as file:
        letter_content = starting_letter_content.replace(PLACEHOLDER, name)
        file.write(letter_content)
