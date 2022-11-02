import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = nato_data.to_dict()
#print(nato_dict)

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_alphabet():
    user_word = input("Choose a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, letters only")
        generate_alphabet()
    else:
        print(output_list)

generate_alphabet()
