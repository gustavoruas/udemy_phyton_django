from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse  # Use reverse to dynamically reference the URL


class RoleRequiredMixin:
    
    #attribute that class views will inherit and define roles from
    allowed_roles = []
    #saves URL.py reference to template for permdenied
    permission_denied_redirect_url = "permission_denied"
    
    
    def dispatch(self, request, *args, **kwargs):
        
        #Fetch all roles from current user - returns a list as flat=True
        user_roles = request.user.roles.values_list("name", flat=True)
                
        #check if user ha any of the allowerd_roles
        if not any(role in user_roles for role in self.allowed_roles):
            #raise PermissionDenied("You do not have permission to access this page.")
            return redirect(reverse(self.permission_denied_redirect_url))

        
        #calls function recursevily, when attribute is referenced for class RoleRequiredMixin
        return super().dispatch(request, *args, **kwargs)
    
    
    