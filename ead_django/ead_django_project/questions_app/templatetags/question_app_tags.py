from django import template

register = template.Library()

@register.filter
def get_dict_item(dictionary,key):    
    return str(dictionary.get(key, ""))


@register.filter
def concat_to_str(start_str,end_str):
    return str(start_str) + str(end_str)

