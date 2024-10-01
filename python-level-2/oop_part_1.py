#In python everything is an object
my_list = [1,2,3]
my_string = "Ajay"
my_num = 234
print(type(my_list)) # o/p <class 'list'>
print(type(my_num)) # o/p <class 'int'>

#A Class is like an object constructor, or a "blueprint" for creating objects.
# From classes we can construct the instances of that class
#Instance is aa object created from a particular class
# Eg: the previously created my_list is an instance of object list

class Sample():
    pass

print(Sample()) #output <__main__.Sample object at 0x100718890>