#handling exceptions need to be in try catch blocks

import traceback

try:
    
    f= open("/text_file.txt", "r")  # to read only
    f.write("inputing text into file")
    
#by handling exception, it does not break the code flow
#except:    #catches anything
except IOError as e:   #fetches only a specific error, as e adds to a variable so it can be printed
    print("  **ERROR:File cannot be read or written \n" + str(e))
    
    #prints stacktrace
    traceback.print_exc() 
    
else:
    print("file saved")
    f.close()
    
finally:  #always run if caught or not
    print("file process finished.")
    
    
print("continuing vcode")
    
