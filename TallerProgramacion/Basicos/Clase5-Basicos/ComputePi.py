MAX_DENOMINATOR=1000000
suma=0
for i in range(1,MAX_DENOMINATOR,2):
    if (i%4==1):
        suma +=(1/i)
    elif(i%4==3):
        suma -=(1/i)
    else:
        print("Imposible")
        break
    
print("El resultado es: \n ",(4*suma))