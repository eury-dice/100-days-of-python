import pandas

df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row.letter: row.code for (_, row) in df_nato.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        code_words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic()
    else:
        print(code_words)


generate_phonetic()
