# print('Hello World')
#
# print(range(10))
#
# # for even in range(0, 100, 2):
# #     print(even)
#
# even = list(range(0, 10, 2))
# print(even)
#
# # for odd in range(1, 100, 2):
# #     print(odd)
#
# odd = list(range(1, 10, 2))
# print(odd)

# alphabets = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabets)
#
# print(alphabets.index('f'))
# print(alphabets[5])
#
# decimals = range(0, 10)
# print(decimals.index(5))
#
# oddNumber = range(1, 100000, 2)
# print(oddNumber.index(577))
#
# sevens = range(7, 100000, 7)
# # print(sevens.index(21))
# number = int(input("Enter a positive number : "))
#
# if number in sevens:
#     print("{} is divisible by 7".format(number))
# else:
#     print("{} is not divisible by 7".format(number))
#
#
# decimals = range(0, 100)
#
# myRange = decimals[3:40:3]
# print(myRange)
#
# for i in myRange:
#     print(i)
#
# print('=' * 40)
#
# for i in range(3, 40, 3):
#     print(i)
#
# print(myRange == range(3, 40, 3))

# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))                 # output : [0, 2, 4]
# print(list(range(0, 6, 2)))                 # output : [0, 2, 4]

r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)
print('=' * 10)
for i in range(99, 0, -2):
    print(i)
print('=' * 10)

for i in range(0, 100, -2):         # that's not printing anything
    print(i)

backString = 'egaugnal lufrewop yrev a si nohtyP'

print(backString[::-1])

reverseOrder = range(0, 10)

for i in reverseOrder[::-1]:
    print(i)