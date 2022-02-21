# -*- coding: utf-8 -*-
"""
Exercise #050
Using the song "10 green bottles" display the lines "there are [num] green
bottles hanging on the wall, [num] green bottles on the wall,and if 1 green
bottle should accidentally fall". Then ask question "How many green bottles
will be hanging on the wall?" if the user answers correctly, display the 
message "there will be [num] green bottles hanging on the wall". If they 
answer incorrectly, display the message "No, try again" until they get it right
When the number of green bottles gets down to 0, display the message "There are
no more green bottles hanging on the wall"
ps. I added color by my self for more estetic output but code is not nice 
I'm sure in future I will find something more 'pythonic'
"""

# num = 10
# while num > 0:
#     print("There are", '\x1b[6;30;42m',num,'\x1b[0m' ,"green bottles\nhanging on the wall")
#     print('\x1b[6;30;42m',num,'\x1b[0m', "green bottles on the wall, and \nif 1 green bottle should accidentally fall\n")
#     usr_answ=int(input("How many green bottles will be hanging on the wall?\n"))
#     num = num - 1
#     if usr_answ == num:
#         print("There will be", '\x1b[6;30;42m',num,'\x1b[0m' ,"green bottles\nhanging on the wall")
#     else:
#         while usr_answ != num:
#             usr_answ=int(input("No, try again\n"))
    
# print('\x1b[6;30;42m'+"There are no more green bottles hanging on the wall"+'\x1b[0m' )



# =============================================================================
# RANDOM 
# =============================================================================

# import random 
# num = random.random()
# print(num)
# #selects random floating-point between 0 - 1
# num2 = random.randint(5, 45)
# print(num2)
# # random.randit selects random number between given 2 numbers a, b. b insclusive
# num3 = random.randrange(0,100,5)
# print(num3)
# #random.randrange selects a random number between the numbers (start, stop, step)
# colour = random.choice(["red","black","green"])
# print(colour)
# #picks random value from the given options 

"""
Exercise 052
Display a random integer between 1 and 100 inclusive
"""
# import random 
# num = random.randint(1, 100)
# print(num)

"""
Exercise 053
Display random fruit from list of five fruits
"""
# import random 
# fruit = random.choice(["apple", "banana", "peach", "ananas", "mango"])
# print(fruit)

"""
Execise 054
Randomly choosee either heads of tails ("h" or "t"). 
Ask the user to make their choice. If their choice is 
the same as the randomly selected value, display the 
message "You win", otherwise display "Bad luck".
At the end, tell the user if the computer selected 
heads or tails
"""
# import random
# random_value=random.choice(["h","t"])
# user_choice=input("Heads = h or Tails = t ??? type your answer:\n")
# if user_choice == random_value:
#     print("You win")
# else:
#     print("Bad luck!\n\n Computer selected",random_value)

"""
Excercise 055
Randomly choose a number between 1 and 5. 
Ask the user to pick a  number. If they guess correctly, 
display the message “Well done”,  otherwise tell them if
they are too high or too low and ask them to pick a  second number.
If they guess correctly on their second guess, display "Correct",
Otherwise display "You lose".
"""
# import random
# random_value = random.randint(1,5) 
# usr_choice = int(input("Enter number between 1 - 5:\n"))
# if usr_choice == random_value:
#     print("Well done")
# elif usr_choice < random_value:
#     print("Number is too low\n")
#     usr_choice = int(input("Try another number\n"))
#     if usr_choice == random_value:
#         print("Correct")
#     else:
#         print("You loose")
# elif usr_choice > random_value:
#     print("Number is too High\n")
#     usr_choice = int(input("Try another number\n"))
#     if usr_choice == random_value:
#         print("Correct")
#     else:
#         print("You loose")
        
"""
Exercise 056  
Randomly pick a whole number between 1  and 10. 
Ask the user to enter a number and  keep entering 
numbers until they enter the number that was randomly picked.
"""
# # Option 1
# import random 
# rand_number = random.randint(1, 10)
# user_answer = int(input("Enter the number between 1 - 10:\n"))
# if user_answer == rand_number:
#     print("Correct!")
# while user_answer != rand_number:
#     user_answer = int(input("No luck this time!\nTry one more time to guess the number between: 1 - 10:\n"))
    
# # Option 2 - with bool 
# import random 
# rand_number = random.randint(1,10)
# correct = False
# while correct == False: 
#     user_answer = int(input("Enter a number:\n"))
#     if user_answer == rand_number:
#         correct = True

