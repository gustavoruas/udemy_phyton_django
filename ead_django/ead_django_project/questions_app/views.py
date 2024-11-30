from questions_app.aux_library import json_datatables, models_functions, views_functions
import math
from django.shortcuts import render, get_object_or_404 ,redirect
from django.urls import reverse_lazy, reverse
from user_auth_app import models as user_auth_models
from user_auth_app import mixins as user_auth_mixins
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from .models import (Difficulty, Subject, Answer, Question, QuestionFromView,
                     Assessment, AssessmentQuestions)
from .forms import DifficultyForm, SubjectForm, AnswerForm, QuestionForm, AssessmentForm
from django.utils.decorators import decorator_from_middleware
from django.middleware.cache import CacheMiddleware
import logging
from django.db.models import Count
from django.db import connection
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage #Needed for paging
from django.contrib.auth.decorators import login_required  #for Function based Views
from django.contrib.auth.mixins import LoginRequiredMixin  #for Class based Views
from django.http import JsonResponse
from django.http.request import QueryDict

logger = logging.getLogger(__name__)


#----------------------------------------------------------------------------Difficulty
# Create your views here.
class DifficultyListView(LoginRequiredMixin,ListView):
    model = Difficulty
    #custom context
    context_object_name = "difficulty_list"
    template_name = "difficulty/difficulty_list.html"
    paginate_by =5
    
    #customize queryset
    def get_queryset(self):
        query = "SELECT * FROM tb_difficulty"
        
        #fetches get request from order column
        ordering = self.request.GET.get("orderby", None)        

        if ordering != None:
            query = query + " ORDER BY difficulty_name DESC" 
        else:
            query = query + " ORDER BY difficulty_name ASC"      
        
        
        diff_return = Difficulty.objects.raw(query)        
        #diff_return.order_by("difficulty_name")
        
        return diff_return
    

@login_required
#returns Json to interact with datatables JS
def DifficultyJson(request):
    
    response = {}
    
    query = "SELECT * FROM tb_difficulty"     
    
    response = json_datatables.json_datatable_data(
        request,
        Difficulty,
        query,
        ["difficulty_name"]    
    )  
    
    return JsonResponse(response)  


class DifficultyDetailView(LoginRequiredMixin, DetailView):
    model = Difficulty
    template_name = "difficulty/difficulty_detail.html"
    context_object_name = "difficulty_context"
    

class DifficultyCreateView(LoginRequiredMixin, CreateView):
    model=Difficulty
    form_class = DifficultyForm
    template_name = "difficulty/difficulty_form.html"       
    
    redirect_field_name = "difficulty/difficulty_list.html"
    
    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["difficulty_form"] = context["form"]     
        #defining a context to difer from Update/Create   
        context["is_update"] = False
        return context
    

class DifficultyUpdateView(LoginRequiredMixin, UpdateView):
    model = Difficulty
    form_class = DifficultyForm
    template_name = "difficulty/difficulty_form.html"
    context_object_name = "difficulty_context"
    redirect_field_name = "difficulty/difficulty_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["difficulty_form"] = context["form"] 
        #defining a context to difer from Update/Create   
        context["is_update"] = True       
        return context
    
    
class DifficultyDeleteView(LoginRequiredMixin, DeleteView):
    model = Difficulty
    template_name = "difficulty/difficulty_confirm_delete.html"
    context_object_name = "difficulty_context"
    success_url = reverse_lazy("questions_app:difficulty_list_url")
        

#----------------------------------------------------------------------------Subject
class SubjectListView(LoginRequiredMixin,ListView):
    model=Subject
    context_object_name = "subject_list"
    template_name = "subject/subject_list.html"
    
    #for pagination enabled, by default pagination context name is page_obj
    paginate_by = 5
    
    #custom query to return list
    def get_queryset(self):
        query = "SELECT * FROM tb_subject"
        
        ordering = self.request.GET.get("orderby",None)
        
        if ordering != None:
            query = query + " ORDER BY subject_name DESC"        
        else:
            query = query + " ORDER BY subject_name ASC"
                        
        #Running query, returning as a list of objects
        subject_return = Subject.objects.raw(query)
        
        return subject_return
        

class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subject/subject_detail.html"
    context_object_name = "subject_context"
    

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject/subject_form.html"
    
    redirect_field_name = "subject/subject_list.html"

    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_form"] = context["form"]
        #flag to identify UPDATE/CREATE
        context["is_update"] = False
        return context
    
    
class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subject/subject_form.html"    
    context_object_name = "subject_context"
    redirect_field_name = "subject/subject_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subject_form"] = context["form"]
        context["is_update"] = True
        return context
    

class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model=Subject
    template_name = "subject/subject_confirm_delete.html"
    context_object_name = "subject_context"
    success_url = reverse_lazy("questions_app:subject_list_url")


