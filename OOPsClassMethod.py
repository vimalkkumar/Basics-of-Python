import datetime

# class Account:
#     """Bank account creation, deposit and withdraw methods inside the class Account"""
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         print("{} account is created".format(self.name))
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         self.show_balance()
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("You have insufficient balance")
#         self.show_balance()
#
#     def show_balance(self):
#         print("{} balance amount is {}".format(self.name, self.balance))
#
#
# if __name__ == '__main__':
#     vimal = Account("Vimal", 0)
#
#     vimal.show_balance()
#     vimal.deposit(1000)
#     vimal.withdraw(20000)
#     vimal.withdraw(500)


class Account:
    """Bank account creation, deposit and withdraw methods inside the class Account"""
    @staticmethod
    def _current_time():
        return datetime.datetime.utcnow()

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print("{} account is created".format(self.name))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("You have insufficient balance")
        self.show_balance()

    def show_balance(self):
        print("{} balance amount is {}".format(self.name, self.balance))

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount == 0:
                tran_type = "deposited"
            elif amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
            print("{:6} {} on {}".format(amount, tran_type, date))


if __name__ == '__main__':
    vimal = Account("Vimal", 0)

    vimal.show_balance()
    vimal.deposit(1000)
    vimal.withdraw(20000)
    vimal.withdraw(500)
    vimal.show_transaction()

    ankit = Account("Ankit", 200)
    ankit.show_balance()
    ankit.withdraw(20000)
    ankit.withdraw(200)
    ankit.deposit(6000)
    ankit.show_transaction()


#  Mangling

class Account:
    """Bank account creation, deposit and withdraw methods inside the class Account"""
    @staticmethod
    def _current_time():
        return datetime.datetime.utcnow()

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance        # mangling the variable
        self._transaction_list = [(Account._current_time(), balance)]
        print("{} account is created".format(self._name))
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("You have insufficient balance")
        self.show_balance()

    def show_balance(self):
        print("{} balance amount is {}".format(self._name, self.__balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount == 0:
                tran_type = "deposited"
            elif amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
            print("{:6} {} on {}".format(amount, tran_type, date))


if __name__ == '__main__':
    vimal = Account("Vimal", 0)

    vimal.show_balance()
    vimal.deposit(1000)
    vimal.withdraw(20000)
    vimal.withdraw(500)
    vimal.show_transaction()

    ankit = Account("Ankit", 200)
    ankit.__balance = 100
    ankit.show_balance()
    ankit.withdraw(20000)
    ankit.withdraw(200)
    ankit.deposit(6000)
    ankit.show_transaction()
    ankit.show_balance()
    print(ankit.__dict__)