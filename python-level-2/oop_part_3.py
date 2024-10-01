#INHERITANCE
#it is the way to form new classes using older classes already defined
#Use of inheritance : Code reuse
class Animal():
    def __init__(self):
        print("Animal Created")
    def my_category(self):
        print("ANimal")
    def eat(self):
        print("Eating")

class Dog(Animal): #Inheriting ANimal class
    def __init__(self):
        #Animal.__init__(self) 
        print("Dog Created") 
    def eat(self):
        print("Dog Eating")

my_animal = Animal()
my_dog = Dog()
my_dog.my_category()
my_dog.eat()

#SPECIAL METHODS

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"Book name: {self.title}, Author: {self.author}, Pages: {self.pages}"
    def __len__(self):
        return self.pages
    def __del__(self):
        print("Deleted")

my_book = Book("Data Science", "Ajay", 234)
print(my_book) #This will check for the string representation. Can be done by __str
length = len(my_book) #len of class check for __len__ special methods
print(length)
del my_book