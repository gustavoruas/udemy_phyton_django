from django import template
from django.db.models.query import QuerySet

register = template.Library()

@register.simple_tag
def has_role_from_list(in_role_list, in_role_to_find):
    
    if isinstance(in_role_list, QuerySet): 
        queryset_result = in_role_list.filter(name=str(in_role_to_find))
        
        if queryset_result.exists():
            return True
        else:
            return False
    
    