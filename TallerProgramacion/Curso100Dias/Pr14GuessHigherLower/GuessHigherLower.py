import random
from replit import clear
from ASCII14GuessHigherLower import logo,vs
from Pr14GuessHigherLower_Data import data as datalist

random.shuffle(datalist)
advance = 1

def asignadorDatos():
    return datalist.pop(0)

def printlogo():
    print(logo)
    return 
   
def printing(AComparar_A,AComparar_B,Score):
    printlogo()
    if Score < 1:
        print(f"You are right!, Your current score is {Score}:")
    print(f"Compare A: {AComparar_A['name']} a {AComparar_A['description']} from {AComparar_A['country']}.")
    print(vs)
    print(f"Against B: {AComparar_B['name']} a {AComparar_B['description']} from {AComparar_B['country']}.")
       
def choiceImput():
    choiceString = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choiceString != 'A' and choiceString != 'B':
        print("Do it right, choice either 'A' or 'B'.")
        choiceImput() 
    return choiceString

def correctness(accountA,accountB):
    choiceString = choiceImput()
    if choiceString == 'A' and (accountA['follower_count']>accountB['follower_count']):
        return True, accountA
    if choiceString == 'B' and accountB['follower_count']>accountA['follower_count']:
        return True, accountB
    else:
        return False, None
    
    
    

AComparar_A = asignadorDatos()
AComparar_B = asignadorDatos()

while len(datalist) > 0:
    clear()
    printing(AComparar_A,AComparar_B,advance)
    
    if advance == 5:
        break
    
    rightChoice, rightData = correctness(AComparar_A,AComparar_B) 
    
    if rightData:
        AComparar_A = rightData
        AComparar_B = asignadorDatos()
    else:
        clear()     
        print("Sorry, that's wrong. Final Score:  {advance}.")
        break 
    
    advance += 1