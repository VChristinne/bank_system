import abc  # abstract base classes
from colorama import Fore
from file_manager import FileManager
from history import History


class Account:

    def __init__(self, holder, id_, balance, limit, password, destination=None):
        self._destination = destination
        self._password = password
        self._limit = limit
        self._balance = balance
        self._id = id_
        self._holder = holder
        self._history = History(self._id)
        self.file_path = "files_json/accounts_list.json"
        self.accounts = FileManager.load_data(self.file_path)

    def __str__(self):
        return (Fore.GREEN + f"\nAccount Info:"
                             f"\nID -> {self._id}"
                             f"\nHolder -> {self._holder}"
                             f"\nBalance -> {self._balance}"
                             f"\nLimit -> {self._limit}" + Fore.RESET)

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
        return self._id

    def add_client(self):
        new_account = {
            "id_": self._id,
            "holder": self._holder,
            "balance": self._balance,
            "limit": self._limit
        }
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
        file_path = "files_json/accounts_list.json"
        accounts = FileManager.load_data(file_path)
        for account_info in accounts:
            if account_info.get("password") == password:
                return Account(
                    holder=str(account_info.get("holder")),
                    id_=str(account_info.get("id")),
                    balance=float(account_info.get("balance")),
                    limit=float(account_info.get("limit")),
                    password=password
                )
        print(Fore.RED + "Password Invalid!" + Fore.RESET)
        return None
