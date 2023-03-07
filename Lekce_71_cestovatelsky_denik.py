# cetovatelský deník
travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    }
]

# nadefinovaní funkce
def add_country(country_name, towns_list, visits_number):
    # vytvoreni noveho prazdneho slovniku, kam budeme ukladat nova data
    new_dictionary = {}
    # print(new dictionary) - vypíše nám pouze prázdný slovnik
    # naplnit new dictionary
    new_dictionary["country"] = country_name
    # print(new_dictionary) - vypíše se country a Italy
    new_dictionary["visited_cities"] = towns_list
    new_dictionary["visits"] = visits_number
    # print(new_dictionary) - vypíše se countr:Italy, visited_cities:Rome,Milan,Florenc, visits:9
    # napojení nového slovniku do cestovatelského deníku
    travel_diary.append(new_dictionary)

add_country("Italy", ["Milan", "Rome", "Florence"], 9)
# print(travel_diary)
print(travel_diary[2])
print(travel_diary[2]["visits"]) 