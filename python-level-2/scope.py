#LEGB Rule and Order
    #Local : Names assigned within the function (def / lambda) & not declared global in that function
    # Enclosing Functions Local : Name in the local scope of any and all enclosing functions from inner to outer
    # Global : Names assigned at the top level
    # Built in : Nmes pre assigned in the built in module : Open, range, syntax error

x = 100
def number_func(x):
    x = 120
    print("Local X", x)
number_func(x)
print("Global X", x)

value_set = lambda x: x/2
print(value_set(x))


#Global

def global_number_change():
    global x
    x = 2000

print("Before changing the global",x)
global_number_change()
print("After changing the global",x)