# create a program that takes some text and returns a list of all the characters in the text
# that are not vowels, sorted alphabetical order.

sampleText = input('Enter string : ')
enterStr = sampleText.replace(' ', '')                  # eliminate all the whitespaces
print(enterStr)
vowels = frozenset("aeiou")

finalSet = set(enterStr).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)

