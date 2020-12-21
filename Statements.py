"""

Statement                   Role                Example
Assignment          Creating reference          a, b, c = 154, 'Vimal', 'Kumar'

Calls               Running functions           log.write("Spam, ham\n")

print               Printing objects            print("Hello world")

if/elif/else        Selecting actions           if "python" in text:
                                                print(text)

for/else            Sequence Iteration          for x in range(1, 10):
                                                print(x)

while/else          General loop                while x > y:
                                                print("Python")

pass                Empty placeholder           while True:
                                                pass

break, continue     Loop jumps                  while True:
                                                    if not line:
                                                        break

try/except/finally  Catching Exceptions         try:
                                                    action()
                                                except:
                                                    print("Action errors")

raise               Triggering Exceptions       raise EndSearch, locations

import, from        Module access               import sys
                                                from sys import stdin

def, return, yield  Building functions          def fun(a, b, c = 1, *d):
                                                    return a+b+c+d[0]
                                                def gen(n):
                                                    for i in n:
                                                        yield("i*2")

class               Building objects            class ClassName:
                                                    print("We are inside class")

global              Namespace                    def function():
                                                    global x, y
                                                    x = 'New'

del                 Deleting reference          del data[k]
                                                del data[i:j]
                                                del obj.attr
                                                del variable

exec                Running code strings        exec "import" + moduleName
                                                exec code in gdict, ldict

assert              Debugging checks            assert x > y

with/as             Context Messaging           with open("fileName") as fileOpen:
                                                    process(fileOpen)

lambda                                          funcs = [lambda x: x**2, lambda x: x**3]


"""

a, b, c = 124, 'Vimal', 845
print(a, b, c)

# log.write("Spam, sam\n")