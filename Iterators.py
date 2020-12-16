# string = "0123456789"
#
# # for char in string:
# #     print(char)
#
# for char in iter(string):
#     print(char)
#
# myIterator = iter(string)
# print(myIterator)
#
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

dayIt = iter(days)

for day in range(0, len(days)):
    nextDay = next(dayIt)
    print(nextDay)

