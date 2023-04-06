import pandas as pd

# abs_path = '/Users/arougellis/Desktop/PythonCourse/100Days/CourseWork/day-26-list-comprehension/NATO-alphabet-start/nato_phonetic_alphabet.csv'
rel_path = 'nato_phonetic_alphabet.csv'

nato_alphabet_df = pd.read_csv(rel_path)

# Step 1:
#   Create a dictionary from the `nato_phonetic_alphabet.csv`:
nato_alphabet_df = pd.read_csv(rel_path)

nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}

# Step 2:
#   Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()

code_words_list = [nato_alphabet_dict[letter] for letter in user_word]

print(code_words_list)