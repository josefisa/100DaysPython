print( '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#)  `-.o `"=.`_.--"_o.-; ;___|__________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/____[jfigueroas]
*******************************************************************************'''
)

print("\n","\t\t\tWelcome to Treasure Island.\n\t\tYour mission is to find the treasure.")
Step1 = input("Right or left?\n"); Step1 = Step1.lower()

if(Step1!="left"):
    print("You fell into a hole, dumbass!!!\n¡¡¡GAME OVER!!!")
else:
    Step2 = input("Swim or wait??\n"); Step2 = Step2.lower()
    if(Step2 == "wait"):
        Step3 = input("Which door?\n (Blue) or (Yellow) or (Red)\n"); Step3 = Step3.lower()
        if(Step3 == "yellow"):
            print('''\n
                    /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$ /$$ /$$
                   |  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$| $$| $$
                    \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$| $$| $$
                     \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$| $$| $$
                      \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$|__/|__/
                       | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$        
                       | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$ /$$ /$$
                       |__/    \______/  \______/       |__/     \__/|______/|__/  \__/|__/|__/
                  ''')
        elif(Step3=="red"):
            print("Burned by fire.\n¡¡¡GAME OVER!!!")
        elif(Step3=="Blue"):
            print("Eaten by beasts.\n¡¡¡GAME OVER!!!")
        else:
            print("Are you stupid?, that option wasn't possible, you loose.\n¡¡¡GAME OVER!!!")        
    else:
        print("Attacked by a trout\n¡¡¡GAME OVER!!!")