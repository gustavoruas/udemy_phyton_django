import inspect
import logging
from user_auth_app import models as custom_user_models

logger = logging.getLogger(__name__)

def get_fk_id(fk_object, attribute_name, default_return_value="N/A"):
    #before returning field, validate attribute FK if exists, then return field
    #self.question_subject.subject_id if self.question_subject else 'N/A'
    return getattr(fk_object, attribute_name, default_return_value ) if fk_object else default_return_value


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
            "<a id=""list_update_link"" href=" + chr(34) + (edit_url_string) + chr(34) +">" +
            "  <span class=" + chr(34) + "glyphicon glyphicon-edit" + chr(34) + "></span> " + 
            "</a> / "  +          
            "<a id=""list_delete_link"" href=" + chr(34) + (delete_url_string) + chr(34) +">" +
            "  <span class="+ chr(34) +"glyphicon glyphicon-remove"+ chr(34) +"></span>" +
            "</a>"
        }
    
    #Appending to a dcitionary another dictionary
    class_attrs_dict.update(action_dict)
    
    return class_attrs_dict
    
    
#SQLite straight connection to DB, to create SQL function, as in SQLite functions are not available.
# Function to replace animal IDs with their corresponding names
def replace_subjects_by_id(conn, pipe_separated_ids):
    
    #new instance for logger
    logger = logging.getLogger(__name__)
    
    try:   
    
        # Split the input string by '|'
        subject_ids = pipe_separated_ids.split('|')

        # Create a query to fetch corresponding animal names
        query = "SELECT GROUP_CONCAT(subject_name, '; ') FROM tb_subject WHERE subject_id IN ({})"
        placeholders = ','.join('?' * len(subject_ids))
        query = query.format(placeholders)

        # Execute the query and fetch the result
        cursor = conn.cursor()
        cursor.execute(query, subject_ids)
        result = cursor.fetchone()

        # Return the animal names as a pipe-separated string
        return result[0] if result else None
    
    except Exception as e:
        logger.debug("models_functions.replace_subjects_by_id.error:%s", e)
        return None
        
def replace_difficulties_by_id(conn, pipe_separated_ids):
    logger = logging.getLogger(__name__)
    
    try:
        difficulty_ids = pipe_separated_ids.split("|")
        
        query = "SELECT GROUP_CONCAT(difficulty_name, '; ') FROM tb_difficulty WHERE difficulty_id IN ({})"
        placeholders= ','.join('?' * len(difficulty_ids))
        query = query.format(placeholders)
        
        cursor = conn.cursor()
        cursor.execute(query,difficulty_ids)
        result = cursor.fetchone()
        
        return result[0] if result else None
        
    except Exception as e:
        logger.debug("models.functions.replace_difficulties_by_id.error:%s", e)
        return None
        

def replace_user_email_by_id(id):    
    
    try:
        user_return = custom_user_models.CustomUser.objects.get(user_id=id)
        
    except Exception as e:
        logger.debug("Error:replace_user_name_by_id:" + str(e))
        return None

    return user_return.email
    

def assess_run_column(
    column_url_string,
    class_attr_dict
):
    
    function_name = str(inspect.stack()[1].function)
    
    if column_url_string is None or column_url_string=="":
        raise ValueError(function_name + ": Empty parameter defined for column_url_string")
    elif not isinstance(class_attr_dict,dict):
        raise ValueError(function_name + ": Not a dictionary type for class_attr_dict")
    
    link_text = ("<a class="+chr(34)+"btn btn-info btn-sm"+chr(34)+" href=""{}" +
        " onclick="+chr(34)+"open_custom_popup_window(this.href,950, 990);return false;"+chr(34)+"  >" +
        "Run Test</a> ")
    
    button_dict = {
        "button"    : link_text.format(column_url_string)
    }
    
    class_attr_dict.update(button_dict)
    
    return class_attr_dict
    


