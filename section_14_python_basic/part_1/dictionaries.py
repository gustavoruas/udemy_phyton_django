# creating a dictionary, or object mapped by a Key an valiue. {} defines a Dictionary, and[] is a list
# var = {"key":"value"}
dictionary_var1 = {"key_1":"value_1","key_2":"value_2","key_3":123, "key_4":["aa","bb","cc"]}

# nested Dictionaries
dictionary_var2 ={"nest_1":{"nest_2":["aa","bb","cc"]}}

print(dictionary_var1)

#selecting the value by key, shows value
print(dictionary_var1["key_4"])

#Fetching nested dictionaries
#Start from the inner element, to the outside
print(dictionary_var2 ["nest_1"]["nest_2"][0])

