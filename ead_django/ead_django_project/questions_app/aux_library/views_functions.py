import logging
from django.db.models import Count
from questions_app.models import (Difficulty, Subject, Answer, Question, QuestionFromView,
                     Assessment, AssessmentQuestions)
from django.utils.decorators import decorator_from_middleware
from django.middleware.cache import CacheMiddleware
from questions_app.aux_library import models_functions
import logging

logger = logging.getLogger(__name__)

def create_questions_for_assessment(assessment_instance, question_qnty=20):
    
    assessment_questions_bulk = []
        
    #https://docs.djangoproject.com/en/5.1/ref/models/querysets/#django.db.models.query.QuerySet.filter
    #filtering using QuerySet filter() clause       
    #fetching 20 questions at random, with specified assessment diff/subj
    pre_questions = (Question.objects
                    .filter(question_difficulty__in=(assessment_instance.difficulties.split("|")),
                            question_subject__in=(assessment_instance.subjects.split("|"))
                    )                        
                    #make sure only questions with 4 answers to be returned
                    .annotate(answer_count=Count("question_answers"))
                    .filter(answer_count=4)
                    .order_by("?")[:question_qnty]
    )
    #logger.debug("assessment_test:" + str(len(pre_questions)))

    for question in pre_questions:
        #logger.debug("question_id:" + str(question.question_id))

        try:
            correct_answer = (Answer.objects
                              .filter(question_answer__exact=question.question_id)
                              .filter(correct_answer__iexact="Y") 
                              #using only filter() returns QuerySEt, by using get(), retuns single Object instance
                              .get()                        
            )
            #logger.debug("correct_answer id:"+str((correct_answer.answer_id)) ) 
            
            assessment_questions = AssessmentQuestions(
                assessment_id   = assessment_instance,
                question_id     = question,
                correct_answer  = correct_answer.answer_id
            )
            assessment_questions_bulk.append(assessment_questions)
            #assessment_questions.save()

        except Exception as e:
            logger.debug("unable to fetch correct asnwer for: " + str(correct_answer) + 
                         ":"+ str(e)
                         )
    
    #Saving every object in a bulk into DB
    AssessmentQuestions.objects.bulk_create(assessment_questions_bulk)        


def validate_assessment_score(
    assesstest_questions_querydict,
    selected_answers_dict,
    total_assessment_questions
):
    #fetching all correct answers into a dict
    correct_answers_dict = {}
    for question in assesstest_questions_querydict:       
        for correct_answer in question.question_answers.filter(correct_answer="Y"):     
            correct_answers_dict[str(question.question_id)] = str(correct_answer.answer_id) 

    correct_answer_amt = 0
    for key in correct_answers_dict:
        
        #current question for both dics, check answer
        if correct_answers_dict[key] == selected_answers_dict.get(key,"NOTFOUND"):
            correct_answer_amt = correct_answer_amt + 1

    total_score = int(round((100 * correct_answer_amt) / total_assessment_questions, 0 ))

    
    return total_score


def no_cache(view_func):
    def wrapped_view(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response["Pragma"] = "no-cache"
        response["Expires"] = "0"
        return response
    return wrapped_view
