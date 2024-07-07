from django.shortcuts import redirect
from django.urls import reverse

#Class to redirect user to login, incase its not authenticated
class AuthRequiredMiddleware:
    
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):   
        
        #defining a list of elements to not need authenticantion
        public_access = [
            reverse("user_auth_namespace:login_url"),
            reverse("user_auth_namespace:signup_url")            
        ]
        
        #Check if user is authenticated
        if not request.user.is_authenticated:            
            
            #if request.path != reverse("user_auth_namespace:login_url"):
            if request.path not in public_access:
                return redirect(reverse("user_auth_namespace:login_url"))
        
        response = self.get_response(request)
        
        return response
    
        