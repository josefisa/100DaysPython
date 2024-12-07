import random

Tu_Dato = input("Write Rock, Paper, or Scissors: \n"); Tu_Dato = Tu_Dato.lower()

objetos = ["rock","paper","scissors"]
ordenador = objetos[random.randint(0,2)]

rock ='''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

    '''
paper = '''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
'''
scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
'''

lose = "\n      You Lose !!!! \n"
win = "\n       You Win !!!! \n"

if(Tu_Dato == "rock" or Tu_Dato =="paper"  or Tu_Dato == "scissors"):
    print(f'''
        Your choice:
        {vars()[Tu_Dato]}  
        ''')
    print(f'''
          Computer's choice:
          {vars()[ordenador]}
          ''')

    if(Tu_Dato ==  ordenador):
        print("\n    It's a draw!!!")
    else:
        if(Tu_Dato == "rock" and ordenador == "paper"):
            print(lose)
        elif(Tu_Dato == "rock" and ordenador == "scissors"):
            print(win)
        elif(Tu_Dato == "paper" and ordenador == "rock"):
            print(lose)
        elif(Tu_Dato == "paper" and ordenador == "scissors"):
            print(win)
        elif(Tu_Dato == "scissors" and ordenador == "rock"):
            print(lose)
        elif(Tu_Dato == "scissors" and ordenador == "paper"):
            print(win)
        
else:
    print('''
            o      o
            
            --------
          
          Try writing again.
          ''')
        
    
        #if(Tu_Dato == "rock" and computador == "scissors" ):
        #   print("You Win!!!")
        #elif(Tu_Dato == "rock" and ):
        
    