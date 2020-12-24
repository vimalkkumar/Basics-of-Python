import math

# Constants

print("Value of pi : {}".format(math.pi))
print("Value of e : {}".format(math.e))
print("Value of 'Not a number' : {}".format(math.nan))
print("Value of 'Infinity' : {}".format(math.inf))
print("Value of 'Negative Infinity' : {}".format(-math.inf))


# Trigonometry

print("Value of cos(45) : {}".format(math.cos(math.pi / 4)))
print("Value of sin(45) : {}".format(math.sin(math.pi / 4)))
print("Value of tan(45) : {}".format(math.tan(math.pi / 4)))
print("Value of tan(90) : {}".format(math.tan(math.pi / 2)))
print("Value of tan(0) : {}".format(math.tan(math.pi)))

# Ceiling anf Floor

age = 27
height = 165.23

# Ceiling
print(math.ceil(age))
print(math.ceil(height))

# Floor
print(math.floor(age))
print(math.floor(height))


# Factorial, square root
print(math.factorial(5))
print(math.sqrt(25))

# Greatest Common Denominator (GCD)
print(math.gcd(125, 75))

# Degrees and Radians
# Radians
print(math.radians(360))
print(math.radians(45))

# Degrees
print(math.degrees(2 * math.pi))
print(math.degrees(math.pi / 2))
