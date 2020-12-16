
# List as a sequence of things. Now those things my be string, number, classes or pretty much any thing
# else. If a list can be sequence of strings, and string is it self a sequence type.
# Than it make sense that a list can also a sequence of lists. Which it can.
# square brackets ([]) indicate a list,

birdLists = ['Parrot', 'Owl', 'Crow', 'Sparrow', 'Crow']
# for state in birdLists:
#     print('The bird is ' + state)

# print(birdLists[0])         # for accessing the first element in a list.
# print(birdLists[3])         # for accessing the fourth element in a list.
# print(birdLists[-1])        # for accessing the last element in a list.
# print(birdLists[-2])        # for accessing the second last element in a list.

# Insert or Append
#
# birdLists.append('Eagle')       # append element at the last of the list
# print(birdLists)
#
# birdLists[0] = "Pigeon"
# print(birdLists)         # after updating or replacing the index[0] value
#
# birdLists.insert(1, 'Peacock')          # insert the element in a list at given location
# print(birdLists)

# Deletion from list

# del birdLists[2]        # del statement for deleting the element from a list

# poppedBird = birdLists.pop()        # Remove last items from the list
# print(birdLists)
# print(poppedBird)                   # Also use the popped item after popping it

# poppedBirdAny = birdLists.pop(2)        # Popping 3rd index value from a list
# print(birdLists)
# print(poppedBirdAny)

# birdLists.remove('Crow')                               # Removing an Item by Value
# print(birdLists)

# removeBird = 'Peacock'
# birdLists.remove(removeBird)
# print(birdLists)
# print(removeBird)

# The remove() method deletes only the first occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop to
# determine if all occurrences of the value have been removed.

# birdLists.sort()            # changes the order of a list permanently.
# print(birdLists)
#
# birdLists.sort(reverse=True)          # reverse the order of a list
# print(birdLists)

# print(sorted(birdLists))        # changes the order of a list temporarily

# ###################### Special case for sorting #####################
# animal = ['Zebra', 'rat', 'Rabbit', 'Dog', 'dog']
#
# print(sorted(animal))             # first Uppercase letters and then lowercase letters are sort
# animal.sort()                     # here also, same case
# print(animal)
#########################################

# birdLists.reverse()             # rearrange the list into reverse chronological order
# print(birdLists)
#
# print(len(birdLists))           # length of a list

# print(birdLists[-1])

# numbers = list(range(1, 11))        # list function
# print(numbers)

# ############## Slicing #####################

# print("Slice [:]".format(birdList[:])                           # starting from 0 and ending with last index
# print("Slice [0 : 2] = {}".format(birdLists[0:2]))              # starting index 0 and ending index (2 - 1)
# print("Slice [1 : 3] = {}".format(birdLists[1:3]))              # starting index 1 and ending index (3 - 1)
# print("Slice [2 : ] = {}".format(birdLists[2:]))                # starting index 2 and ending index last index
# print("Slice [ : 5] = {}".format(birdLists[:5]))                # starting index 0 and ending index (5 -1)
# print("Slice [-3 : ] = {}".format(birdLists[-3:]))              # starting index (last index - 3) and backward 3 index
# print("Slice [ : -2] = {}".format(birdLists[:-2]))              # starting index 0 and ending (last index - 2)

# for bird in birdLists[2:-2]:
#     print(bird)

# for bird in birdLists[-6:3]:
#     print(bird)

# for bird in birdLists[-6:-3]:
#     print(bird)

# for bird in birdLists[2:8]:
#     print(bird)

# ###################### Copying List ######

# birds = birdLists[:]            # copying the entire list to the birds Lists
#
# birds.append("Penguin")
# birdLists.append("Parrot")
# print(birds)
# print(birdLists)
#
# birdCon = birdLists
# # connect the new variable birdCon to the list that is already contained in birdList,
# # so now both variables point to the same list.
#
# birdCon.append('Swallow')
# birdLists.append("Woodpecker")
# print(birdCon)
# print(birdLists)

# #################### List Comparision

# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# number = even + odd
# print('The unsorted list = {} '.format(number))
# # number.sort()
# # print('The sorted list = {}'.format(number))
# # print(sorted(number))
# sortNumber = sorted(number)
# print('The sorted list = {}'.format(sortNumber))
# #
# # if sortNumber == number.sort():         # here sort() is the object not work very well
# #     print("the list are equal")
# # else:
# #     print("the list are not equal")
#
# # if number == number.sort():
# #     print("the list are equal")
# # else:
# #     print("the list are not equal")
#
# # if number == sorted(number):            # It shows the list are not equal
# #     print("the list are equal")
# #
# # else:
# #     print("the list are not equal")
#
# # if sortNumber == sorted(number):            # output : the list are equal
# #     print("the list are equal")
# #     print(number)
# #     print(sortNumber)
# #     print(sorted(number))
# # else:
# #     print("the list are not equal")

# ###### List constructor ######

# listOne = []
# listTwo = list()
#
# print('List one : {}'.format(listOne))
# print('List two : {}'.format(listTwo))
#
# if listOne == listTwo:
#     print("The list are equal")
#
# print(list('Hello world'))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

anotherEven = even          # both's pointing the same list
anotherEvenMemory = list(even)   # list constructor return a new list
print(anotherEven)

print(anotherEven is even)
print(anotherEvenMemory is even)        # contents are equal whether they are pointing the different variable in the m/y
print(anotherEven == even)
print(anotherEvenMemory == even)

# numbers = [even, odd]
# print(numbers)
#
# for number in numbers:
#     print(number)
#
#     for value in number:
#         print(value)
