import random

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # публічний атрибут
        self.__balance = balance  # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Bohdan", 1000)

for i in range(5):
    # Випадкове поповнення та зняття
    dep = random.randint(100, 500)
    wit = random.randint(50, 600)
    
    account.deposit(dep)
    account.withdraw(wit)
    print(f"Транзакція {i+1}: Поповнено на {dep}, знято {wit}. Баланс: {account.get_balance()}")

print(f"\nКінцевий результат: {account.get_balance()}")