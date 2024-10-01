#Booleans
value = True
negative = False
print(value)
print(negative)

#Tuples
#Tuples are immutable sequences
tuples_1 = (0,1,4,3)
tuples_2 = ("a", "j", "a", True, 898)

#Tuples are same as lists but the difference is it is immutable (We cannot edit it)
#tuples_1[4] = 90

print(tuples_1[0])
print(tuples_2)
#slicing indexing are same as lists for tuples

#Sets
# Sets are unordered collections of unique elements#
x = set()
x.add(1)
x.add(2)
x.add("data")
x.add("data") #if we add the same data multiple times it will not add
x.add("data")
print(x)
random_data = [1,2,3,43,21,2,1,2,3,1,23,1,23,12,2,1,2,3]
y = set(random_data) #Will convert the list into sets
print(y)