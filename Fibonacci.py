import numpy as np


def main():
    def fibonacci(n):
        if n == 0 or n == 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print(fibonacci(20))

    def fibonacci_memorized(n, cache):
        if n == 0 or n == 1:
            return 0

        if cache[n - 1] != 0:
            return cache[n - 1]
        cache[n - 1] = fibonacci_memorized(n - 1, cache) + fibonacci_memorized(n - 2, cache)
        return cache[n - 1]

    print(fibonacci_memorized(20, np.zeros(20, dtype.int)))


if __name__ == "__main__":
    main()

