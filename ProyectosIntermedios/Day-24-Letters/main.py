#This code will create a series of personalized letters for the members of the avatar team...
""" It will read from names.txt sotre them as a list, then it will read the base letter from starting_letter.txt
    replacing a designated space there with the names in the previous list, and finally it will create a new
    letter in a .docx format in the carpet Output..."""
    
    
""" For some unkown reason there is a problem visualizing those .docx archives in Microsoft Office Word. """

#Created by José Emanuel Figueroa Salgado _ Free Use License. Love for y'all.

with open("ProyectosIntermedios/Day-24-Letters/Input/Names/names.txt", "r") as names_file:
    names_list = names_file.readlines()
   
    with open("ProyectosIntermedios/Day-24-Letters/Input/Letters/starting_letter.txt") as base_letter:
        letter_text = base_letter.read()
    
    for i in names_list:
        final_letter_text = letter_text.replace("[name]",i.strip())
        with open(f"ProyectosIntermedios/Day-24-Letters/Output/ReadyToSend/letter_to_{i.strip()}.docx", mode="w") as new_letter:
            new_letter.write(final_letter_text)