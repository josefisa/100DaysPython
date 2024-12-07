import random

col = random.randint(5,8)
fil = random.randint(5,8)

print(col)
print(fil+"\n")

pos_col = random.randint(0,col-2)
pos_fil = random.randint(0,fil-2)

tablero = [[int(0)  for i in range(col)] for i in range(fil)]
tablero[pos_col][pos_fil]  = 1
for lst in tablero:
    print(lst, sep=" ")
