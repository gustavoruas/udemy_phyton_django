from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreateForm, CustomPasswordChangeForm
from .models import Role
from django.contrib.auth.views import PasswordChangeView
# Needed to force login into accessing URLS
from django.contrib.auth.decorators import login_required  #for Function based Views
from django.contrib.auth.mixins import LoginRequiredMixin  #for Class based Views

# Create your views here.

def signup_user(request):
    
    if request.method == "POST":
        custom_user_form = CustomUserCreateForm(data=request.POST)
        
        #fires up form validation
        if custom_user_form.is_valid():
            standard_role = Role.objects.get(name="standard_user")    
                      
            
            custom_user = custom_user_form.save(commit=True)
            print("custom_user type:" + str(type(custom_user)))
            
            #Adding a role to users, using related_name attribute in ManyToManyField
            if custom_user.user_id is not None and custom_user.user_id != "":  
                custom_user.roles.add(standard_role)
                
                #if it is staff, add as ateacher, otherwise, as student.
                if custom_user.is_staff:
                    custom_user.roles.add(Role.objects.get(name="teacher_role"))
                else:
                    custom_user.roles.add(Role.objects.get(name="student_role"))
                
                custom_user.save()
            
            #redirect to login if user created successfully
            return redirect("user_auth_app:login_url")
            
    else:
        custom_user_form = CustomUserCreateForm()
        
    context_form = {"customuser_form":custom_user_form}
    
    return render(request,"signup.html",context_form)
        

#Customizing form must be called by view, must be logged in to access with LoginRequiredMixin
class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name = "change_password.html"
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("index_url")
 
    #customizing context to render in template
    #Django default, context for form is named "form"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_form"] = context["form"]
        return context 
       



#class view 
#https://stackoverflow.com/questions/68845984/does-form-valid-in-cbv-not-call-is-valid-method
#https://stackoverflow.com/questions/8903601/how-to-process-a-form-via-get-or-post-using-class-based-views
#class Signup(CreateView):
#    form_class = CustomUserCreateForm
#    
#    success_url = reverse_lazy("user_auth_app:login_url")
#    
#    template_name = "signup.html"
#    
#    #customizing context name
#    def get_context_data(self, **kwargs):
#        self.object =  self.get_object()
#        context = super().get_context_data(**kwargs)
#        context["customuser_form"] = CustomUserCreateForm
#        return context
#       
#    def form_valid(self, form):
#        return super(Signup, self).form_valid(form)
#        
#    def form_invalid(self, form):
#        return super(Signup, self).form_invalid(form)
#    
#    def post(self, request, *args, **kwargs):
#        self.object =  self.get_object() 
#        current_form = self.get_form()
#        
#        if current_form.is_valid():
#            return self.form_valid(current_form)
#        
#        else:
#            return self.form_invalid(current_form)
        
    
    
