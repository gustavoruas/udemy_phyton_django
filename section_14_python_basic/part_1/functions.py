#custom function in python
def custom_function_1(param_1, param_2 = 5):
    print("function 1 return: " + str(param_1 * param_2))
    
#calling func
custom_function_1(3)

#validating that both params are numbers
def custom_sum_two_numbers(param_1, param_2):
    #type validates the Type of the variable
    if (type(param_1) == type(param_2) == type(1)) or (type(param_1) == type(param_2) == type(1.1)):
        return param_1 + param_2
    else:
        print("non numbers informed int the function")
        
print(custom_sum_two_numbers(22.33,33.2))

#filter list
list_1 = [2,3,4,5,7]

def return_even(param_1):
    return param_1%2 == 0

#filter returns all elements that are true, iterating from a list as second param
#filter(function_name,list_elements) => returs a list, need to CAST list()
even_nums = filter(return_even,list_1)
print(list(even_nums))

#validating elements without loop or if, returns boolean
#find 10 in the list
list_2 = [33,12,56,88,10,20]
if 10 in list_2:
    print("10 is in the list")
else:
    print("not in the list")
    
    
