"""
A "shelf" is a persistent, dictionary-like object.  The difference with dbm databases is
that the values (not the keys!) in a shelf can be essentially arbitrary Python objects
-- anything that the "pickle" module can handle.
This includes most class instances, recursive data types, and objects containing lots of
shared sub-objects. The keys are ordinary strings.
"""

import shelve
#
# print(dir())
help(shelve)
# for m in dir(shelve):
#     print(m)

# with shelve.open('shelveFileOne') as fruits:
#     fruits["apple"] = "good for making cider"
#     fruits["orange"] = "a sweet citrus fruit"
#     fruits["lemon"] = "a sour yellow citrus fruit"
#     fruits["mango"] = "a powerful energetic fruit"
#     fruits["grape"] = "a small, sweet fruit growing in bunches"
#
#     print(fruits['lemon'])
#     print(fruits["apple"])
# print(fruits)                   # <shelve.DbfilenameShelf object at 0x7fc8a5dd3cc0>


# fruits = shelve.open('shelveFileOne')
# fruits["apple"] = "good for making cider"
# fruits["orange"] = "a sweet citrus fruit"
# fruits["lemon"] = "a sour yellow citrus fruit"
# fruits["mango"] = "a powerful energetic fruit"
# fruits["grape"] = "a small, sweet fruit growing in bunches"
#
# print(fruits['lemon'])
# print(fruits["apple"])
#
# fruits.close()

# below code dosen't replicate like shelve
# with shelve.open('shelveFileOne') as fruits:
#     fruits = {"apple": "good for making cider",
#     "orange": "a sweet citrus fruit",
#     "lemon": "a sour yellow citrus fruit",
#     "mango": "a powerful energetic fruit",
#     "grape": "a small, sweet fruit growing in bunches"}
#
#     print(fruits['mango'])
# print(fruits["orange"])
# print(fruits)

