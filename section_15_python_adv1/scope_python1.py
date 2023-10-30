#Local - names assigned in any waay withib a function def or lambda, and not declared globaly
#EFL - Name in the local scope, and all enclosing functions from innter to outer
#Global - Names assigned at teh top level of module file, delcared globally
#Builtin - names preassigned and built in in python (print, range, enumerate)

#Global example
var1 = 20

def func1():
    var1 = 55   #This is a local scope of the function
    return var1

#refers to the global var
print(var1)
#returns the local variable
print(func1())
func1()
print(var1)  #This only returns the global function variable, not the local from the variable

#To redifine Global scope var, with local from function, reasing
var1 = func1()
print(var1)

#local level
lambda x: x**2

#Enclosing functions local variables, inner to outer looking for variable
name = "test name"

def greet():
    #name = "test1"
    def hello():
        print("displaying var: " + name)
        
    hello()

greet()


#to change a global scope variable , inside a local function

var2 = 200

def change_global():
    #global must be placed first, referencing to the same variable name
    global var2
    var2 = 1000
    
print("Before calling global change func: " + str(var2))
change_global()
print("After calling global change func: " + str(var2))
    

