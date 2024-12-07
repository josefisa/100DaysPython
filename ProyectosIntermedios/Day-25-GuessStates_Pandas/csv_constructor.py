# This is just a basic script to createa a CSV file containing.
# All the Colombian Departments, and is location relative to a .GIF map image.
# Storing those values in a DataFrame as [name]:..,
                                    #    [x_cor]
                                    #    [y_cor]
import turtle
import pandas as pd


# The list of all the departaments in Colombia.
colombian_departaments = [
    "Amazonas",
    "Antioquia",
    "Arauca",
    "Atlántico",
    "Bolívar",
    "Bogotá DC",
    "Boyacá",
    "Caldas",
    "Caquetá",
    "Casanare",
    "Cauca",
    "Cesar",
    "Chocó",
    "Córdoba",
    "Cundinamarca",
    "Guainía",
    "Guaviare",
    "Huila",
    "La Guajira",
    "Magdalena",
    "Meta",
    "Nariño",
    "Norte de Santander",
    "Putumayo",
    "Quindío",
    "Risaralda",
    "San Andrés y Providencia",
    "Santander",
    "Sucre",
    "Tolima",
    "Valle del Cauca",
    "Vaupés",
    "Vichada"
]
# colombian_departaments = ['Amazonas','Antioquia']

# Create my Screen object
screen = turtle.Screen()
screen.title(".                     Guess all US States")
map_image = "ProyectosIntermedios/Day-25-GuessStates_Pandas/colombian_dep_map.gif"
screen.addshape(map_image)

# Create my turtle object (being the map)
turtle.shape(map_image)

# Create a method to read clicks on the screen, in order to asing a location.
x_cor, y_cor = [],[]
def location_asignator(x,y):
    x_cor.append(x)
    y_cor.append(y)
    
turtle.onscreenclick(location_asignator)
screen.mainloop()

# Build the data frame from the lists.
data_frame = {
    'name'  : colombian_departaments,
    'x_cor' : x_cor,
    'y:cor' : y_cor
}

# Create a .csv archive containing information.
new_data = pd.DataFrame(data_frame)
new_data.to_csv("ProyectosIntermedios/Day-25-GuessStates_Pandas/departaments.csv", index=False)
print(x_cor,y_cor)