"""
Exercise 057  
Update  program 056  so that it  tells the  user 
if they  are too high  or too low  before they 
pick again
"""
# # Option 2 - with bool 
# import random 
# rand_number = random.randint(1,10)
# correct = False
# while correct == False: 
#     user_answer = int(input("Enter a number:\n"))
#     if user_answer == rand_number:
#         correct = True
#         print("Correct!")
#     elif user_answer < rand_number:
#         print("Too low!")
#     else:
#         print("Too high!")
        
"""
Exercise 058
Make a maths quiz that asks five questions by randomly  
generating two whole numbers to make the question  
(e.g. [num1] + [num2]). Ask the user to enter the  answer. 
If they get it right add a point to their score. At  the end of the quiz, 
tell them how many they got correct  out of five.  
"""
# SOLUTION 1 - while loop 
# import random 
# counter = 0
# user_points = 0
# while counter < 5 :
#     num1=random.randint(1,1000)
#     num2=random.randint(1,2000)
#     print(num1,"+",num2,"= ")
#     user_answer=int(input())
#     if user_answer == num1+num2:
#         print("Correct!")
#         user_points = user_points + 1
#     else:
#         print("Try one more time")
#     counter = counter + 1
# print("You gave", user_points,
#       "correct answers for 5 questions!")


# SOLUTION 2 for loop 
# import random 
# user_points = 0
# for i in range(1, 6):
#     num1=random.randint(1,10)
#     num2=random.randint(1,20)
#     print(num1,"+",num2,"= ")
#     user_answer=int(input())
#     if user_answer == num1+num2:
#         print("Correct!")
#         user_points = user_points + 1
#     else:
#         print("Try one more time")
# print("You gave", user_points,
#       "correct answers for 5 questions!")

# SOLUTION 3
# import random 
# user_points = 0
# for i in range(1, 6):
#     num1=random.randint(1,10)
#     num2=random.randint(1,20)
#     correct = num1 + num2
#     print(num1,"+",num2,"= ")
#     user_answer=int(input())
#     if user_answer==correct:
#         user_points=user_points+1
# print("You gave", user_points,
#       "correct answers for 5 questions!")


"""
Exercise 059  
Display five colours and ask the user to pick one. 
If they  pick the same as the program has chosen, 
say “Well  done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. 
Ask  them to guess again; if they have still not got it right,  
keep giving them the same clue and ask the user to 
enter a colour until they guess it correctly 
"""
# import random 
# print("Pick one of the following colours:\nYELLOW\nGREEN\nBLUE\nBLACK\nWHITE\n")
# colour = random.choice(['YELLOW', 'GREEN', 'BLUE', 'BLACK', 'WHITE'])
# answer = input("Guess color:\n")
# answer=answer.upper()
# while answer != colour:
#     joke = random.choice(['YELLOW', 'GREEN', 'BLUE', 'BLACK', 'WHITE'])
#     print('You are probably feeling that it should be', joke ,'right now!')
#     answer = input("Guess color:\n")
#     answer=answer.upper()
# print("Well done!")
"""
Zabawa z funcja random
"""
# import random 
# for i in range(1,220):
#     imieOna=random.choice(['Emi', 'Emilia', 'Emcia', 'Emka', 'Tomilia'])
#     imieOn=random.choice(['Tomi', 'Tomasz', 'Tomcio', 'Tomeczek', 'Emiliasz'])
#     relacja=random.choice(['Kocha', 'Chce zerznac', 'Teskni', 'Pragnie', 'Szanuje'])
#     a=print(imieOna, relacja, imieOn)
#     b=print(imieOn, relacja, imieOna)
#     wydruk=random.choice([a,b])
# print(wydruk)

# =============================================================================
# TURTLE FUNCTION - I will skip this section. I don't see the use for now
# =============================================================================

# import turtle 
# for i in range(0,4):
#     turtle.forward(100)
#     turtle.right(90)
# turtle.exitonclick()

# =============================================================================
# TUPLES, LISTS AND DICTIONARIES
# =============================================================================

"""
Exercise 069  
Create a tuple containing the names of five countries and display
the whole tuple. Ask  the user to enter one of the countries that 
have been shown to them and then display  the index number 
(i.e. position in the list) of that item in the tuple. 
"""
# #option 1
# countries = ("Norway", "Poland", "Great Britain", "New Zeland", "Scotland")
# print(countries)
# user_action=input("Enter the name of one of the countries from the list:\n")
# print(countries.index(user_action))

