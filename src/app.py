from player import Player
from category import Category
from answer import Answer
import random

player_1 = Player(1, "Mateo", 5, True)

# Creating answers given the text of them 
def creating_answers(answers_text, correct):
    answers_per_question = 4
    if len(answers_text) == answers_per_question and 0 < correct < len(answers_text):
        answers_list = []   
        random_ids = random.sample(range(101, 200), len(answers_text))

        for i in range(len(answers_text)):
            if i == correct-1:
                answer = Answer(random_ids[i], answers_text[i], True)
            else: 
                answer = Answer(random_ids[i], answers_text[i], False)

            answers_list.append(answer)
            print(i , answers_list[i])
        return answers_list
    else:
        msg = "There must be "+ answers_per_question +"answers per question"
        return msg
    
# Creation of categories given a number and names
def setting_categories(categories_names):
    number_of_categories = 5
    if (len(categories_names) == number_of_categories):
        dificulty_level = 1
        random_ids = random.sample(range(1,100), len(categories_names))
        categories_list = []

        for i in range(len(random_ids)):
            category = Category(random_ids[i], dificulty_level, categories_names[i])
            print(i, category)
            categories_list.append(category)
            dificulty_level+=1
    
        return categories_list
    else:
        msg = "You can only have "+ str(number_of_categories) +" categories"
        return msg


