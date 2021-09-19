from player import Player
from category import Category
import random

player_1 = Player(1, "Mateo", 5, True)

# Creation of categories given a number and names
def setting_categories(categories_number, categories_name):
    if (categories_number == len(categories_name)):
        dificulty_level = 1
        random_ids = random.sample(range(1,100), categories_number)
        categories_list = []

        for i in range(len(random_ids)):
            category = Category(random_ids[i], dificulty_level, categories_name[i])
            print(category)
            categories_list.append(category)
            dificulty_level+=1
    
        return categories_list
    else:
        msg = "You must give the same amount of names as categories"
        return msg



