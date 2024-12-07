
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

df = pandas.read_csv("ProyectosIntermedios/Day-26-ListComp_NATOAlph/nato_phonetic_alphabet.csv")
#data_frame = df.to_dict() #Don't see why should I use this....
new_dict = {row.letter:row.code for (index, row) in df.iterrows()}  

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word:").upper()
nato_list = [new_dict[letter] for letter in user_word]

print(f'\n{nato_list}')