# #option 2
# countries = ("Norway", "Poland", "Great Britain", "New Zeland", "Scotland")
# print(countries)
# oneMoreTime = "y"
# while oneMoreTime == "y":
#     user_action=input("Enter the name of one of the countries from the list:\n")
#     print(countries.index(user_action))
#     oneMoreTime = input("Will you continue?: y/n\n")
#     oneMoreTime = oneMoreTime.lower()
    

"""
Exercise 070  
Add to program 069 to ask the  user to enter a 
number and  display the country in that  position. 
"""
# #option 1
# countries = ("Norway", "Poland", "Great Britain", "New Zeland", "Scotland")
# print(countries)
# user_action=input("Enter the name of one of the countries from the list:\n")
# print(countries.index(user_action))
# user_index=int(input("Please enter the number from 0 - 4 to see index:\n"))
# print(countries[user_index])

# # option 2 
# countries = ("Norway", "Poland", "Great Britain", "New Zeland", "Scotland")
# print(countries)
# oneMoreTime = "y"
# while oneMoreTime == "y":
#     user_action=input("Enter the name of one of the countries from the list:\n")
#     print(countries.index(user_action))
#     user_index=int(input("Enter the number:\n"))
#     while user_index > (len(countries)-1):
#         print("Enter the number in range 0 -",(len(countries)-1))
#         user_index=int(input())
#     if user_index < len(countries):
#         print(countries[user_index])
#     oneMoreTime = input("Do you want to continue?: y/n\n")
#     oneMoreTime = oneMoreTime.lower()
# print("Thank you for your time :)")
    
"""
Exercise 071
Create a list of two sports. Ask the  user what their favourite sport 
is and  add this to the end of the list. Sort the list and display it
"""
#option 1
# sports = ["Football", "MMA"]
# userSport=input("Enter your favourite sport:\n")
# sports.append(userSport)
# print(sorted(sports)
 
#option 2
# sports = ["Football", "MMA"]
# sports.append(input("Enter your favourite sport:\n"))
# sports.sort()
# print(sports)

#option 3
# sports = ["Football", "MMA"]
# sports.append(input("Enter your favourite sport:\n"))
# print(sorted(sports))

"""
Source: Lacey, Nichola. Python by Example (p. 61). Cambridge University Press. Kindle Edition. 

Exercise 072  
Create a list of six school subjects. Ask the user which of these  
subjects they don’t like. Delete the subject they have chosen from the  
list before you display the list again. 

Note to myself:
this is something which I need to figure out - how to delete elements from subjects_list
which are included in dislike list. Compare the lists? and than remove redundant elements?
well this is the problem for tomorrow :) :) or evening :) """
    
# option 1 - without modifying original list - for loop 
# subjects_list = ['math','chemistry','geography','computer science','latin','english']
# for i in subjects_list:
#     print(i,"\n")
    
# dislike=[]

# for i in subjects_list:    
#     dislike.append(input('Which subjects from the list you don''t like?:\n'))
#     answer=input("If this is all enter: exit\n")
#     if answer == 'exit':
#         break
      
# liked_subjects = [i for i in subjects_list]
# for i in subjects_list:
#     if i in dislike:
#         liked_subjects.remove(i)
# for i in liked_subjects:
#     print("Seems that you like: ",i,"\n")
    
# print("subjects list =", subjects_list)    
# print("disliked subjects list =", dislike)
# print("liked subjects list =", liked_subjects)

# solution from stack overflow
# C = ['A','B', 'A','A','B','B','B','X','B']
# D = ['A','B','B','Y']

# res = [ i for i in C ]

# for i in D:
#   if i in C:
#     res.remove(i)

# print(res)

# start = 110 
# lista1 = []
# lista2 = []
# while start > 10: 
#     minus = start - 10
#     lista1.append(minus)
#     start -=10
# print(lista)

"""073  Ask the user to  enter four of their  favourite foods  and store 
them in  a dictionary so  that they are  indexed with  numbers starting  
from 1. Display  the dictionary in  full, showing the  index number  and 
the item. Ask  them which they  want to get rid of  and remove it  from 
the list. Sort  the remaining  data and display.
"""

