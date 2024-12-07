numero = input("Regalame un número del uno al cuatro")
if numero>1 and numero<4:
        print(" El número no esta en el rango: ")
else :
    match numero:
        case 1:
            print("     ... preparar datos iniciales")
        case 2:
            print("     ... preparar añadir datos")
        case 3:
            print("     ... producir consolidados")
        case 4:
            print("     ... opción implementación")
                
            