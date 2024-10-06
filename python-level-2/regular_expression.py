import re
names = ['ajay', 'lekshmy']
text = "nice to meet you ajay"
# for name in names:
#     if name in text:
#         print(f"find {name} in the text")
#     else:
#         print(f"{name} not find in text")

#We can do the above thing using regular expression
for name in names:
    if re.search(name, text):
      print(f"find {name} in the text")
    else:  
        print(f"{name} not find in text")

match = re.search('ajay', text)
print(match.start())
print(re.split('ajay', text))
print(re.findall('ajay', text))

def multiple_reg_find(patterns, phrase):
   for pa in patterns:
      print("pattern Searching.......")
      print(re.findall(pa, phrase))
      print("\n")

text = "Testing environment test the tested data! and tested and retested! again retestt and tritest 232 it and again tes?"
test_pattern = ["est*"] #return aj followed by anything, Zero or more occurrences['est', 'est', 'est', 'est', 'est', 'estt', 'est', 'es']
test_pattern_1 = ["est+"] #One or more occurrences checking for exact aj ['est', 'est', 'est', 'est', 'est', 'estt', 'est']
test_pattern_2 = ["est?"]#Zero or one occurrences ['est', 'est', 'est', 'est', 'est', 'est', 'est', 'es']
test_pattern_3 = ["est{2}"]#Exactly the specified number of occurrences	['estt']
test_pattern_3 = ["e[st]+"]# e is followed by one ore more s or one or more d ['est', 'est', 'est', 'est', 'et', 'est', 'et', 'estt', 'est', 'es']
test_pattern_4 = ["[^!.?]+"] # ^ used to exclude terms
test_pattern_5 = ['[A-Z]+'] # Return all the uppercase characters
multiple_reg_find(test_pattern, text)
multiple_reg_find(test_pattern_1, text)
multiple_reg_find(test_pattern_2, text)
multiple_reg_find(test_pattern_3, text)
multiple_reg_find(test_pattern_4, text)
multiple_reg_find(test_pattern_5, text)
#
#[r'\d+'] - List all the digits
# [r'\D+'] - List all the non digits
# [r'\s+'] - List all the white spaces
# [r'\S+'] - List all the non white spaces
# [r'\w+'] - List all the alpha numeric
# [r'\w\W+'] - List all the non alpha numeric