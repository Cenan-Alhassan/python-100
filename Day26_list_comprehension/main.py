import random
import pandas

# convert csv file into dataframe
# that dataframe becomes a dictionary

# given an input, convert to a lost of letters
# create a list of key values from dictionary if it matches the letter in the character list

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter : row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dictionary)

exception = True
while exception:
    input_letters = input("Enter word: ")
    try:
        input_letters_as_code = [nato_dictionary[letter.upper()] for letter in input_letters]
        exception = False
    except KeyError:
        print("Please enter valid word.")
    else:
        print(input_letters_as_code)