# def fact(n):
#     """ n! iteratively """                    # Docstring
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result
#
#
# for i in range(1, 10):
#     print(i, fact(i))


# def factorial(n):
#     """factorial using recursion n! = n * (n - 1)"""
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
#
# for i in range(1, 10):
#     print(i, factorial(i))


# def fib(n):
#     """F(a) = F(n -1) + F(n - 2)""" # Using recursion
#     if n < 2:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# for i in range(1, 40):
#     print(i, fib(i))

def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, n):
            result = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result


for i in range(1, 40):
    print(i, fibonacci(i))

