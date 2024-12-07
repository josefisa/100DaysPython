import random
print("Welcome to the PyPassword Generator!")
nletters = input("How many letters would you like in your password? \n"); nletters = int(nletters)
nsymbols = input("How many symbols would you like? \n"); nsymbols = int(nsymbols)
nnumbers = input("How many numbers would you like? \n"); nnumbers = int(nnumbers)

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','*','+','?','¿']

password_list = []

for i in range(0,nletters):
    password_list.append(letters[random.randint(0,int(len(letters))-1)])
for i in range(0,nsymbols):
    password_list.append(random.choice(symbols))    
for i in range(0, nnumbers):
    password_list.append(random.choice(numbers))
longitud = len(password_list)

password = ''

random.shuffle(password_list)
#Primer metodo de combinación
for i in password_list:
    password += i
print(password,"\n")   

password = ''

for i in range(0,longitud):
    b = random.choice(password_list)
    password += b
    password_list.remove(b)
print(password,"\n")