#Functions
def return_name(name = "No name"):
    """
    This is a dock string

    When it comes to writing clean, well-documented code, 
    Python developers have a secret weapon at their disposal – docstrings. 
    Docstrings, short for documentation strings, are vital in conveying the 
    purpose and functionality of Python functions, modules, and classes.
    """
    print(f"Your name is {name}")
return_name("Ajay")

def add_num(num1, num2):
    """"
    Find the sum of 2 numbers
    """
    if type(num1) == type(num2) == type(10):
        return f"Sum of numbers is {num1 + num2}"
    else:
        return "Please enter numbers"
first_num = input("Enter the first number ")
second_num = input("Enter the second number ")
print(f"{add_num(first_num, second_num)}")

#Filter
    #Filter function has 2 arguments, a function and a sequence
    #Find even numbers list in given list
sample_list = [1,2,3,4,5,6,7,8,9,10]
def even_func(num):
    return num%2 == 0
even_data = filter(even_func,sample_list)
print(list(even_data))

#Lambda Expression
 #Convert the above function to lambda expression

even_data = filter(lambda num: num%2 == 0, sample_list)
print(f"lambda list {list(even_data)}")

