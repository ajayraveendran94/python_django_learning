my_string = 'adventurous'
print(my_string[-1]) #print the last letter of string

#slicing
print(my_string[4:]) #Skip the first 4 letters and print others
print(my_string[:4]) #Catch the first 4 letters (catch the word upto 3 position)
print(my_string[2:6]) #Catch the letters from 2 to 5 position
print(my_string[::-1]) #Reverse string using indexing

print(my_string.upper()) #Convert to uppercase, lower() used to convert to lowercase
print(my_string.capitalize()) #Convert the first letter to Uppercase
print(my_string.casefold()) #same as lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
print(my_string.ljust(16, "c")) #Fill the remaining slot with specified character, here we expect a word of length 16 with blanck spaces with letter c
print(my_string.center(20,"e")) #Almost same as ljust but the remaining characters add in the 2 sides of word
print(len(my_string)) #Length of string
new_string = 'Ajay Raveendran'
print(new_string.split('a')) #Split the string into array by default with spaces
print(('.....').join(new_string.split('a'))) #join used to combine the array with given character

#string concatnation
formattted_string_1 = "My Name is %s" % (new_string) #Using %s
formattted_string_2 = "My Name is {}".format(new_string) #Using format function
formattted_string_2 = "{a} My Name is {b}".format(a= 'Hi', b=new_string) #Using format function
formattted_string_3 = f"My Name is {new_string}" #Using f
print(formattted_string_1)
print(formattted_string_2)
print(formattted_string_3)