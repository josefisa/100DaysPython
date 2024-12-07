import random

#mat = [[0 for _ in range(cols)] for _ in range(rows)]

numero_lindo = random.randint(1,25)
matriz = [[0 for _ in range(numero_lindo)] for _ in range(numero_lindo)]

for i in range(numero_lindo):
    for j in range(numero_lindo):
        matriz[i][j] = random.randint(48,48+24)
        
#for row in matriz:
    #print(*row)        
print(*matriz, sep='\n')