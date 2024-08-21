from django.urls import reverse
import inspect

def action_delete_column(
    edit_url_string,
    delete_url_string,
    class_attrs_dict
):
    
    #get stack of class/function position on debug
    function_name = str(inspect.stack()[1].function) 
    
    if edit_url_string is None or edit_url_string == "":
        raise ValueError(function_name+ ": Empty url string for parameter edit_url_string")
    elif delete_url_string is None or delete_url_string == "":
        raise ValueError(function_name+ ": Empty url string for parameter delete_url_string")
    elif class_attrs_dict is None:
        raise ValueError(function_name+ ": Empty url string for parameter class_attrs_dict")
    #Validates if parameter is of type dictionary
    elif not isinstance(class_attrs_dict,dict):
        raise ValueError(function_name+ ": Not a dictionary type class_attrs_dict")
    
    action_dict = {
            "action"          : 
            "<a href=" + chr(34) + (edit_url_string) + chr(34) +">" +
            "  <span class=" + chr(34) + "glyphicon glyphicon-edit" + chr(34) + "></span> " + 
            "</a> / "  +          
            "<a href=" + chr(34) + (delete_url_string) + chr(34) +">" +
            "  <span class="+ chr(34) +"glyphicon glyphicon-remove"+ chr(34) +"></span>" +
            "</a>"
        }
    
    #Appending to a dcitionary another dictionary
    class_attrs_dict.update(action_dict)
    
    return class_attrs_dict
    
    




