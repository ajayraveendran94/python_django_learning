#Lists
    #Lists are python form of arrays
    # Behave very similarly to JS array#
my_list = [1,2,3,'a','b',True,[4,5,6]] #sample
print(my_list)
print(len(my_list))
print(len(my_list[-1]))
#Slicing will work same as that we did for string
print(my_list[:5])
print(my_list[4:6])
print(my_list[5:])

new_list = [7,8,9]
my_list.append(new_list) #Add a new list/element after the last element of original list
my_list.extend(new_list) #Extend another list with original list
print(my_list)
pop_list = my_list.pop() #remove the last element from list
print(my_list)
pop_list_ = my_list.pop(5) #remove the given index element from list
print(my_list)

number_list = [76,89,87.2,897,23,356]
number_list.reverse()
print(number_list)
number_list.sort()
print(number_list)

#nested list
format_list = [1,5,7,["a","b","c","f"]]
print(format_list[3][3]) #we can access the nested list element by this

#list comprehension
    #List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
input_list = [[1,2,3],[4,5,6],[7,8,9]]
output_list = [x[0] for x in input_list]
print(output_list)

datalist = []
for n in input_list:
 datalist.extend(n) 
print(datalist)
#Print a new array all the words which has letter a from array
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "n" in x:
    newlist.append(x)

print(newlist)
