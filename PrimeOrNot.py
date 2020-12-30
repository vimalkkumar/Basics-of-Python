def main():
    # print('Hello World')
    def prime(num):

        for i in range(2, num // 2):
            if num % i == 0:
                print("{} is not a prime number".format(num))
                break
        else:
            print("{} is a prime number".format(num))

    number = int(input("Please, Enter a number : "))
    if number > 1:
        prime(number)
    else:
        print("{} is a prime number".format(number))


if __name__ == "__main__":
    main()
