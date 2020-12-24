import random

# Print the random value between o and 1
print(random.random())

# picking one random value, it may be 0 or 1
print(random.randrange(2))

decider = random.randrange(2)
if decider == 0:
    print("HEAD")
else:
    print("TAIL")
# picking one random value, from 1 to 7
print(random.randrange(1, 8))

# Random Choice
lotteryWinner = random.sample(range(100), 5)
print(lotteryWinner)

pets = ["Cats", "Dogs", "Fish"]
print(random.choice(pets))

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)

