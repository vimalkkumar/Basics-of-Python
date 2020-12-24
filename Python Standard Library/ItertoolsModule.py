import itertools

# # infinite counting
#
# # for x in itertools.count(50):       # it unbreakable
# #     print(x)
#
# # result
# for x in itertools.count(50, 5):
#     print(x)
#     if x == 80:
#         break
#
# # Infinite Cycle
#
# # for x in itertools.cycle("Apple"):
# #     print(x, end=' ')
#
# x = 0
# for t in itertools.cycle("Apple"):
#     print(t, end=' ')
#     x = x + 1
#     if x >= 50:
#         break
#
#
# print(" ")
# # Infinite Repeating
#
# for t in itertools.repeat(True):
#     print(t, end=" ")
#     x = x + 1
#     if x > 100:
#         break

# Permutations and combinations

# Permutations - Order matter - Some copies with same inputs but different order
election = {1: "Narendra Modi", 2: "Rahul Gandhi", 3: "Mayawati", 4:"Akhilesh Yadav"}
for p in itertools.permutations(election):
    print(p)

for p in itertools.permutations(election.values()):
    print(p)

# Combinations - Order does not matter - No copies with same inputs

colors = ["Red", "Blue", "Pink", "Yellow", "Purple", "Orange"]
for c in itertools.combinations(colors, 3):
    print(c)
