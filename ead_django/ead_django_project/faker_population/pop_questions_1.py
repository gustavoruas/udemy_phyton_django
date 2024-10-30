import os
import sys
import datetime


# Get the directory containing this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the base directory as the parent directory of faker_population
base_dir = os.path.dirname(current_dir)


sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ead_django_project.settings")

import django

django.setup()

import random
from questions_app.models import Answer, Difficulty, Question, Subject
from faker import Faker

print("Test running")

#instanciating Faker Class
fakegen = Faker()

#fetching all objects from subobjects
all_subjects = Subject.objects.all()
all_difficulties = Difficulty.objects.all()

yes_no = ["Y","N"]

def populate_questions(quantity=20):
    
    for question_loop in range(quantity):
        
        p_description         = fakegen.sentence(nb_words = 8 )
        p_question_html_text  = fakegen.sentence(nb_words = 122 )
        p_question_difficulty = random.choice(all_difficulties)
        p_question_subject    = random.choice(all_subjects)
        p_active              = random.choice(yes_no)
        p_date_created        = fakegen.date_time_this_decade().strftime("%Y-%m-%d %H:%M")
        p_date_updated        = fakegen.date_time_this_decade().strftime("%Y-%m-%d %H:%M")
        
        question = Question.objects.create(
             description         = p_description 
            ,question_html_text  = p_question_html_text
            ,question_difficulty = p_question_difficulty
            ,question_subject    = p_question_subject
            ,active              = p_active
            ,date_created        = p_date_created
            ,date_updated        = p_date_updated
        )
        
        print("**check instance: " , isinstance(question, Question))
        print("**Type of: " , type(question))
        #looping 4 answers per question
        for answer_loop in range(4):            
            p_answer_html_text  = fakegen.sentence(nb_words = 12 )
            p_date_created      = fakegen.date_time_this_decade().strftime("%Y-%m-%d %H:%M")
            p_question_answer   = question
            
            if answer_loop == 1:
                p_correct_answer    = "Y"
            else:
                p_correct_answer    = "N"
            
            p_active            = "Y"
            
            answer = Answer.objects.get_or_create(
                 answer_html_text   = p_answer_html_text
                ,date_created       = p_date_created    
                ,question_answer    = p_question_answer 
                ,correct_answer     = p_correct_answer
                ,active             = p_active            
            )          
        
populate_questions(quantity=54)

