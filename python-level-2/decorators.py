#Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class

#
# Decorators can be thought of as functions which modify the "functionality" of
# another function. They help to make your code shorter and more "Pythonic".
# They are also used a lot in Python Web Frameworks, which is why we need to learn
# them.

def func():
    return 1

func()

s = 'Global Variable'

def func():
    print(locals())
print(globals())

print(globals().keys())

globals()['s']
func()

def hello(name='Jose'):
    return 'Hello '+name

hello()



greet = hello

greet
# Call it
greet()



del hello

hello()

greet()

def hello(name='Jose'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()

welcome()

def hello(name='Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

x = hello()
print(x())

def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()