# food_dict={}
# for i in range(1, 5):
#      user_foods = input("Enter 4 of you favourite foods:\n")
#      food_dict[i] = user_foods #  iterator 'i' will generate key and value from user input will be assigned
# print(food_dict)
# removal = int(input("which food you want to remove?:\n"))
# food_dict.pop(removal)
# print(sorted(food_dict))
# print(food_dict)

"""
075  Create a list of four three-digit  numbers.
Display the list to the  user, showing each item 
from  the list on a separate line. Ask  the user to
enter a three-digit  number. If the number they  have 
typed in matches one in  the list, display the position 
of  that number in the list,  otherwise display the message 
"""
# list_ = ['123', '456', '789']
# for i in list_:
#     print(i)
# user_input = input('Enter 3 digit number:\n')
# if user_input in list_:
#     print(user_input, "element is in the list")
#     print(list_.index(user_input))
# else: 
#     print("There is no such element in the list")

               
"""
076  Ask the user to enter the names of three people 
they want to  invite to a party and store them in a list.
 After they have entered  all three names, ask them if 
 they want to add another. If they do,  allow them to add
 more names until they answer “no”. When  they answer “no”, 
 display how many people they have invited to the party.
"""
#for loop 
# guests = []
# party_size = int(input('How many people you want to invite?:\n'))
# for i in range(party_size):
#     guests.append(input('Enter guest name:\n'))
# print('your guest list:', guests)

#while loop
# guests = []
# for i in range(3):
#     guests.append(input('Enter names of 3 people you want to invite:\n'))
# add_more_guest = input('Do you want to invite more? (yes/no):\n')
# while add_more_guest == 'yes':
#     guests.append(input('Enter the name:\n'))                    
#     add_more_guest = input('Do you want to invite more? (yes/no):\n')
# print(len(guests))
# for name in guests:
#     print('Name:', guests.index(name), name)


"""
077  
Change program 076 so that once the user has
 completed their list of names, display the  full
 list and ask them to type in one of the names on
 the list. Display the position of that  name in
 the list. Ask the user if they still want that
 person to come to the party. If they answer no 
delete entry from the list and display the list again.
"""
# guests = []
# for i in range(3):
#     guests.append(input('Enter names of 3 people you want to invite:\n'))
# add_more_guest = input('Do you want to invite more? (yes/no):\n')
# while add_more_guest == 'yes':
#     guests.append(input('Enter the name:\n'))                    
#     add_more_guest = input('Do you want to invite more? (yes/no):\n')
# print(len(guests))
# for name in guests:
#     print('Name:', name)
# after_thought = input('Enter one of the names:\n')
# print('this person has number', guests.index(after_thought), 'on the list')
# final_decision = input('nb on list. Do you still want to invite? (y/n)?\n')
# if final_decision == 'n':
#     guests.remove(after_thought)
# print(guests)

"""
078  
Create a list containing the titles of  four TV 
programmes and display  them on separate lines. 
Ask the  user to enter another show and a  position 
they want it inserted into  the list. Display the 
list again,  showing all five TV programmes in 
their positions"""

# tv_list = ['MTV', 'Viva', 'MTV2', 'RTL7']
# for show in tv_list:
#     print(show)
# add_show = input('Enter the name of the tv show you like:\n')
# insert_at = int(input('On which position you would like to add this record?:\n'))
# tv_list.insert(insert_at, add_show)
# print(tv_list)  


"""
079  
Create an empty list called “nums”.  
Ask the user to enter numbers.  After 
each number is entered, add  it to the 
end of the nums list and  display the list. 
Once they have  entered three numbers, ask 
them if  they still want the last number they  
entered saved. If they say “no”,  remove the 
last item from the list. Display the list of the numbers
"""
# nums = []
# for i in range(3):
#     nums.append(int(input('Enter a number:\n')))
# question = input('Do you still want last number to be added to list? (y/n)?:\n')
# if question == 'n':
#     nums.pop(2)
# print(nums)

# nums = []
# for i in range(3):
#     num = int(input('Enter a number:\n'))
#     nums.append(num)
# question = input('Do you still want last number to be added to list? (y/n)?:\n')
# if question == 'n':
#     nums.remove(num)
# print(nums)

# nums = []
# counter = 0 
# while counter < 3:
#     num = int(input('Enter a number:\n'))
#     nums.append(num)   
#     print(nums)
#     counter += 1
# question = input('Do you still want last number to be added to list? (y/n)?:\n')
# if question == 'n':
#     nums.remove(num)
# print(nums)

