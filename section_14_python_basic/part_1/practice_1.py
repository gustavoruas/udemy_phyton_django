string_1 ="django"

# print the followings d, o , djan, jan, go, use indexing to reverse string
print(string_1[0])
print(string_1[1])
print(string_1[:4])
print(string_1[1:4])
print(string_1[-2:])
# slicing the string, first : starts at 1 and second : until the end, stepping at every -1
print(string_1[::-1])

# cahnge from nested liste hello, to goodbye
string_2 = [3, 7, [1,4,"hello"]]

string_2[2][2] = "goodbye"
print(string_2)

#with keys and indexing, grab hello from belows
dict1 = {"key1":"hello"}
dict2 = {"key1":{"key2":"hello"}}
dict3 = {"key1":[{"key2":["deep1",["hello"]]}]}

print(dict1["key1"])
print(dict2["key1"]["key2"])
print(dict3["key1"][0]["key2"][1][0])

#using sets to find only unique values from a list
repeat_list = [1,2,3,4,4,4,2,2,1,1,3,3,3,5,3,5]
#create empty set
set_1 = set(repeat_list)
#using FOR
#for element_list in repeat_list:
#    set_1.add(element_list)

print(set_1)

# using format method to displya vars in string
word_1 = "four"
word_2 = "Sammy"
template_sentence_1 = "{a} dog is {b} years old."
print(template_sentence_1.format(a=word_2, b=word_1))
