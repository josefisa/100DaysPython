from random import randint
lista=[int(randint(-10,10)) for k in range(15)]
print (lista)
neg=[];pos=[]
for i in range(len(lista)):
    if lista[i]<=0:
        pos.append(lista[i])
    else:
        neg.append(lista[i])
suma=0
suma0=0
for i in range (len(neg)):
    suma=suma+neg[i]
for i in range (len(pos)):
    suma0=suma0+pos[i]    
print(" El promedio de los datos negativos es :", suma/len(neg))
print(" El promedio de los datos positivos es :", suma/len(pos))
print(pos,neg)
print(" c: %8.4f"%pos)