"""
080  
Ask the user to enter their  
first name and then display  
the length of their first name.  
Then ask for their surname  and 
display the length of  their surname. 
Join their first  name and surname 
together  with a space between and  
display the result. Finally,  display 
the length of their full name (including the space)
"""
# name = input('Enter your name:\n')
# print(len(name))
# surname = input('Enter your surname\n')
# print(len(surname))
# full_name = name + ' ' + surname
# print(full_name)
# print(len(full_name))

"""
081  
Ask the user to type in their favourite school subject.  
Display it with “-” after each letter
"""
# fav_subject = input('Enter your favourite subject:\n')
# for i in fav_subject:
#     print(i,end='-')

"""
082  
Show the user a line of text from your favourite 
poem  and ask for a starting and ending point. 
Display the  characters between those two points. 
"""
# camus = "one must imaginge sisiphus happy"
# print(camus) 
# start_ = int(input('Enter starting point:\n'))
# stop_ = int(input('Enter end point:\n'))
# print(camus[start_ : stop_])

"""
083  
Ask the user to type in a word in upper case. 
If they  type it in lower case, ask them to try again. 
Keep  repeating this until they type in a message all in  uppercase. 
""" 
# usr_ipt = input('Type any word in upper case:\n')
# while usr_ipt.islower():
#     usr_ipt = input('Type in upper case:\n')
# print('Thank you')


# =============================================================================
# NUMERIC ARRAYS 
# =============================================================================

##examples 
# from array import *
# nums = array ('i', [45, 56, 76, 89])
# print(nums)
# for x in nums:
#     print(x)
# new_value = int(input("Enter number: "))
# nums.append(new_value)
# nums.reverse()
# print(nums)
# print(sorted(nums))
# print('applying pop function')
# nums.pop()
# print(nums)
# #adding elements
# new_array = array('i', []) #  creation of empty integer array 
# range_stop = int(input("How many elements you're wishing to add?: "))
# for i in range(0, range_stop):
#     user_input = int(input('Enter a number: '))
#     new_array.append(user_input)
# nums.extend(new_array)
# print(nums)
# for i in nums:
#     print(i)
# get_rid = int(input('Enter the number you wish to remove: '))
# nums.remove(get_rid)
# print(nums)
# how_many = int(input('Enter the number, which you want to check how many times it appears in array: '))
# print(how_many, 'appears', nums.count(how_many), 'times')

"""
088  
Ask the user for a list of five  integers. 
Store them in an array.  Sort the list and 
display it in  reverse order.  
"""
# from array import *
# new_array = array('i', [])
# for i in range(5):
#     new_array.append(int(input('Enter a number: ')))
# new_array.reverse()
# print(new_array)
    

"""
089  
Create an array which will store a list of integers.  
Generate five random numbers and store them in  the array.
Display the array (showing each item on  a separate line). 
"""
# from array import * 
# import random 

# new_array = array('i', [])
# while len(new_array) < 5:
#     random_int = random.randint(1, 1000)
#     new_array.append(random_int)
# for i in new_array:
#     print(i)

"""
090  
Ask the user to enter numbers. 
If they enter a  number between 10 and 20, 
save it in the array,  otherwise display the 
message “Outside the  range”. Once five numbers 
have been  successfully added, display the 
message “Thank  you” and display the array 
with each item shown on a separate lines
"""
# from array import * 

# new_array = array('i', [])
# while len(new_array) < 5:
#     user_input = int(input('Enter number: '))
#     if user_input in range(10,21):
#         new_array.append(user_input)
#     else: 
#         print('Outside the range')
# for i in new_array:
#     print(i)

"""
091  
Create an array which contains  five numbers 
(two of which  should be repeated). Display  
the whole array to the user. Ask  the user to 
enter one of the  numbers from the array and  
then display a message saying  how many times 
that number  appears in the list. 
"""
# from array import *
# num_array = array('i', [1, 2, 3, 3, 4])  
# print(num_array)
# user_input = int(input('Enter one of the numbers from the array: '))
# if num_array.count(user_input) == 1 :
#     word = "time"
# else: 
#     word = "times"
# print(user_input, "is in an array", num_array.count(user_input), word)

"""
092  
Create two arrays
(one  containing three numbers that  the user
enters and one  containing a set of five random
numbers). Join these two arrays  together into one 
large array.  Sort this large array and display  
it so that each number appears on a separate line.
"""
# from array import * 
# import random 

