#Function 1 to check if list [1,2,3] exists in another list
def array_check(list_param, template_val_param):
    sequence_boolean = False
    
    # iterate all the list 3 by 3 elements at a tyme, stepping 1 forward.
    for i in range(len(list_param)):
        
        if i == (len(list_param) - 2):
            break
        else:
            if (list_param[i:i+3] == template_val_param):
                sequence_boolean = True
                #print(list_param[i:i+3])
                
    return sequence_boolean    


template_val_param = [1,2,3]
list_ex1 = [3,2,2,1,5,6,1,2,3,7]
list_ex2 = [3,2,1,4,5,9,654,123,32,1]

print(array_check(list_ex1, template_val_param))

#exercice 2
def string_jump(param_string):
    return param_string[::2]

print(string_jump("Heeololeo"))


#exercice 3
def arra_str_check(param_string,param_term):
        
    #searches all lowercase, for a specific pattern of char, using FIND
    string_found = str(param_string).lower().find(str(param_term).lower())
    
    if string_found != -1 :
        return True    
    else:
        return False
    

print(arra_str_check("asdabcwdw dwdw feg", "abc"))

