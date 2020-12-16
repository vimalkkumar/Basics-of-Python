# print('Hello World')
# ############### FOR loop ###############

# for i in range(1, 20):            # Range scope is always consider (scope - 1) ex: 19
#     print("i is {}".format(i))

# number = "986,458,458,458,210"
# for i in range(1, len(number)):
# # range domain is start from 0 in case of number printing Ex: Skipping 9 from the number
#     print("{}".format(number[i]))

# number = "986,458,458,458,210"
# for i in range(0, len(number)):
#     print('{}'.format(number[i]))


# number = "986,458,458,458,210"
# cleanedNumber = ''
#
# for char in number:
#     cleanedNumber  += char
#
# print(cleanedNumber)        # But it's a sequence of character or string


# number = "986,458,458,458,210"
# cleanedNumber = ''
# for i in range(0, len(number)):         # range domain is start from 0 in case of number printing
#     if number[i] in "1234567890":
#         cleanedNumber += number[i]
#     newNumber = int(cleanedNumber)
# print("{}".format(newNumber), end='')


# number = "986,458,458,458,210"
# cleanedNumber = ''
#
# for char in number:
#     if char in '1234567890':
#         cleanedNumber += char
#
# newNumber = int(cleanedNumber)
# print(newNumber)


# for state in ["Apple", "Mango", "Orange", "Banana"]:        # it's a list
#     print('The fruit is '+state)
#     # print('The fruit is '+state + '. You wnt to eat. ')


# for i in range(0, 100, 5):
#     print('i is {}'.format(i))


# for i in range(1, 5):
#     for j in range(1, 11):
#         print('{1} times {0} is {2}'.format(i, j, i*j))
#     # print("===========")
#     print('')

# for i in range(1, 5):
#     for j in range(1, 5):
#         print('*', end=' ')
#     print(end='\n')

# ######## Continue Statement ################

# shoppingList = ["Milk", "Bread", "Banana", "Spam", "Protein Powder"]

# for item in shoppingList:
#     if item == 'Spam':
#         continue
#
#     print('Buy '+item)

# ######## Break Statement ################

# shoppingList = ["Milk", "Bread", "Banana", "Spam", "Protein Powder"]
#
# for item in shoppingList:
#     if item == 'Spam':
#         break
#
#     print('Buy '+item)

# meal = ['egg', 'bacon', 'spam', 'beans', 'potato']
# nastyFoodItem = ''
# for item in meal:
#     if item == 'spam':
#         nastyFoodItem = item
#         break
# else:
#     print("I'll have a plate of that, then, Please")
#
# if nastyFoodItem == 'spam':
#     print("Can't I have anything without spam in it")

# ######################## While Loop #####################################

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

availableExit = ["east", "north east", "south"]

chosenExit = ""
while chosenExit not in availableExit:
    chosenExit = input("Please Enter the direction: ")
    if chosenExit == 'quit':
        print('Game Over')
        break
else:
    print("Fail to got out from there")
