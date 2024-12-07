#This program is a secret auction; anonimus usesrs will give their bid. Unknown of other players bids, 
# and the ammount of players
# the final program will output the highest bid and who won the auction


from replit import clear
from ASCII09BlindAuction import logo
print("Welcome to the secret auction program.")

data_dict = {}

def value_changer():
    name = input("Whats your name?: ").lower()
    bid = int(input("Whats your bid?: $"))
    continuity = str(input("Are there any more bidders? Type 'yes' or 'no': ")).lower()
    return name, bid, continuity

def data_modifier(user, ammount):
    data_dict[user] = ammount

def data_access():
    max_number = 0
    name_bider = ""
    for key in data_dict:
        number = data_dict[key]
        if number > max_number:
            max_number = number
            name_bider = key
            
    return name_bider, max_number
        
    
    
    
running = True
while running:
    clear()
    print(logo)
    
    name, bid, continuity = value_changer()
    data_modifier(name, bid)
    
    if continuity == 'no':
        winner, highest_bid = data_access()
        print(f"\n The winner is {winner}, at ${highest_bid} given.\n")
        running = False
        
#print(data_dict)    
    