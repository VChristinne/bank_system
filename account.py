import abc  # abstract base classes
from colorama import Fore
from bank_system.history import History


class Account(abc.ABC):

    def __init__(self, holder, number, balance, limit, destination=None):
        self._limit = limit
        self._balance = balance
        self._number = number
        self._holder = holder
        self._destination = destination
        self._history = History()

    def __str__(self):
        return (Fore.GREEN + f"\nAccount Info:"
                             f"\nNumber -> {self._number}"
                             f"\nHolder -> {self._holder}"
                             f"\nBalance -> {self._balance}"
                             f"\nLimit -> {self._limit}\n")

    def deposit(self, value):
        if value > 0:
            new_balance = self._balance + value
            if new_balance <= self._limit:
                self._balance = new_balance
            else:
                raise ValueError(Fore.RED + "Limit Exceeded!" + Fore.RESET)
        else:
            raise ValueError(Fore.YELLOW + "Tried to deposit less than $1!" + Fore.RESET)

    def withdraw(self, value):
        if value < 0:
            raise ValueError(Fore.YELLOW + "Tried to withdraw less than $1!" + Fore.RESET)
        elif self._balance < value:
            raise ValueError(Fore.RED + "Insufficient funds!" + Fore.RESET)
        else:
            self._balance -= value
            return True

    def transfer_to(self, destination, value):
        withdrew = self.withdraw(value)
        if not withdrew:
            return False

        if isinstance(destination, Account):
            destination._balance += value
            return True
        else:
            raise ValueError(Fore.RED + "Invalid destination account!" + Fore.RESET)

    @property
    def balance(self):
        return self._balance

    @abc.abstractmethod
    def update(self, tax):
        self._balance += self._balance * tax
