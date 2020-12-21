
# Values that cannot change as immutable, and an immutable list is called a tuple.

# List have intended to hold homogeneous items (Items of the same types)
# Tuples are actually to hold heterogeneous items
# Tuples are unchangeable

# tup = 'Hello', 'Hi', 'How are you?'
# print(tup)

print('Hello', 'Hi', 'How are you?')        # It's not a tuple

myDetails = 'My self Vimal Kumar', 'I am from Kanpur', 'and I am 27 years old'

# print(myDetails)
# print(myDetails[1])
# print(myDetails[-1])

for item in myDetails:
    print(item)

# myDetails[1] = 'I am from Lucknow'      # error : 'tuple object does not support item assignment
# we’re trying to alter a tuple, which can’t be done to that type of object

# Tuple supports indexing and slicing
# we could redefine the entire tuple
myDetails = myDetails[0], 'I am from Lucknow', myDetails[2]
print(myDetails)

# a, b, c = 'Hel'
#
# print(a)            # Output : H
# print(b)            # Output : e
# print(c)            # Output : l
#
# d, e, f = myDetails
# print(d)            # Output : My self Vimal Kumar
# print(e)            # Output : I am from Lucknow
# print(f)            # Output : and I am 27 years old

