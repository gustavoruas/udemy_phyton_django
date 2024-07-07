import math, os

loop_list = ["a","b", "c", "d"]


print("len(loop_list):{}".format(len(loop_list)))
      
loop = 0
for iter in loop_list:
    loop = loop + 1
    
    print(loop)
    if loop == 1:
        print("first element of the list")
        
    elif loop == len(loop_list):
        print("last element of the list")
    
        

