import json
json_file = open('C:/Users/Robin/Documents/Universitet-CBS/Ekstra-studier/TechLabs/recipes_raw_nosource_epi.json')
data = json.load(json_file)
flag = 0

def dish_with_title(title):
    for dishID in data:
        entire_dish = data[dishID]
        if entire_dish['title'].find(title) != -1:
            print(title)
            print(entire_dish)

dish_with_title("Tikka Masala")
