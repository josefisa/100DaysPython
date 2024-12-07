#import sys
#sys.path.append(r'c:\Users\jeman\CursoPython\TallerProgramacion\CursoPython'); 
import WordListHangman
import ASCII07Hangman
print(ASCII07Hangman.logo)

from replit import clear
 
import random
palabra = random.choice(WordListHangman.word_list); print(palabra)
longitud = len(palabra)
vidas = False
print(f"Tienes {vidas} intentos, ¡buena suerte!")
display = []
for i in range(longitud):
    display += "_"
    
print(f"{' '.join(display)}")
dibujito=0
muerte = False   
while muerte == False:  
    guess = input("Ingresa una letra:  ").lower()
    
    clear()
    
    for posicion in range(longitud):
        if guess == palabra[posicion]:
            display[posicion] = guess
            vidas = True

    if guess in display:
         print(f'Ya has acertado la letra {guess}') 
                  
    if "_" not in display:
        muerte = True
        print(f"{' '.join(display)}")
        print("!Has ganado el juego¡")
        print(f"Tu palabra es: {palabra} !!!")
        break
    
    if vidas == False:
        print(ASCII07Hangman.stages[dibujito])            
        dibujito+=1
    else:
        vidas = False
        print(f"{' '.join(display)}")
        
    if dibujito == len(ASCII07Hangman.stages):    
        muerte = True
        print("!!!!Has perdido el juego¡¡¡¡¡¡")
        print(f'Tu palabra era : {palabra}')