# array_1 = array('i', [])
# while len(array_1) < 3:
#     usr_ipt = int(input('Enter number: '))
#     array_1.append(usr_ipt)
# array_2 = array('i', [])
# while len(array_2) < 5:
#     array_2.append(random.randint(1, 1000))
# print('Array 1:', array_1)
# print('Array 2:', array_2)   
# array_1.extend(array_2)
# array_1 = sorted(array_1)
# for i in array_1:
#     print(i)

"""
093  
Ask the user to enter five  numbers. 
Sort them into order  and present them to the user.  
Ask them to select one of the  numbers. 
Remove it from the  original array and save it in a new array.
""" 
# from array import *
# new_array = array('i', [])
# for i in range(5):
#     new_array.append(int(input('Enter a number: ')))
# print(sorted(new_array))  
# get_rid = int(input('Select one of the numbers: '))
# removed = array('i', [get_rid])
# new_array.remove(get_rid)
# print(removed, 'is removed from', new_array)

"""
094  
Display an array of five  numbers. 
Ask the user to  select one of the numbers.  
Once they have selected a  number, display the  
position of that item in the  array. If they enter  
something that is not in  the array, ask them 
to try  again until they select a relevant item
"""
# from array import *
# array_of_5  = array('i', [1,3,4,5,6])
# print(array_of_5)
# user_choice = int(input('Select one of the numbers: '))
# while user_choice not in array_of_5:
#     user_choice =  int(input('Select relevant numbers: '))
# if user_choice in array_of_5:
#     print('index of', user_choice, 'is', array_of_5.index(user_choice))

"""
095  
Create an array of five numbers  between 10 and 100 which 
each have  two decimal places. Ask the user to  enter a whole 
number between 2 and 5.  If they enter something outside of 
that  range, display a suitable error message  and ask them to 
try again until they  enter a valid amount. Divide each of the  
numbers in the array by the number the  user entered and display 
the answers shown to two decimal places
"""
# from array import *
# import math
# new_array = array('f', [10.11, 11.12, 12.13, 13.14, 14.15] )
# divider = int(input('Enter whole number between 2 and 5: '))
# while divider not in range(2, 6):
#     divider = int(input('Enter whole number between 2 and 5: '))
# for i in range(len(new_array)):
#     answer = new_array[i] / divider
#     print(round(answer, 2))

# =============================================================================
# LISTS AND DICTIONARIES
# =============================================================================
# simple_array = [[2,5,8], [3,7,4], [1,6,9]]
# print(simple_array)
# print(simple_array[1])
# simple_array[2][1] = 5
# print(simple_array[1][2])
# print(simple_array)
# simple_array[1].append(3)
# print(simple_array)
# data_set = {"A": {'x':54, 'y':82, 'z':91}, "B": {'x':75, 'y':29, 'z':80 }}
# print(data_set["A"])
# print(data_set["B"]["y"])
# for i in data_set:
#     print(data_set [i]["y"])

"""
096  
Create the following using a  simple 2D list using the  
standard Python indexing: 
"""
#2D_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] 

"""
097  Using the 2D list from program 096, 
ask the user to  select a row and a column 
and display that value. 
"""
# list_2D = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] 
# row = int(input('Enter row: '))
# column = int(input('Enter column: '))
# print(list_2D[row][column])

"""
098  
Using the 2D list from program 096, 
ask the user  which row they would like 
displayed and display  just that row. 
Ask them to enter a new value and  add 
it to the end of the row and display the row  again. 
"""
# list_2D = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] 
# row = int(input('Enter row: '))
# print(list_2D[row])
# value = int(input('Enter the value: '))
# list_2D[row].append(value)
# print(list_2D[row])

"""
099  
Change your previous program  
to ask the user which row they  
want displayed. Display that  row. 
Ask which column in that  row they 
want displayed and  display the value 
that is held  there. Ask the user if 
they want  to change the value. If they do,  
ask for a new value and change  the data. 
Finally, display the whole row again

Lacey, Nichola. Python by Example. Cambridge University Press. Kindle Edition. 
"""
# list_2D = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] 
# row = int(input('Enter row: '))
# print(list_2D[row])
# column = int(input('Which columnd in this row you want to display?: '))
# print(list_2D[row][column])
# value_change  = input('Do you want to change this value?(y/n): ')
# value_change  = value_change.lower()
# if value_change == 'y':
#     value = int(input('Please enter desired value: '))
#     list_2D[row][column] = value
#     print('value in row:', row, 'column:', column, 'succesfully changed to:', list_2D[row][column])
# else: 
#     print('value in row:', row, 'column:', column, 'remains unchanged:', list_2D[row][column])
# print(list_2D[row])

