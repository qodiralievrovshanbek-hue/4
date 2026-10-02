from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    @abstractmethod
    def get_info(self):
        return f"Egasi: {self._owner}, Hisob raqami: {self._account_number}, Balans: {self._balance}"

    def __str__(self):
        return f"{self._owner} ({self._account_number}): {self._balance}"

    def __repr__(self):
        return f"{type(self).__name__}('{self._account_number}', '{self._owner}', {self._balance})"
    def __bool__(self):
        return self._balance > 0

    def __eq__(self, other):
        return self._account_number == other._account_number

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self._balance > other._balance

    def __ge__(self, other):
        return self._balance >= other._balance

    def __lt__(self, other):
        return self._balance < other._balance

    def __le__(self, other):
        return self._balance <= other._balance

class SavingsAccount(BankAccount):
    def get_info(self):
        return f"Jamg'arma hisob: {self}"

class BusinessAccount(BankAccount):
    def get_info(self):
        return f"Biznes hisob: {self}"

a1 = SavingsAccount("S-1", "Shahriyor", 5500)
a2 = BusinessAccount("B-1", "Vali", 0)

print(a1)
print(repr(a1))
print(bool(a1))
print(a1 == a2)
print(a1 != a2)
print(a1 > a2)
print(a1 <= a2)