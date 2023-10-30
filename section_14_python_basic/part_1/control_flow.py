#same value and type validation is reprenseted by ==
if 1 == "1":
    print("true")
elif 1==1 and 1!="1":  #and / or
    print("true")   
else:
    print("false")


# Iterate 5 times
for i in range(5):
    print("Iteration:", i)

#simple for within list
list_1 = ["aa","bb","cc","dd"]

for element in list_1:
    print(element)
    
# Looping a dictionary
dict_1 =  {"key1":"aa","key2":"bb"}

for element in dict_1:
    # to print the keys, you direct the dictionary variable[tempvar]
    print(element + " " + dict_1[element])

# looping a tuple
tuple_1 = [("aa","bb","cc"),(1,2,3),("c","d","e")]

for element in tuple_1:
    print(element)
    
# tuple unpacking, each tupN indicates the position of each element in a tuple
# they must have thename Number of elements per tuple
for tup1, tup2, tup3 in tuple_1:
    print(tup1)
    print(tup2)
    print(tup3)
    
# while
i = 5

while i < 10:
  print("list is being printed") 
  i = i + 1   

#range command returns seq numbers from start to finish
# range(start, finish, incrementBY)
list_2 = list(range(22,55,5))

print(list_2)

#list comprehension - list_4 gets every element of list_3 multBy 2
list_3 = [1,2,3,4]

list_4 = [element**2 for element in list_3]
print(list_4)
    