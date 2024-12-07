numero, digito = None, None
print("Este programa reversa números enteros POSITIVOS: \n")
numero = int(input("Digite el número a reversar: "))
print("El número en reversa es: ",end='')

while(numero>0):
    digito = numero%10
    print(int(digito), end='')
    numero -=digito
    numero /=10
    
    