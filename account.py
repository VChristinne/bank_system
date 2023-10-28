import abc  # abstract base classes
import time

from colorama import Fore
from bank_system.file_manager import FileManager
from bank_system.history import History


class Account:

    def __init__(self, holder, number, balance, limit, password, destination=None):
        self._destination = destination
        self._password = password
        self._limit = limit
        self._balance = balance
        self._number = number
        self._holder = holder
        self._history = History(self._number)
        self.file_path = "files_txt/accounts_list.txt"
        self.accounts = FileManager.load_data(self.file_path)

    def __str__(self):
        return (Fore.GREEN + f"\nAccount Info:"
                             f"\nNumber -> {self._number}"
                             f"\nHolder -> {self._holder}"
                             f"\nBalance -> {self._balance}"
                             f"\nLimit -> {self._limit}")

    def deposit(self, value):
        if value > 0:
            new_balance = self._balance + value
            if new_balance <= self._limit:
                self._balance = new_balance
                self._history.add_transaction(f"Deposit of ${value}")
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
            self._history.add_transaction(f"Withdraw of ${value}")
            return True

    def transfer_to(self, destination, value):
        withdrew = self.withdraw(value)
        if not withdrew:
            return False

        if isinstance(destination, Account):
            destination._balance += value
            self._history.add_transaction(f"Transfer of ${value}")
            return True
        else:
            raise ValueError(Fore.RED + "Invalid destination account!" + Fore.RESET)

    def get_history(self):
        return self._history

    @property
    def balance(self):
        return self._balance

    @abc.abstractmethod
    def update(self, tax):
        self._balance += self._balance * tax

    @property
    def number(self):
        return self._number

    def add_client(self):
        new_account = [self.number, self._holder, self.balance, self._limit]
        self.accounts.append(new_account)
        FileManager.save_data(self.file_path, self.accounts)

    @staticmethod
    def list_accounts(accounts_list):
        result = "\nAccounts:\n"

        for a in accounts_list:
            result += f"- Number: {a[0]}, Holder: {a[1]}, Balance: {a[2]}, Limit: {a[3]}\n"

        return result

    @staticmethod
    def load_account(password):
        file_path = "files_txt/accounts_list.txt"
        accounts = FileManager.load_data(file_path)
        for account_info in accounts:
            if account_info[4] == password:
                return Account(
                    number=str(account_info[0]),
                    holder=str(account_info[1]),
                    balance=float(account_info[2]),
                    limit=float(account_info[3]),
                    password=str
                )
        print(Fore.RED + "Password Invalid!" + Fore.RESET)
        return None
