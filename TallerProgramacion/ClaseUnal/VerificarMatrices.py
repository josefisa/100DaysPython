from random import randint
#En la siguientes lineas genero el tamaño y la cantidad de matrices, asi como defino vectores en los cuales
    #voy a guardar los datos de cuantas matrices magicas genero, y poder extraer la primera y la ultima.
n = randint(5,12)
if n%2==0:n += 1
print("La matriz tiene un tamaño de:",n," por",n)
CantidadMatrices = n*n #randint(3,3)
print("Voy a generar ",n*n,"Matrices")
PosCol, PosFil = 0,0
VecDMat = [0]*CantidadMatrices
VecConfirmacion=[]

#En este ciclo, voy generando n*n cantidad de matrices, el punto inicial de la matriz es en [0,0]
    #y voy avanzando por columna, llenando todas las filas de la columna, y luego avanzo por columna hasta n.
    #cada matriz la guardo en el vector VecDMat (Vector de Matrices)
    #si una o varias de estas matrices son magicas las guardo en VecConfirmacion (Vector de Confirmacion)
    #Los comentarios dentor del ciclo son print para verificar operaciones
    
for ContMat in range(CantidadMatrices):
    #print("Voy en el númeral: ", ContMat)
    
    s=[int(9995-5*k) for k in range(n*n)]   # para una primera corrida
    #s=[int(102+3*k) for k in range(n*n)]   # para una segunda corrida
    magico = [[int(0) for j in range(n)] for i in range(n)]
    fils=[int(0) for k in range(n)];cols=[int(0) for k in range(n)]
    dpal=[int(0) for k in range(1)];dsec=[int(0) for k in range(1)]
    
    i = PosCol;j = PosFil;magico[i][j] = s[0]
    #print("Voy en la columna ",j, " con fila ",i)
    #print("  pos. inicial:[%3d"%i,",%3d"%j,"]","  vlr. inicial: %3d"%s[0]," para N: %2d"%n)
    for k in range(1,n*n):
        i -= 1;j += 1
        if i<0:i = n-1
        if j>n-1:j = 0
        if magico[i][j]==0:
            magico[i][j] = s[k]
        else:
            i +=1;j -= 1
            if i>n-1:i = 0
            if j<0:j = n-1
            i +=1
            if i==n:i =0
            magico[i][j] = s[k]
    
    for i in range(n):
            for j in range(n):
                    fils[i] += magico[i][j];cols[j] +=magico[i][j]
                    if i == j:dpal[0] += magico[i][j]
                    if i+j == n-1:dsec[0] += magico[i][j]
                    
    if fils==cols and dpal[0]==fils[0] and dsec[0]==cols[0]:
        #print("La matriz número",ContMat)
        #print("\n  ..  SÍ es mágica")
        VecConfirmacion.append(ContMat) 
        #for i in range(n):
            #for j in range(n):
                #print(" %3d"%magico[i][j], end="")
            #print(" ")
    #else:
       # print("La Matriz número: ",ContMat)
       # print("  ..  NO es mágica")
    
    VecDMat[ContMat] = magico
           
    PosCol +=1    
    if (PosCol%n)==0:
        PosCol=0
        PosFil+=1
        
#Aqui extraigo información de los vectores de matrices y de confirmacaion para imprimir la primera y ultima matriz magica.
        
if (len(VecConfirmacion))==0:
    print("El programa no genero matrices magicas, :(, correlo de nuevo)")
else:
    print("La primera matriz magica es: ")
    Mf = len(VecConfirmacion)
    print(*VecDMat[VecConfirmacion[0]], sep='\n')
    print('  ')
    print("La ultimas matriz magica es: ")
    print(*VecDMat[VecConfirmacion[Mf-1]], sep='\n')
    print("En total se generaron ",Mf," matrices magicas. ")
