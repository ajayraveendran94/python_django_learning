#Given list of integers return true if the sequesnce of numbers 1,2,3 appears
#My Answer
def arrray_check(nums):
    # return all(i in nums for i in given_list)
    for i in range(len(nums)):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            print("Yes")
arrray_check([1,3,4,1,2,3,67])

#Answer
def arrayCheck(num):
    for i in range(len(num) - 2):
        if num[i] == 1 and num[i+1] == 2 and num[i+2] == 3:
            return True
    return False
print(arrayCheck([1,3,4,1,2,3,67]))


#Given a string and print a string with intermediate letters starting with first letter
# EG: input "JLOPIUN" output "JOIN" 

#My Answer
def print_sub_string(strin):
    print(("").join(list(strin)[::2]))

print_sub_string("MFYFDFEFASR")

#Answer
def stringBits(str):
    print(str[::2])

print_sub_string("MFYFDFEFASR")

#Given 2 strings, return true if either of the string appears very last of other

#My Answer
def check_string(string_1, string_2):
    if len(string_1) > len(string_2):
        if list(string_1.lower())[-len(string_2)::] == list(string_2.lower()):
            return True
        else:
            return False
    else:
        if list(string_2.lower())[-len(string_1)::] == list(string_1.lower()):
            return True
        else:
            return False
print(check_string("HiAbc", "abc"))
print(check_string("ABC", "abcXABc"))

#Answer
def end_other(a,b):
    a= a.lower()
    b = b.lower()
    #return(b.endswith(a) or a.endswith(b))
    #OR
    return a[-(len(b)):] == b or b[-(len(a)):] == a
print(end_other("HiAbc", "abc"))
print(end_other("ABC", "abcXABd"))


#Double the characters in a string

#My Answer
def double_string(string_name):
    double_string = []
    for x in range(len(list(string_name))):
        double_string.append(string_name[x])
        double_string.append(string_name[x])
    return ("").join(double_string)

print(double_string("AbCdeF"))

#Answer
def doubleChar(my_string):
    new_string = ""
    for char in my_string:
        new_string += char * 2
    return new_string
print(doubleChar("AbCdeF"))

#Find sum of 3 numbers, if any number is in range 13-19 except 15 and 16 shoul be considered as 0

#My Answer
def fix_teen(num):
     if num in range(13,20) and num != 15 and num != 16:
         return num
     else:
         return 0
def teen_sum(a,b,c):
    sum = a+b+c
    value = [a,b,c]
    difference = 0
    for x in value:
        difference = difference + fix_teen(x)
    return (sum - difference)

print(teen_sum(1,2,3)) 
print(teen_sum(2,13,1)) 
print(teen_sum(2,1,14)) 

#Answer
def no_teen_sum(a,b,c):
    return fix_teen_val(a) + fix_teen_val(b) + fix_teen_val(c)
def fix_teen_val(n):
    if n in range(13,20) and n != 15 and n != 16:
        return 0
    else:
        return n

print(no_teen_sum(1,2,3)) 
print(no_teen_sum(2,13,1)) 
print(no_teen_sum(2,1,14)) 

#Return the number of even integers in array

#My Answer

def count_evens(num):
   even_list =  [x for x in num if x%2 == 0]
   print(f"Even numbers in array is {len(even_list)}")
count_evens([2,1,2,3,4])
count_evens([2,2,0])
count_evens([1,3,5])

#Answer
def even_count(list_data):
    count = 0
    for n in list_data:
        if n % 2 == 0:
            count+=1
    return count
print(even_count([2,1,2,3,4]))
print(even_count([2,2,0]))
print(even_count([1,3,5]))

#LEARNINGS
#1 No need to convert string into array and join back again. for loop will work with in the strings
