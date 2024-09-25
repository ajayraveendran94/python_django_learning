s = "django"
#Print d
print(s[0])
#Print o
print(s[-1])
#Print djan
print(s[:4])
#Print jan
print(s[1:4])
#Print go
print(s[-2:])
#Print ognajd  
print(s[::-1])

#change Hello with good bye in following list
l = [3,7,[1,4,"Hello"]]
l[2][2] = "good bye"
print(l)

#Grab hello from following dictionaries
d1 = {'simple_key': 'hello'}
d2 = {'k1':{'k2': 'hello'}}
d3 = {'k1':[{'nest_key':[ 'this is deep', ['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(my_list))

age = 4
name = "sammy"
print(f"hello my dog's name is {name} and he is {age} years old")