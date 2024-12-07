n =5; m=7 #otra versión para : n filas x m columnas
t =[int(0) for k in range(m)]; matriz =[[int(i+j) for j in range(m)] for i in range(n)]
for i in range(n): print("  ",matriz[i])
suma=0;print("\n")
for j in range(m): # recorriendo la matriz por columnas
    for i in range(n): suma += matriz[i][j]
    t[j] = suma;suma=0
for k in range(m):print("%5d"%t[k],end="",sep="")
print("\n")