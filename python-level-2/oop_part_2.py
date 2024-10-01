
#Attributors are the characteristics of an object
#Methods are operation that perform on the object
#Eg: for class Dog, attribute is dog's breed  or dog's pet name etc
    #Methods eg bark will return the sound from dog

class Dog():

    # Class Object Attribute
    species = 'mammal'
#All classes have a function called __init__(), which is always executed when the class is being initiated.
    def __init__(self,breed,name): 
        self.breed = breed
        self.name = name

sam = Dog('Lab','Sam') 
#sam = Dog(breed = 'Lab', name = 'Sam') 

print(sam.name)
print(sam.species)

class Employee():
    company = "Chorfidy"
    def __init__(self,name, designation):
        self.name = name
        self.designation = designation
ajay = Employee("Ajay", "Senior Engineer")
samily = Employee("Samily", "QA Engineer")

print(ajay.name, ajay.company, ajay.designation)
print(samily.name, samily.company, samily.designation)

#methods are functions that defined inside the body of the class
#methods are essentials for the encapsulation concept of oop

class Circle():
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
#The __str__() function controls what should be returned when the class object is represented as a string.
    def __str__(self):
        return f"Circle radius is {self.radius}"
    def area(self): #method
        return self.radius*self.radius*Circle.pi
    def change_radius(self, new_radius):
        self.radius = new_radius
    
#print(Circle(3).area())
my_circle = Circle(2)
my_circle.change_radius(342)
print(my_circle.area())
print(my_circle) #This will represent the class object as string and then __str__() function will be triggered

