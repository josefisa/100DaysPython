#Este programa es una calculadora, y nada más que eso.
import ASCII10Calculator

def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1 - n2
def multi(n1,n2):
    return n1 * n2
def divis(n1,n2):
    return (n1/n2)+(n1%n2)
def percen(n1,n2):
    return (n1/100)*n2
def expon(n1,n2):
    if n2 == 0:
        return 0
    return n1*expon(n1, n2-1)

operaciones = { "+":suma, "-": resta , "*": multi, "/": divis, "%":percen, "^": expon, "C":"", "E": ""}
    
def calculos(n1,ope,n2):    
    function = operaciones[ope]
    return function(n1,n2)
def numero():
    num1 = float(input("Imput N: "))
    return num1
def operan():
    symbol = input("Input O: ")
    symbol = symbol[0]
    if symbol not in operaciones:
        symbol = operan()
    return symbol

continuidad = True
primero = True

print(ASCII10Calculator.logo)
print(ASCII10Calculator.textoExplica)
while continuidad:
    print("LOGO")
    if (primero == True):
        num1 = numero()
        primero = False
        
    operation = operan()
    
    if (operation == "C"):
        num1 = numero()
        operation = operan()

    if(operation == "E"):
        print("Goodbye")
        quit()   
        
    num2 = numero()
    resultado = calculos(num1,operation,num2)
    print(f"{num1} {operation} {num2} = {resultado}")
    num1 = resultado    