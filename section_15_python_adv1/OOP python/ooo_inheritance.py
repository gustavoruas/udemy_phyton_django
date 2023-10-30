#Inheritance
class Animal():
    
    def __init__(self):
        print("Animal Class")
    
    def who_am_I(self):
        print("Animal")
        
    def eat(self):
        print("Eating")
    
    
#calling an inherintance class into another via param
class Cat(Animal):
    def __init__(self):
        #Inside the init constructor, you call a INIT Const for the father class
        Animal.__init__(self)
        print("Cat Class")
        
    #override method
    def who_am_I(self):
        print("Animal Cat")


new_class = Cat()

new_class.eat()
new_class.who_am_I()


