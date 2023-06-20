import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
   
while True:
    try:
        word = input("Enter a word: ").upper()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word)
        break

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)