#----------------------------------------------------------------------------Answers
class AnswerListView(LoginRequiredMixin, ListView):
    model = Answer
    #custom context
    context_object_name = "answer_list"
    template_name = "answer/answer_list.html"
    paginate_by = 5
    
@login_required
#returns Json to interact with datatables JS
#question_id refers to what has been mapped on URLs.py, must be the same
def AnswerJson(request,question_id):    
    response = {}    
    
    save_question_id = int(question_id)
      
    query = (
        f"SELECT * FROM tb_question_answers \n"
        f"WHERE question_answer_id = {save_question_id}")
            
    response = json_datatables.json_datatable_data(
        request,
        Answer,
        query,
        [ "date_created"
          ,"answer_html_text"
          ,"correct_answer"
          ,"active"          
         ]
    )
    
    return JsonResponse(response)


class AnswerDetailView(LoginRequiredMixin, DetailView):
    model=Answer
    template_name="answer/answer_detail.html"
    context_object_name="answer_context"
    


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model=Answer
    form_class = AnswerForm
    template_name = "answer/answer_form.html"     
    #redirect_field_name = "answer/answer_list.html"
    
    #defining initial fields in create form.
    def get_initial(self):
        initial = super().get_initial()
        #defines the question of parent from URL, on create.
        question = get_object_or_404(Question, pk=self.kwargs["question_id"])
        
        initial["question_answer"] = question      
        print("did initial " + str(type(initial["question_answer"])))  
        return initial        
    
    #defining kwargs to be fetched in forms.py
    #needed to load Question from URL into form.py
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["question_id"] = self.kwargs["question_id"]
        return kwargs        
        
        
    #as QUestion is parent, must return ID from parent in order to create answer
    def form_valid(self, form):
        #passes question in filed as it is EDIT only.
        print("ran form_valid")
        #defines the question of parent from URL, on save
        form.instance.question_answer = get_object_or_404(Question, pk=self.kwargs["question_id"])
        return super().form_valid(form)  
    
    
    #to redirect to the question father page
    def get_success_url(self):
        return reverse_lazy("questions_app:question_detail_url", kwargs={"pk":self.kwargs["question_id"]})
    
    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["answer_form"] = context["form"]
        #swithch same page between UPDATE or CREATE
        context["is_update"] = False
        context["question_context"] = get_object_or_404(Question, pk=self.kwargs["question_id"])
        return context
    

class AnswerUpdateView(LoginRequiredMixin,UpdateView):
    model=Answer
    form_class=AnswerForm
    template_name="answer/answer_form.html"
    context_object_name="answer_context"
    #redirect_field_name="question/question_detail.html"

    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)        
        context["answer_form"] = context["form"]
        #swithch same page between UPDATE or CREATE
        context["is_update"] = True        
        context["question_context"] = get_object_or_404(Question, pk=self.kwargs["question_id"])        
        return context

    #defining kwargs to be fetched in forms.py, to load Question from
    #needed to load Question from URL into form.py
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["question_id"] = self.kwargs["question_id"]
        return kwargs   
    
    #redirects to specific page after update done
    def get_success_url(self):
        #self.object refers to model=Answer of the class
        return reverse('questions_app:question_detail_url',kwargs={"pk":self.object.question_answer.question_id})
    
    
class AnswerDeleteView(LoginRequiredMixin, DeleteView):
    model=Answer
    template_name = "answer/answer_confirm_delete.html"
    context_object_name = "answer_context"
    #success_url = reverse_lazy("questions_app:question_detail_url",)
    
    #as redirect to parent question, requires fetch in temp variable before delete
    def get_success_url(self):
        answer = self.get_object()
        return reverse('questions_app:question_detail_url',kwargs={"pk":self.object.question_answer.question_id})    
    
    #need to fetch Parent ID from URL for Back button
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_context"] = get_object_or_404(Question,pk=self.kwargs["question_id"])
        return context


#----------------------------------------------------------------------------Question
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    #custom_context
    context_object_name = "question_context"
    template_name = "question/question_list.html"
    paginate_by = 5
    
@login_required
#returns json for datatables listing
def QuestionJson(request):
    response = {}
    
    query = "SELECT * FROM tv1_questions"
    
    response = json_datatables.json_datatable_data(
        request,
        QuestionFromView,
        query,
        [ "date_created",
          "description",
          "difficulty_name",
          "subject_name"
        ]
        
    )
    
    return JsonResponse(response)


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = "question/question_detail.html"
    context_object_name = "question_context"
    
    
class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "question/question_form.html"
    
    redirect_field_name = "question/question_list.html"
    
    #customizing context to render in template
    #Django default, context for form is named "form"   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_form"] = context["form"]
        # for update/create page
        context["is_update"] = False
        return context
    
