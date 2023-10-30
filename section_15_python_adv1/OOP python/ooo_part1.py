#Creating a class
class Dog():
    
    #attributes - globally set for static values
    animal_type = "mamal"
    
    #constructor method   
    def __init__(self, breed, name):  # this initializes the objectn with a parameter ( constructor)
                                #self is always needed to represent the method of this class
                                #It holds the attributes
        self.breed = breed
        self.name = name
    
    #methods - self is always needed to represent the method of this class
    def ToString(self):
        return ("animal_type: " + str(self.animal_type) + " " +
                "breed: " + str(self.breed) + " " +
                "name: " + str(self.name) + " ")
        
    def get_animal_type(self):
        return self.animal_type
    
    def set_animal_type(self,p_animal_type):
        self.animal_type = p_animal_type


var2 = Dog("vira lata", "toto")

print(str(type(var2)) + " " + str(var2.animal_type))

#calling methods from classes require a () at the end
print(var2.ToString())


