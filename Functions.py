"""
Syntax                  Location                Interpretation
func(value)             Caller          Normal argument: matched by position
func(name=value)        Caller          Keyword argument: matched by name
func(*name)             Caller          Pass all objects in name as individual positional arguments
func(**name)            Caller          Pass all key/value pairs in name as individual keyword arguments
def func(name)          Function        Normal argument: matches any by position or name
def func(name=value)    Function        Default argument value, if not passed in the call
def func(*name)         Function        Matches and collects remaining positional arguments (in a tuple)
def func(**name)        Function        Matches and collects remaining keyword arguments (in a dictionary)
"""


def fun():
    print("Python function is useful")


fun()
print(fun())            # function return type is None


# def addition(num_first, num_second):                  # Parameter in function
#     num_sum = num_first + num_second
#     print('Sum of {} and {} is {}'.format(num_first, num_second, num_sum))
#
#
# addition(num_first=10, num_second=20)
#

# def addition(num_first, num_second):                  # Parameter in function
#     return num_first + num_second
#     # print('Sum of {} and {} is {}'.format(num_first, num_second, num_sum))
#
#
# print(addition(num_first=10, num_second=20))
# print(addition(20, 20))
# one = int(input("enter first number :"))
# two = int(input("enter second number :"))
# print("Sum of {} and {} is {}.".format(one, two, addition(one, two)))

#
# def center_text(text):
#     text = str(text)
#     left_margin = (100 - len(text)) // 2
#     print(" " * left_margin, text)
#
#
# center_text("Hello, World")
# center_text("How the things going on")
# center_text("Hope, Everything going in the thoughtful direction")
# center_text(12)
# center_text("*")


# def center_text(*args):
#     text = ""
#     for arg in args:
#         text += str(arg) + " "
#     left_margin = (100 - len(text)) // 2
#     print(" " * left_margin, text)


# def center_text(*args, sep=' ', end='\n', file=None, flush=False):        # Like print function
#     text = ""
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (100 - len(text)) // 2
#     print(" " * left_margin, text, end=end, file=file, flush=flush)


# center_text("Hello, World")
# center_text("How the things going on")
# center_text("Hope " + "Everything going in the thoughtful direction", 15, "Wind mill")
# center_text(12)
# center_text("*")

# def center_text(*args):
#     text = ""
#     for arg in args:
#         text += str(arg) + " "
#     left_margin = (100 - len(text)) // 2
#     return " " * left_margin + text


# with open("centerText", "w") as centerFile:
#     s1 = center_text("Hello, World")
#     print(s1, file=centerFile)
#     s2 = center_text("How the things going on")
#     print(s2, file=centerFile)
#     s3 = center_text("Hope " + "Everything going in the thoughtful direction", 15, "Wind mill")
#     print(s3, file=centerFile)
#     s4 = center_text(12)
#     print(s4, file=centerFile)

# with open("centerText", 'r') as centerFile:
#     lines = centerFile.readlines()
#     for line in lines:
#         print(line, end='')