class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "question/question_form.html"
    context_object_name = "question_context"
    redirect_field_name = "question/question_detail.html"
    
    #customizing context to render in template
    #Django default, context for form is named "form"        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_form"] = context["form"]
        context["is_update"] = True
        
        return context
    
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = "question/question_confirm_delete.html"
    context_object_name = "question_context"
    success_url = reverse_lazy("questions_app:question_list_url")
    



#----------------------------------------------------------------------------Assessment
class AssessmentListView(LoginRequiredMixin,ListView):
    model = Assessment
    context_object_name = "assessment_context"
    template_name = "assessment/assessment_list.html"
    
@login_required
def AssessmentJson(request):
    response = {}
    
    #fetching user from request, current user logged
    current_user = request.user 
    
    #filter returns Queryset, get() returns single Object.
    roles= user_auth_models.Role.objects.filter(users=current_user)
    
    if roles.filter(name="student_role").exists():
        #replace_subject_ids is a SQL function created at Python level, and registered within jsondatatable_data()
        query = """
        SELECT assessment_id, 
            replace_difficulty_ids(difficulties) AS difficulties, 
            replace_subject_ids(subjects) AS subjects, 
            replace_user_email_by_id(assigned_to),
            status, 
            date_created, 
            date_completed, 
            score 
        FROM tb_assessments 
        WHERE assigned_to = {} 
        """
        
        query = query.format(current_user.user_id)
                
    else:    
        #replace_subject_ids is a SQL function created at Python level, and registered within jsondatatable_data()
        query = """
        SELECT assessment_id, 
            replace_difficulty_ids(difficulties) AS difficulties, 
            replace_subject_ids(subjects) AS subjects, 
            replace_user_email_by_id(assigned_to),
            status, 
            date_created, 
            date_completed, 
            score 
        FROM tb_assessments    
        """
    
    # Needs to fetch current DB connection
    conn = connection.connection
    # Register the custom SQLite function, at memory time, as SQLlite holds no DB function
    conn.create_function("replace_subject_ids", 1, 
                         lambda ids: models_functions.replace_subjects_by_id(conn, ids)) 
    
    conn.create_function("replace_difficulty_ids", 1 ,
                         lambda ids: models_functions.replace_difficulties_by_id(conn, ids))   
    
    conn.create_function("replace_user_email_by_id",1,
                         lambda ids : models_functions.replace_user_email_by_id(ids)        
    )
        
    logger.debug("user_return:" + str(models_functions.replace_user_email_by_id(3)))
    
    response = json_datatables.json_datatable_data(
        request,
        Assessment,
        query,
        [  "date_created"
           ,"date_completed"
           ,"replace_user_email_by_id(assigned_to)"  
           ,"status"
           ,"replace_subject_ids(subjects)"          #SQL functions built on runtime
           ,"replace_difficulty_ids(difficulties)"   #SQL functions built on runtime
        ]
    )
    
    return JsonResponse(response)


class AssessmentDetailView(LoginRequiredMixin,DetailView):
    model = Assessment
    template_name = "assessment/assessment_detail.html"
    context_object_name = "assessment_context"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        conn = connection.connection
        context["assessment_context"].difficulties = models_functions.replace_difficulties_by_id(
            conn, 
            context["assessment_context"].difficulties
            )
        context["assessment_context"].subjects = models_functions.replace_subjects_by_id(
            conn, 
            context["assessment_context"].subjects
            )
        return context



