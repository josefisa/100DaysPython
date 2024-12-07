import turtle
import pandas as pd
 
# Initializing the screen object
screen = turtle.Screen()
screen.title(".                     Guess all Colombian Departaments.")
map_image = "ProyectosIntermedios/Day-25-GuessStates_Pandas/colombian_dep_map.gif"
screen.addshape(map_image)
turtle.shape(map_image)

# Import the data from the csv file.
departaments = pd.read_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/departaments.csv")
# Creating two list, to avoid repeating the same answer twice.
dept_list = departaments['name'].to_list()
guess_list = []

# Search if the user input is among the options.
def checker(guess):
    if guess in guess_list:
        return False
        # elif departaments["name"].str.contains(f"{guess}").any():
    elif (departaments["name"] == guess).any():
        print(f"Yes there is {guess}")
        dept_list.remove(guess)
        guess_list.append(guess)
        print(guess_list)
        return True
    else:
        return False
        
def accesing_data(input):
    # If the guess is true
    guess_row = departaments[departaments.name == input]
    go_to = [guess_row.x_cor.values[0],guess_row.y_cor.values[0]]
    answer_writer(go_to)
       
def answer_writer(location):
    # Rode the text to the location in the map.
    dpt_name = turtle.Turtle()
    dpt_name.hideturtle()
    dpt_name.penup()
    dpt_name.goto(location)
    dpt_name.write(user_input, font=("Courier", 8, "normal"))
        
# Check for the winner
def winner():
    victory_prompt = turtle.Turtle()
    victory_prompt.hideturtle()
    victory_prompt.penup()
    victory_prompt.goto(-250,0)
    victory_prompt.write("You Won!!", font=("Courier", 80, "normal"))

game_is_on = True
while game_is_on:
    # Read the user imput and convert it to title case.
    user_input = screen.textinput(title="Guess the Departament", prompt="What's another departament's name? \n\n"
                                  +"To exit, type ESC")
    user_input =  user_input.title()
    
    # Exit on input.
    if user_input == "Esc":
        break
    
    # Check is
    if checker(user_input):
        accesing_data(user_input)
    else:
        continue
    
    if len(guess_list) == 33:
        winner()
        game_is_on = False

# # I don't see why I Should do this.
# This creates a csv archive containing those state the user could not guess.
# new_data = pd.DataFrame(dept_list)
# new_data.to_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/departaments_to_learn.csv")

screen.mainloop()