"""
A set is similar to a list except that each item in the set must be unique.
"""


# farmAnimals = {"sheep", "cow", "hen"}                   # first way to define set
# print(farmAnimals)
# print(type(farmAnimals))
# for animal in farmAnimals:
#     print(animal)
#
# wildAnimals = set(['lion', 'zebra', 'elephant'])
# print(wildAnimals)
# print(type(wildAnimals))
# for animal in wildAnimals:
#     print(animal)
#
# farmAnimals.add('horse')                    # adding a element in set farmAnimals
# print(farmAnimals)
#
# wildAnimals.add('horse')                    # adding a element in set wildAnimals
# print(wildAnimals)

# emptySetOne = {}
# emptySetTwo = set()
#
# # emptySetOne.add('a')                      # its treat like a dictionary so adding impossible
# emptySetTwo.add('a')
#
# print(emptySetOne)
# print(emptySetTwo)

evens = set(range(0, 40, 2))
print(evens)
print(len(evens))
squaresTuple = (4, 9, 16, 25, 36)
squares = set(squaresTuple)
print(squares)
print(len(squares))


# print(evens.union(squares))                         # UNION operation
# print(len(evens.union(squares)))
#
# print(squares.union(evens))
# print(len(squares.union(evens)))
#
# print(evens.intersection(squares))                  # INTERSECTION operation
# print(len(evens.intersection(squares)))
#
# print(squares.intersection(evens))
# print(len(squares.intersection(evens)))
#
# print(squares & evens)                              # INTERSECTION operation using "&" symbol
# print(len(squares & evens))

# print(sorted(evens))
# print(sorted(squares))
#
# # SUBTRACTION using difference method
# print(sorted(squares.difference(evens)))          # squares - evens = squares items not in evens
# print(sorted(evens.difference(squares)))          # evens - squares = evens items not in squares
#
# # SUBTRACTION using "-" symbol
# print(squares - evens)                            # squares - evens = squares items not in evens
# print(evens - squares)                            # evens - squares = evens items not in squares

# squares.difference_update(evens)
# print(squares)
#
# evens.difference_update(squares)
# print(evens)

# print("Symmetric evens minus squares ")
# print(evens.symmetric_difference(squares))
#
# print("symmetric squares minus evens")
# print(squares.symmetric_difference(evens))
#

# print("Symmetric evens minus squares Updated ")
# evens.symmetric_difference_update(squares)
# print(evens)

# print("symmetric squares minus evens Updated")
# squares.symmetric_difference_update(evens)
# print(squares)

# Removing and discarding the elements from the set

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)              # no error, does nothing
# # squares.remove(8)               # error
#
# print(squares)
#
# # option 1
# if 8 in squares:
#     squares.remove(8)
# # option 2
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not the member of squares")

# # Subset and Superset
# squares.discard(9)
# squares.discard(25)
# if squares.issubset(evens):
#     print("Square is the subset of evens set")
#
# if evens.issuperset(squares):
#     print("evens is the superset of squares set")

# frozenset


even = frozenset(range(0, 20, 2))
print(even)
print(type(even))

