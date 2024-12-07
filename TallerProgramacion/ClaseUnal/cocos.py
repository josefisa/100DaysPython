# con m  marineros  en el rango [+2  ..  +9] usando arreglos
from random import randint
#m = randint(2,8) # marineros para posteriores corridas cuando este optimizado el programa
m=int(input("   dar un valor de m en el rango [+2  ..  +8] : "))
while m<2 or m>8:
    m=int(input("   error  ..  dar un valor de m en el rango [+2  ..  +8] : "))
mars=[int() for i in range(m+1)]
kokos=[int() for j in range(10)]
i = 0;cocos = 50000;pasos = 0;cocos0=cocos
n = 10; # número de casos válidos
while i<n:
    cocos +=1;resto = cocos
    for j in range(m+1):
        if resto%m==1:
            mars[j] = int(resto/m);resto = resto-mars[j]-1
        else:
            break
        if j==m:
            kokos[i]=cocos
            i +=1;print("  .. i: ",i,", Cocos :",cocos)
            tot = 0
            for k in range(m+1):
                print(" .. rep",k+1,":",mars[k],sep='',end='')
                tot = tot + mars[k]
            print("  ...comprobando:",tot+(m-1)*mars[m]+m+1)
    pasos +=1
print("Pasos:",pasos)
q=str(input("  presionar 's' o 'S' para pasar a la parte final o cualquier otro para terminar programa :"))
if q=="s" or q=="S":
    print(kokos)
    for i in range(1,10):
        print("  ", kokos[i]-kokos[i-1],sep='',end='')
    print("\n")
    D=kokos[1]-kokos[0]
    A=kokos[0]-D;print("  A:  ",A,"  D:",D)
    for i in range(10):
        A=A+D;print("  ",A,sep='',end='')
    A=kokos[0]-D;print("\n\n  A:  ",A,"  D:",D)
    print("    Con cocos>",cocos0,"  y para marineros=",m,"     y=",A," + ",D,"*X   con X entero > 0")
    for x in range(1,11):
        y=A+D*x;print("  ",y,sep='',end='')
    print("\n")
