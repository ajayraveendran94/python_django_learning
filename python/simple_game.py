#Guess a 3 digit number
#Close - Gussed a correct number but in different position
#Match - Gussed a correct number but in correct position
#Nope - You haven't gussed any of the number correctly

import random
random_number = str(random.randint(100,999))
def get_the_number():
    guessed_number = input("Enter your guess: ")
    check(guessed_number)
def check(my_num):
    print("Here is the result of your guess: ")
    if my_num == "000":
        print(f"The number is {random_number}")
    if my_num == random_number:
        print(f"Success the number is {random_number}")
    else:
        count = []
        for num in my_num:
            if num in random_number:
                count.append("Close")
        for x in range(len(my_num)):
            if my_num[x] == random_number[x]:
                count.append("Match")
        if count == []:
            print("Nope")
            get_the_number()
        elif "Match" in count:
            print("Match")
            get_the_number()
        elif "Close" in count:
            print("Close")
            get_the_number()

get_the_number()


#Step 1: Generate a random number r
# Step2:Enter Number b
#Step 3: if any number in a is in b count = 1
# Step4: if first number of a == first number of b count = count + 1 
# Step 5: elif second number of a == second number of b count = count + 1
# Step 6: elif third number of a == third number of b count = count + 1
# Step 7: else count = 0 
# Step 8: if count == 0 print Nope go to step 2
# Step 9: elif count < 4 print Close go to step 3
# Step 9: elif count == 4 print Done Correct number##