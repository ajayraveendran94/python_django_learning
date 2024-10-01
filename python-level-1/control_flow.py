#No type conversion in python means 1 == "1" gives false

#OR AND
print((1<3) or (4>8))
print((1<3) and (4>=8))
if 3<2:
    print("Hello!")
    print("Hi")
else:
    print("Okay")

#IF
#Find the entered number is odd even or zero
val = input("Enter a number: ")
#try - except is used to handle the error. Here we handle the value error means any error from input value
try:
    number = int(val)
    if number == 0:
        print("Entered number is zero")
    elif number%2 == 0: #elif id same as else if
        print(f"{val} is an even number")
    else:
        print(f"{val} is a odd number")
except ValueError:
    print("You are not entered a number")

#For loop
#Print the even numbers in an array
number_array = [1,45,78,3,54,7,88,5,34,6]
odd_array = []
even_array = []
for item in number_array:
    if item%2 == 0:
        even_array.append(item)
    else:
        odd_array.append(item)
print(f"Odd array {odd_array}")
print(f"Even array {even_array}")

temp_even = [x for x in number_array if x%2 == 0]
temp_odd = [x for x in number_array if x%2 != 0]
print(temp_even)
print(temp_odd)

#Loop in dictionary
dictionary = {"Ajay": 3, "Lekshmy": 7, "Jay": 8}
for record in dictionary:
    print(record) #No need to print in order
    print(dictionary[record]) 


#Tuple unpacking
tuple_array = [(1,2,10), (3,4,9), (5,6,8)]
for dat1,dat2,dat3 in tuple_array:
    print(dat2)
    print(dat1)
    print(dat3)

#While loop
i = 1
while(i < 5):
    print(f"Number is {i}")
    i = i + 1

#Range functions
range(10) #range the first 10 digits from 0
print(list(range(0,10,2))) #Display the even numbers in 0-10 in lists

#Advantage of Using range is it willnot save the entire number and only generate if we want and save memmory

for data in range(20):
    print(data * 2)

#List Comprehension
#Task print the square of 1 to 4
value = [1,2,3,4]
data_set = []
for num in value: #OR for num in range(1,5):
    data_set.append(num**2)
print(f"Data Set {data_set}")
#OR
data_set_1 = [x**2 for x in range(1,5)]
print(data_set_1)