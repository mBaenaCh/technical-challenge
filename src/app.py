from player import Player
from category import Category
from answer import Answer
from question import Question
from string import ascii_lowercase, digits
from random import choice
import random

ANSWERS_PER_QUESTIONS=4
MIN_NUMBER_OF_CATEGORIES = 5
MIN_NUMBER_OF_QUESTIONS = 25
NUMBER_OF_ROUNDS = 5

QUESTIONS = []
player_1 = Player(1, "Mateo", 5, True)

# Creating answers given a list of texts
def creating_answers(answers_text, correct):
    if len(answers_text) == ANSWERS_PER_QUESTIONS and 0 < correct < len(answers_text):
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
        msg = "There must be "+ ANSWERS_PER_QUESTIONS +"answers per question"
        return msg
    
# Creation of categories given a list of names 
def setting_categories(categories_names):

    if (len(categories_names) == MIN_NUMBER_OF_CATEGORIES):
        dificulty_level = 1
        random_ids = random.sample(range(1,100), len(categories_names))
        categories_list = []

        for i in range(len(random_ids)):
            category = Category(random_ids[i], dificulty_level, categories_names[i])
            print(category)
            categories_list.append(category)
            dificulty_level+=1
    
        return categories_list
    else:
        msg = "You can only have "+ str(MIN_NUMBER_OF_CATEGORIES) +" categories"
        return msg

# Creation of questions given a title, category and a list of answers
def creating_question_per_category(id, question_title, category):
    if(len(answers) == ANSWERS_PER_QUESTIONS):
        question = Question(id, question_title, category, [])
        return question
    else:
        msg = "Must have " +str(ANSWERS_PER_QUESTIONS)+ " answers per questions"
        return msg

# Asignation of a question to a bank given a category
def creating_bank_of_questions_per_category(question, categories):
    some_id = question.category_id
    bank = []
    for i in range(len(categories)):
        if(some_id == categories[i].id):
            bank.append(question)

    return bank

def assing_answers_to_question(question, answers):
    question.answer_list = answers






