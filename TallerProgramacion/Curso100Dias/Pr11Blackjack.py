'''
Este programa es un juego de BlackJack.
Se mezclara una baraja, y a la casa como al jugador se le daran dos.
No hay que pasarse de la linea de 21.

'''
import random
from replit import clear

Baraja = [11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10]

random.shuffle(Baraja)

def entregaCarta():
        return Baraja.pop(0)

def VerificaSi21(ManoPC,ManoUser):
    if sum(ManoPC) == 21:       
        return "\n¡La casa gana!"
    elif sum(ManoUser) == 21:
        return "\n¡Has ganado!"
    elif sum(ManoPC) > 21:
        return "\n¡La casa se pasa de 21! ¡Has ganado!"
    elif sum(ManoUser) > 21:
        return "\n¡Te has pasado de 21! ¡La casa gana!"  
        
def MuestraMano(ManoPC):
        Vector = ['?'] + ManoPC[1:]
        print(Vector)
        print("Muestra Mano fue llamado")
         
def pideMasCartas():
        respuestaJugador = input("\n¿Desea pedir otra carta? (s/n): ")
        respuestaCasa = bool(random.choice([True, False]))
        if respuestaJugador.lower() == 's' or respuestaCasa == True:
                if respuestaJugador.lower() == 's':
                      Jugador.append(entregaCarta())  
                if respuestaCasa == True:
                      print("La casa a pedido carta")  
                      Computador.append(entregaCarta())          
                return
        else:
                print("\nAl no haber pedido hay un nuevo turno")
                pideMasCartas()

                
  

Computador = [entregaCarta(),entregaCarta()]
Jugador = [entregaCarta(),entregaCarta()]
           
while True:
        clear()
        print("\n||||||||||||||||||| B L A C K J A C K ||||||||||||||||||||||||||") 
        print(f"\nMano de la casa: {Computador} \nTu mano es: {Jugador}")
        
        if( sum(Computador) >= 21 or sum(Jugador) >= 21):
                print(VerificaSi21(Computador,Jugador))
                break
        
        pideMasCartas()

print(f"\nMano de la casa: {Computador} \nTu mano es: {Jugador}")