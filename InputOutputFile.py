#

# textFile = open("Sample.txt")             # default is binary mode (b)
"""
the default is platform dependent. 'b' appended to the mode opens the file in binary mode:
now the data is read and written in the form of bytes objects.
This mode should be used for all files that don’t contain text.
"""
# for line in textFile:
#     print(line, end='')
#
# textFile.close()

# textFile = open("Sample.txt", 'r')               # only read the text from file
# for line in textFile:
#     print(line, end='')
#
#  textFile.close()

"""
If you don’t explicitly close a file, Python’s garbage collector will eventually
destroy the object and close the open file for you, but the file may stay open for a while.
Another risk is that different Python implementations will do this clean-up at different times.

It is good practice to use the with keyword when dealing with file objects.
The advantage is that the file is properly closed after its suite finishes,
even if an exception is raised at some point.
Using with is also much shorter than writing equivalent try-finally blocks:
"""

# with open("Sample.txt", 'r') as textFile:
#     lines = textFile.read(30)               # print 30 characters only
# print(lines)

# with open("Sample.txt", 'r') as textFile:
#     for line in textFile:
#         if 'PYTHON' in line.upper():              # printing only those lines, python available
#             print(line, end="")

# readline(): reads a single line from the file; a newline character (\n) is left at the end of the string,
# and is only omitted on the last line of the file if the file doesn’t end in a newline.

# # printing line by line
# with open("Sample.txt", 'r') as textFile:
#     line = textFile.readline()                    #
#     while line:
#         print(line, end="")
#         line = textFile.readline()

# # Only for one line
# with open("Sample.txt", 'r') as textFile:
#     line = textFile.readline()
# print(line)

# with open("Sample.txt", 'r') as textFile:
#     lines = textFile.readlines()                  # read all the lines of a file
# print(lines)
#
# # for line in lines:
# #     print(line, end='')
#
# for line in lines[::-1]:
#     print(line, end='')

# # printing the text in reverse orders
# with open("Sample.txt", 'r') as textFile:
#     lines = textFile.read()
#
# for line in lines[::-1]:
#     print(line, end="")

# # ############## Writing Files ###########
# cities = ["Bombay", "Delhi", "Kolkata", "Bengaluru", "Noida"]
# with open("cities.txt", 'w') as citiesFile:
#     for city in cities:
#         print(city, file=citiesFile)

# ###### Reading the text from the created file # # #######
# cities = []
#
# with open("cities.txt") as citiesFile:
#     for city in citiesFile:
#         cities.append(city.strip("\n"))         # striping the text from the start and last
#
# print(cities)
#
# for city in cities:
#     print(city)

#

# imelda = "More mayhem", "Imelda May", "2011", (
#     (1, "Pulling the ring"),
#     (2, "Psycho"),
#     (3, "Mayhem")
# )
#
# with open("imelda.txt", 'w') as imeldaFile:
#     print(imelda, file=imeldaFile)

# with open("imelda.txt", 'r') as imeldaFile:
#     contents = imeldaFile.readline()
#
# imelda = eval(contents)
# print(imelda)
#
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
#
# for trackDetails in tracks:
#     # print(trackDetails)
#     for track in trackDetails:
#         print(track)


# ######## Reading and Writing Binary files #######

# with open("binary", 'bw') as binaryFile:
#     for i in range(0, 17):
#         binaryFile.write(bytes([i]))

# # OR
# with open("binary", 'bw') as binaryFile:
#     binaryFile.write(bytes(range(17)))

# with open("binary", 'br') as binaryFile:
#     # binaryNum = binaryFile.read()
#     # print(binaryNum)
#     # # OR
#     # for b in binaryFile:
#     #     print(b)
#     # OR
#     # binaryNum = int.from_bytes(binaryFile.read(2), 'big')
#     # print(binaryNum)

# a = 65534       # FF FE
# b = 65535       # FF FF
# c = 65536       # 00 01 00 00
# d = 2998302     # 02 2D C0 1E
#
# with open("binary2", 'bw') as binaryFile:
#     binaryFile.write(a.to_bytes(2, 'big'))
#     binaryFile.write(b.to_bytes(2, 'big'))
#     binaryFile.write(c.to_bytes(4, 'big'))
#     binaryFile.write(d.to_bytes(4, 'big'))
#     binaryFile.write(d.to_bytes(4, 'little'))

# with open("binary2", 'br') as binaryFile:
#     aa = int.from_bytes(binaryFile.read(2), 'big')
#     print(aa)
#     bb = int.from_bytes(binaryFile.read(2), 'big')
#     print(bb)
#     # bba = int.from_bytes(binaryFile.read(4), 'little')
#     # print(bba)
#     cc = int.from_bytes(binaryFile.read(4), 'big')
#     print(cc)
#     dd = int.from_bytes(binaryFile.read(4), 'big')
#     print(dd)
#     ee = int.from_bytes(binaryFile.read(4), 'big')
#     print(ee)
#
#
