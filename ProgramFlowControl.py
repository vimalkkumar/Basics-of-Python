# print("Hello World!!!")
#
for i in range(1, 10):
    print("{} squared is {:3} and Cubed is {:4}".format(i, i**2, i**3))


name = input("Please, Enter your name : ")
age = int(input("{}, enter your age : ".format(name)))

if age >= 18:
    print('Congreats {}, you are old enough to vote'.format(name))
else:
    print('Sorry, {} Come after {} years'.format(name, 18 - age))

# ########################################################

# print('Please guess a number between 1 to 10')
# guess = int(input())

# if guess < 5:
#     print('please guess the higher number')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, You guess the perfect number')
#     else:
#         print('Sorry, you lost the golden chance')
# elif guess > 5:
#     print('Please guess the lower number')
#     guess = int(input())
#     if guess == 5:
#         print('Well done, You guess the perfect number')
#     else:
#         print('Sorry, You lost the golden chance')
# else:
#     print('Congreats, You guess the right number in first attempt')

# if guess != 5:
#     if guess > 5:
#         print('Please guess the lower number')
#     else:
#         print('Please guess the higher number')
#
#     guess = int(input())
#     if guess == 5:
#         print('Well done, You guess the right number')
#     else:
#         print('Sorry, You miss the chance')
# else:
#     print('Congrets, you guess the right number')
#

# ###############################################

# age = int(input('How old are you? '))
#
# # if age >= 16 and age <= 66:
# # if (age >= 16) and (age <= 66):
# if 16 <= age <= 66:
#     print('Have a good day at work!!!!!!!!!')
# else:
#     print('Enjoy your free time')
#
# if age <= 16 or age >= 66:
#     print('Enjoy your free time!!!!')
# else:
#     print('Have a good day at work')

################################

# Boolean data type is not exist in python

# x = 'false'
# if x:       # it understand only 0 (no value or false) or 1(for value or true)
#     print('x is true')
#
# print("""
# False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# ##################NOT keyword##############################

# where 'not false means true' and 'not true means false'

# print('True : {}'.format(not False))
# print('False : {}'.format(not True))

# age = int(input('How old are you : '))
#
# if not (age <= 18):
#     print('Yor are old enough to vote')
# else:
#     print('Please come back in {0} years'.format(18 - age))

# #################### IN Keyword ####################

# parrot = "Norwegian Blue"
#
# letter = input("Enter a charcter : ")
#
# # if letter in parrot:
# #     print('{} is present in row'.format(letter))
# # else:
# #     print('{} is not in paragraph'. format(letter))
#
# if letter not in parrot:
#     print('{} is not in paragraph'. format(letter))
# else:
#     print('{} is present in row'.format(letter))

# ############## Challenge ######################
# write a small program to ask for name and age. when both values have entered,
# check if the person is the right age to go on an 18 - 30 holiday (They must be
# over 18 and under 31). If they are, Welcome them to the holiday, otherwise print a
# polite message refusing them entry
#
# name = input("Enter your name : ")
# age = int(input("how old are {} : ".format(name)))
#
# if 18 <= age <= 31:
#     print('Welcome to the holiday')
# else:
#     print('Sorry, you are not eligible')
