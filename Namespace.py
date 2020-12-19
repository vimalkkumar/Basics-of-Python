"""

When you use an unqualified name inside a function, Python searches up to four scopes—the
local (L) scope, then the local scopes of any enclosing (E) defs and lambdas, then the
global (G) scope, and then the built-in (B) scope—and stops at the first place the
name is found. If the name is not found during this search, Python reports an error.

• Global names are names at the top level of the enclosing module file.
• Global names must be declared only if they are assigned in a function.
• Global names may be referenced in a function without being declared

"""

# y = 3
x = 5


def funcs1(y=5):
    global x
    print("funcs1 - 1 : {}".format(x))
    x = y**2
    print("funcs1 - 2 : {}".format(x))


# def funcs2(y):
#     global x
#     print("funcs2 - 1 : {}".format(x))
#     x = y*2
#     print("funcs2 - 2 : {}".format(x))
#
#
# print("funcs1 - Up : {}".format(x))
# funcs1(10)
# print("funcs1 - Down : {}".format(x))
#
# print("funcs2 - Up : {}".format(x))
# funcs2(5)
# print("funcs2 - Down : {}".format(x))
