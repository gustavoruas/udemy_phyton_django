print("testing page for python")

# requests the user to inser text
# scan_key = input("Please provide a number")
# print("Number typed in : " + scan_key)

# concatenating strings
print("sentence 1 added" + " to another string")

# variables have no type association
variable_a = "test string"
variable_a = variable_a + "12"

print(variable_a)


# To validate if it is a string
non_string = 450

# second parameter defines what data type to validate
if isinstance(non_string, str):
  print("variable is a string")
else:
    print("Variable is not a string")
    
# this converts to a string
is_string = str(non_string)

if isinstance(is_string, str):
  print("variable is a string")
else:
    print("Variable is not a string")
    
# string indexing like a array
long_string = "sentence with longer approach"

print(long_string[10]) #returns the 10 position character
print(long_string[-1]) #prints the last character

#Slicing strings, is fetching parts of the string
print(long_string[2:10])  # the : indicates  START:END position of characters
print(long_string[:4])  #fetches from first up to 4, but not including 4
print(long_string[::2]) # Double : says that starts from the start until the end of string
#but, the number after is the number of steps it does until the end, if 1 it selects sequentially
print(long_string.upper()) #upper case of string, opposite is string.lower

#splits a string as an array, wehre it splits blank spaces
print("split func: ")
print(long_string.split())

#Splits into an array at a specific character
print(long_string.split("o"))

#String interpolation, or formatting, with replacement with string
template_string = "a string will be inserted here: {}"
print(template_string.format("VALUE INSERTED"));

# more than 1 item
template_string = "a string will be inserted here: {a} and {b}"
print(template_string.format(a = "VALUE INSERTED", b = "Value 2"));
