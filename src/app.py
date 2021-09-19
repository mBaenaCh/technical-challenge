from player import Player
from category import Category
from answer import Answer
import random

player_1 = Player(1, "Mateo", 5, True)

# Creating answers given the text of them 
def creating_answers(answers_text, correct):
    if len(answers_text) == 4 and 0 < correct < len(answers_text):
        answers_list = []   
        random_ids = random.sample(range(1, 100), len(answers_text))

        for i in range(len(answers_text)):
            if i == correct-1:

                answer = Answer(random_ids[i], answers_text[i], True)
            else: 
                answer = Answer(random_ids[i], answers_text[i], False)

            answers_list.append(answer)
            print(i , answers_list[i])
        return answers_list
    else:
        msg = "There must be 4 answers per question"
        return msg
# Creation of categories given a number and names
#RECIBIR SOLO EL NOMBRE DE LAS CATEGORIAS Y TRABAJAR CON EL LEN() DE ESE categories_name
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



