"""
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value,
and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces.
"""
# # Empty dictionary
# color = {}
# print(color)
# print(type(color))
#
# # adding new key-value pair in to dictionary
# color["green"] = 5
# color["red"] = 6
# print(color)

fruits = {"apple": "good for making cider",
          "orange": "a sweet citrus fruit",
          "lemon": "a sour yellow citrus fruit",
          "mango": "a powerful energetic fruit",
          "grape": "a small, sweet fruit growing in bunches"}

# print(fruits)
# print(fruits['apple'])          # printing individual item by the key
# # updating the description of the particular key
# fruits['orange'] = 'very sweet citrus fruit'
# print(fruits)
#
# # Adding the new key-value pair in the dictionary
# fruits["ginger"] = "this is not a fruit"
# print(fruits)

# # Be aware that the deleted key-value pair is removed permanently.
# del fruits["apple"]             # deleting the key and its description
# print(fruits)
#
# fruits.clear()                  # clear the whole dictionary but it's brackets are still left
# print(fruits)

# print(fruits['banana'])         # KeyError: 'banana'; banana is not in the dictionary

# printing the key-value pair along with key and value
# for fruitName, description in fruits.items():
#     print("The " + fruitName.title() + " is " + description+".")

# while True:
#     key = input("Please enter a fruit ('quit' for quiting): ")
#     if key == 'quit':
#         break
#     if key in fruits:
#         description = fruits.get(key)
#         print(description)
#     else:
#         print('{} is not in the bucket'.format(key))

# orderKeys = list(fruits.keys())
# orderKeys.sort()
# for fruit in orderKeys:
#     print(fruit + ' - ' + fruits[fruit])

# OR

# orderKeys = sorted(list(fruits.keys()))
# for fruit in orderKeys:
#     print(fruit + ' - ' + fruits[fruit])

# OR

# for fruit in sorted(list(fruits.keys())):
#     print(fruit + ' - ' + fruits[fruit])

# OR

# for fruit in sorted(fruits.keys()):
#     print(fruit + ' - ' + fruits[fruit])

# for f in fruits:
#     print(f + ' - ' + fruits[f])

# for val in fruits.values():
#     print(val)
#
# for key in fruits.keys():
#     print(key)

# print(fruits.keys())
# print(fruits.values())
#
# print(fruits.items())
#
# fruitsTuple = tuple(fruits.items())         # dictionary converted to tuple
# print(fruitsTuple)
#
# print(dict(fruitsTuple))                    # Tuple converted to dictionary

moreFruits = {"banana": "Its wrapper is yellow",
              "pineapple": "Its wrapper is very rough and tough"}

# moreFruits.update(fruits)                     # update method for copy the dictionary
# print(moreFruits)
#
# fruits.update(moreFruits)
# print(fruits)

# testyFruits = fruits.copy()                     # for copy the dictionary into another variables
# print(testyFruits)
# testyFruits.update(moreFruits)
# print(testyFruits)