class AssessmentCreateView(LoginRequiredMixin,user_auth_mixins.RoleRequiredMixin,CreateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "assessment/assessment_form.html"
    
    redirect_field_name = "assessment/assessment_list.html"
    
    #lists allowed roles from CustomRoles, RoleRequiredMixin is a custom Role permission mixin
    allowed_roles = ["admin_role","teacher_role"]
    #RoleRequiredMixin has custom forbidden page, which must be referenced by attribute
    #It must reference the denied page in user_auth_app, which is named in urls.py of main project.
    permission_denied_redirect_url = "user_auth_namespace:permission_denied"    
 
    #customizing context to render in template
    #Django default, context for form is named "form"     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assessment_form"] = context["form"]
        # for update/create page
        context["is_update"] = False
        return context        
 
 
        ###################################
        ###################################
        #TO ADD to ASSESSMENTQUESTION via def form_valid(), background add into DB
    def form_valid(self, form):
        # must perform this line, in order to create an INSTANCE within form_valid
        response = super().form_valid(form)
        
        #need to instantiate via instance, the current object of Assessment being created via the
        #form object being used in the parameter        
        assessment_instance = form.instance
        
        views_functions.create_questions_for_assessment(assessment_instance)                      
                   
        return response
        
        

class AssessmentUpdateView(LoginRequiredMixin,user_auth_mixins.RoleRequiredMixin, UpdateView):
    model = Assessment
    form_class = AssessmentForm
    template_name = "assessment/assessment_form.html"
    context_object_name = "assessment_context"
    redirect_field_name = "assessment/assessment_detail.html"

    #lists allowed roles from CustomRoles, RoleRequiredMixin is a custom Role permission mixin
    allowed_roles = ["admin_role","teacher_role"]
    #RoleRequiredMixin has custom forbidden page, which must be referenced by attribute
    #It must reference the denied page url in user_auth_app, which is named in urls.py of main project.
    permission_denied_redirect_url = "user_auth_namespace:permission_denied"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assessment_form"] = context["form"]
        context["is_update"] = True
        
        return context
    
    #to define initial state of fields difficulties and subjects
    def get_initial(self):
        initial = super().get_initial()        
        #if the field has already been populated, 
        if self.object.difficulties:
            initial["difficulties"] = self.object.difficulties.split("|")
            
        if self.object.subjects:
            initial["subjects"] = self.object.subjects.split("|")            
            
        return initial
        
            
class AssessmentDeleteView(LoginRequiredMixin, user_auth_mixins.RoleRequiredMixin, DeleteView):
    model = Assessment
    template_name = "assessment/assessment_confirm_delete.html"
    context_object_name = "assessment_context"
    success_url = reverse_lazy("questions_app:assessment_list_url")
    
    #lists allowed roles from CustomRoles, RoleRequiredMixin is a custom Role permission mixin
    allowed_roles = ["admin_role","teacher_role"]
    #RoleRequiredMixin has custom forbidden page, which must be referenced by attribute
    #It must reference the denied page in user_auth_app, which is named in urls.py of main project.
    permission_denied_redirect_url = "user_auth_namespace:permission_denied"


@views_functions.no_cache  # custom annotation to aavoid back button tto reload form with selected answers
@login_required
def render_test1(request, pk):
    
    total_assessment_questions=0
    errors = []

    #fetch current assessment being worked on
    assessment = (Assessment.objects.get(assessment_id__exact = pk))
    
    if assessment.status in ("COMPLETE"):
        logger.debug(f"test {pk} already had been done")
        return redirect(reverse("questions_app:assessment_detail_url", kwargs={"pk":pk}))
    
    #fetching into var a [] of QUestion ids, with value_list(), flat=True to return only single field
    assesstest_questions_ids = (AssessmentQuestions.objects
                                .filter(assessment_id__exact=pk)        
    ).values_list("question_id",flat=True)
 
     #https://docs.djangoproject.com/en/5.1/ref/models/querysets/#django.db.models.query.QuerySet.filter
    #filtering using QuerySet filter() clause   
    assesstest_questions = (Question.objects
                            .filter(question_id__in=assesstest_questions_ids)
                            #.order_by("?")   
    )
    
    total_assessment_questions = len(assesstest_questions)
                  
    if request.method == "POST":
        questions_total_answered = 0
        request_post = request.POST        
                
        if isinstance(request_post, QueryDict):
            #converts dictionary key:value, to a key:[value]
            #list_value_dict = dict(request_post.lists())   
            list_value_dict = request_post.dict()    
                        
            #filters via iteration, only for keys that have, and removes questionradio_ from question ID             
            selected_answers_dict = {
                key.replace("questionradio_",""):value for key, value in list_value_dict.items() 
                if "questionradio_" in key 
            }
            
            questions_total_answered = len(selected_answers_dict)   
            
            if questions_total_answered < total_assessment_questions:
                errors.append("Not all questions have been answered, please review")
                                        
            if errors:
                context_return = {
                    "questions_assessment_test":assesstest_questions,        
                    "assessment_id_cont":pk,
                    "test_count":len(assesstest_questions),
                    "errors":errors,
                    "submitted_data":request_post    # returns context to check selected questions when validation fires error.
                }
                
                return render(request,"question/question_render1.html",context_return)
            
            else:
                
                #validate all selected answers against correct answers from selected questions
                total_score = views_functions.validate_assessment_score(                
                    assesstest_questions_querydict = assesstest_questions,
                    selected_answers_dict = selected_answers_dict,
                    total_assessment_questions = total_assessment_questions                
                )
                
                assessment.score = total_score
                assessment.status = "COMPLETE"
                
                assessment.save()
                              
                #REVERSE returns the URL string, so to browse to that location, redirect() is needed                                                
                return  redirect(reverse("questions_app:assessment_detail_url", kwargs={"pk":pk}))            
            
            
    context_return = {
        "questions_assessment_test":assesstest_questions,        
        "assessment_id_cont":pk,
        "test_count":len(assesstest_questions)       
    }
    
    return render(request,"question/question_render1.html",context_return)
    



