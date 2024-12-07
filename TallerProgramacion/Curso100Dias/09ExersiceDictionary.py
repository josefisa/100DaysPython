travel_log = [
    {
        "country" : "France",
        "cities" : ["Paris","Lile","Lyon","Dijon"],
        "visits" : 12,
    },
    {
        "country" : "Italy",
        "cities" : ["Milan","Rome","Palermo","Venice"],
        "visits" : 9,
    },  
]
      
country = input("Input the country: \n")
visits = int(input("Input the ammount of visits: \n"))
list_of_cities = eval(input("Input the cities: \n"))      
      
      
          
def add_new_country(name_country, numb_visits, cities_visited):
    new_country = {}
    new_country["country"] = name_country
    new_country["cities"] = cities_visited
    new_country["visits"] = numb_visits
    travel_log.append(new_country)  
    return

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times. ")
