def main():
    def factorial_number(num):
        result = 1
        for i in range(1, num+1):
            result = i*result
        print("factorial of {} is {}".format(num, result))

    factorial_number(int(input("Enter a number : ")))


if __name__ == "__main__":
    main()
