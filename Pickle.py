import pickle
#
# # The pickle module implements binary protocols for serializing and de-serializing a Python object
# # structure. “Pickling” is the process whereby a Python object hierarchy is converted into a
# # byte stream, and “unpickling” is the inverse operation, whereby a byte stream
# # (from a binary file or bytes-like object) is converted back into an object hierarchy.
# # Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” or “flattening”;
#
# # ******** #
# # The pickle module is not secure against erroneous or maliciously constructed data.
# # Never unpickle data received from an untrusted or unauthenticated source.
# # ******** #
#
# imelda = "More mayhem", "Imelda May", "2011", (
#         (1, "Pulling the ring"),
#         (2, "Psycho"),
#         (3, "Mayhem"),
#         (4, "Kentish well town")
#     )
#
# # with open("imelda.pickle", 'wb') as imeldaPickleFile:
# #     pickle.dump(imelda, imeldaPickleFile)
#
# # with open("imelda.pickle", 'rb') as imeldaPickleFile:
# #     imeldaPickle = pickle.load(imeldaPickleFile)
# #
# # print(imeldaPickle)
# #
# # title, artist, year, tracks = imeldaPickle
# #
# # print(title)
# # print(artist)
# # print(year)
# # for track in tracks:
# #     trackNo, trackTitle = track
# #     print("  {} - {}".format(trackNo, trackTitle))
#
# # ********************** #
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", 'bw') as imeldaPickleFile:
#     pickle.dump(imelda, imeldaPickleFile, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, imeldaPickleFile, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(odd, imeldaPickleFile, protocol=0)
#
# with open("imelda.pickle", 'br') as imeldaPickleFile:
#     imeldaPickle = pickle.load(imeldaPickleFile)
#     evenList = pickle.load(imeldaPickleFile)
#     oddList = pickle.load(imeldaPickleFile)
#
# print(imeldaPickle)
# print(evenList)
# print(oddList)
#
# title, artist, year, tracks = imeldaPickle
# print("Title - {}".format(title))
# print("Artist - {}".format(artist))
# print("Year - {}".format(year))
# print("Tracts of {}".format(artist))
# for track in tracks:
#     trackNo, trackTitle = track
#     print(" {} - {}".format(trackNo, trackTitle))
#
# print("*" * 40)
#
# for i in evenList:
#     print(i)
#
# print("*" * 40)
#
# for i in oddList:
#     print(i)
#

# ***** For Removing the pickle file from system ******
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")             #Mac/Linux
# # pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR")             # Windows
