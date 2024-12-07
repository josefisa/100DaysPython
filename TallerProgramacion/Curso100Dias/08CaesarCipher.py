import ASCII08CaesarCipher
from replit import clear
print(ASCII08CaesarCipher.titleCaesarCipher)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def direction():
    assignation = input("\nType 'encode' to encrypt, type 'decode' to decrypt, type 'esc' to exit:\n").lower()
    return assignation

def ask_data():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return text, shift

def solution(text_sample, shift_ammount, direction):
    result = ''
    maxLen = len(alphabet); maxIndex = maxLen-1; minIndex = 0
    for letter in text_sample:
        if letter in alphabet:
            if direction == 'encode':
                position = alphabet.index(letter)+ shift_ammount
            if direction == 'decode':
                position = alphabet.index(letter)- shift_ammount
                maxLen = -len(alphabet)
                
            if position >= maxIndex or position <= minIndex:
                position %= maxLen
                result += alphabet[position]
            else:    
                result += alphabet[position] 
        else:
            result += letter          
    print(f'The {direction}d text is: {result}')                           
           
control = True
while control: 
    executable = direction()
    clear()
    
    if executable == 'esc':
        print('Thanks for using this program, Goodbye! \n')
        control = False; break
    
    if executable == 'encode' or  executable == 'decode':
        text, shift = ask_data()
        solution(text, shift, executable)     
    else:        
        print('Please, try again, input a valid option')

