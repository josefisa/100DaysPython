FibN1 = FibN2 = 1
Limite = 20
FibN = 0
Sumador = 0
print(FibN1,FibN2,end="")
for i in range(3,Limite+1,1):
    FibN = FibN2+FibN1
    FibN2 = FibN1
    FibN1 = FibN
    Sumador += FibN
    print(" ",FibN,end="")
    
promedio = Sumador/Limite  