"""
100  
Create the following table using a 2D dictionary showing  
the sales each person has made in the different
geographical regions: 

      |   N   |   S   |   E   |   W   |
---------------------------------------      
 John | 3056  | 8464  | 8441  | 2694  |
---------------------------------------
 Tom  | 4832  | 6786  | 4737  | 3612  |
---------------------------------------
 Anne | 5239  | 4802  | 5820  | 1859  |
---------------------------------------
 Fion | 3904  | 3645  | 8821  | 2451  |


101  
Using program 100:
    - ask the user for a name and a region. 
    - Display the relevant data. 
    - Ask  the user for the name and 
    region of data they want to change and allow them to make  
    the alteration to the sales figure. 
    - Display the sales for all regions for the name they choose.
 
Lacey, Nichola. Python by Example. 
Cambridge University Press. Kindle Edition.
"""

#  functions to use with input mistakes 
# def reg(x):
#      regions = ['N','S','E','W']
#      while x not in regions:
#          x = input('Please enter valid region (N,S,E,W): ')
#      return x

# def name(x):
#     names = ['John', 'Tomi', 'Anne', 'Fion']
#     while x not in names:
#         x = input('Please enter valid employee name: ')
#     return x 

 
# sale_reg = {"John": {"N": 3056, "S": 8464, "E": 8441, "W": 2694}, 
#             "Tomi": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#             "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#             "Fion": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

# name_ipt = input('To check results, please enter the name of sales rep.: ')
# name_ipt = name(name_ipt)

# region_ipt = input('Please enter region (N,S,E,W): ')
# region_ipt = reg(region_ipt)

    
# print('Result of', name_ipt, 'in region', region_ipt, "is: ", sale_reg[name_ipt][region_ipt])
# name_ipt = input('To change results, please enter the name of sales rep.: ')
# name_ipt = name(name_ipt)
# region_ipt = input('Please enter region in which you want to maake change (N,S,E,W): ')
# region_ipt = reg(region_ipt)
# value = int(input('Enter value you want to save for this region: '))
# guestion_check = question_check = input('Are you sure you want to save this change?(y/n): ')
# guestion_check.lower()
# if guestion_check == 'y':
#     sale_reg[name_ipt][region_ipt] = value
#     print(name_ipt, "sales figures:", sale_reg[name_ipt])
# else: 
#     print('Sales results unchanged')

# print('\nCheers! t.')



# y = [["Mary", "Jack", "Tiffany"], 
#           ["Brad", "Claire"],
#           ["Molly", "Andy", "Carla"]]

# student_list = []
# for x in y:

#     for z in x:
        
#         student_list.append(z)

# print(student_list)

###########matrix creation##############
# matrix = [] 
  
# for i in range(2): 
      
#     # create empty row (a sublist inside our list)
#     matrix.append([]) 
#     print(matrix)
#     for j in range(5): 
#         matrix[i].append(j) 
# print(matrix)
# text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
#         ["Ephemeral", "lasts", "one", "day", "only"],
#         ["Accolade", "is", "an", "expression", "of", "praise"]]
# user_input = int(input())       
# input_list = []
# for lists in text:
#     print(lists)
#     for word in lists:
#         print(word)
#         if len(word) <= user_input:
#                 input_list.append(word)
# print(input_list)

"""
102  
Ask the user to enter the name, age and shoe size for four  people. 
Ask for the name of one of the people in the list and  display their 
age and shoe size. 
 
103  
Adapt program 102  to display the  names and 
ages of  all the people in  the list but do not  
show their shoe  size.
  
104 
After gathering the four names, ages and shoe sizes,
ask the  user to enter the name of the person they want to 
remove from  the list. Delete this row from the data and display the other rows 
on separate lines
Lacey, Nichola. Python by Example (p. 82). 
Cambridge University Press. Kindle Edition.
"""
list = {}

for i in range(4):
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    shoe_size = int(input('Enter shoesize: '))
    list[name] = {"Age":age, "Shoe size":shoe_size}
ask = input("Enter a name: ")
print(list[ask])
print(list)



