import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {value.letter: value.code for (index, value) in nato_data.iterrows()}

user_input = input("Type in the Word : ").upper()
nato_words = []

for letter in user_input:
    nato_words.append(nato_dict[letter])

print(nato_words)