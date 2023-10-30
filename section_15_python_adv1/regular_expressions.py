import re

patterns = ["textA", "textB"]
text = "this contain textB as an example contained"

#iterating in patterns to find a match
for pattern in patterns:
    print("Searching for: " + pattern)
    
    if re.search(pattern,text):
        print("Found")
    else:
        print("Not Found")
        
#returning the position of
find_position = re.search("textB",text)
print(str(type(find_position)) + " " + str(find_position.start()))

#searches for term many times, returns a list of all matches  re.findall
print(str(len(re.findall("on", text))) + "  " + str(re.findall("on", text)))

#reg expression
def multi_re_find(patterns, phrase):
    
    for pat in pattern:
        print("Searching fo pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")
        
new_text1 = "sddsddd ... sdddd....sddd...ssssddd...sssd"

#pattern = ["sd*"] #0 or more times
#pattern = ["sd?"] #0 or more than once d
#pattern = ["sd{3}"] #followed by 3 d.
pattern = ["s[sd]+"] #an s followed by one more s or d

multi_re_find(pattern,new_text1)

