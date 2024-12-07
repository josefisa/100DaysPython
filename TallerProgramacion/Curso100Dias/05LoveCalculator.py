print("Welcome to the love calculator!!")
name1 = input("Whats your name? \n")
name2 = input("Whats your lover's name? \n")

combined_string = name1 + name2
minuscula = combined_string.lower()

T = minuscula.count("t")
R = minuscula.count("r")
U = minuscula.count("u")
E = minuscula.count("e")
true = T+R+U+E

L = minuscula.count("l")
O = minuscula.count("o")
V = minuscula.count("v")
E = minuscula.count("e")
love = L+O+V+E

love_score = str(true) + str(love)
love_score = int(love_score)

if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")    
elif love_score>40 and love_score<50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")