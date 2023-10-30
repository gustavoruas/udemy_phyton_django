#Computers gues a 3 digit number
#it must say to each character if it is 
#NOPE, CLOSE MATCH
import random

def get_user_intput():
    
    try:
        user_input = int(input("Please provide a 3 digit number: "))

        if len(str(user_input)) !=3:
            print("  *** please inform a 3 digit number")
            return 0
        else:
            return int(user_input)        
        
    except:
        print("   *** a non numeric integer was informed, please review")
        #if type(user_input) != type(100):
            #print(type(user_input))
            
    
def main_game():
    print("Game start, number generated")
    random_number = generate_number()
    print("Please guess the number generated")
    number_match = False
    
    while number_match == False:
        input_number = 0
        input_number = get_user_intput()
        
        number_match = check_random_number(random_number, input_number)
        
    print("Congratulations, you have found the number! :" + str(random_number))
    

def generate_number():
    return random.choice(range(100,1000))

def convert_to_list(param_number):
  string_list = list(str(param_number))
  #need to use list comprehension to convert from number to number list
  number_list = [int(digit) for digit in string_list]
  return number_list

def check_random_number(param_random, param_input):
            
    matcher_return_string=""    
    random_list = convert_to_list(param_random)
    input_list  = convert_to_list(param_input)
    match_amount = 0
    
    for i in range(0, len(random_list)):
        #print("i " + str(i))
        #print("rand indx: " + str(input_list[i]))
        
        if random_list[i] == input_list[i]:
            matcher_return_string = matcher_return_string + "MATCH "
            match_amount += 1
        elif ((input_list[i] == (random_list[i]-1)) or (input_list[i] == (random_list[i]+1))):
            matcher_return_string = matcher_return_string + "CLOSE "
        else:
            matcher_return_string = matcher_return_string + "NOPE "
           
    print(matcher_return_string)
    
    if match_amount == 3:
        return True
    else:
        return False

main_game()

