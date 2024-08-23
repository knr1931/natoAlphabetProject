import pandas as pd

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}
# print(nato_alphabet_dict)

word = input("Enter a word: ")
nato_word_list = [nato_alphabet_dict[letter.upper()] for letter in word]
print(nato_word_list)
