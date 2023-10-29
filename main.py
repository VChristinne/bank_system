from colorama import Fore

from bank_system.client import Client
from bank_system.history import History
from types_bank_account import *


def initialize_checking_account(client_data, account_data):
    client = Client(*client_data)
    account = CheckingAccount(client.name, *account_data)
    history = History(account.number)
    return client, account, history


def initialize_saving_account(client_data, account_data):
    client = Client(*client_data)
    account = SavingAccount(client.name, *account_data)
    history = History(account.number)
    return client, account, history


def initialize_investment_account(client_data, account_data):
    client = Client(*client_data)
    account = InvestmentAccount(client.name, *account_data)
    history = History(account.number)
    return client, account, history


def main():
    # types accounts: checking | saving | investment
    # deposit | withdraw | transfer | history | list clients | list accounts
    account_1 = CheckingAccount.load_account("12345")

    while True:
        print("\nType Banck Account:"
              "\n1. Deposit"
              "\n2. Withdraw"
              "\n3. Transfer"
              "\n4. History"
              "\n5. Account Info")
        user_input = input("Option: ")

        try:
            match user_input:
                case '1':
                    amount = int(input("Amount to be deposited: "))
                    account_1.deposit(amount)
                case '2':
                    amount = int(input("Amount to be withdrawn: "))
                    account_1.withdraw(amount)
                case '3':
                    destination = str(input("Account to transfer: "))
                    amount = int(input("Amount to transfer: "))
                    account_1.transfer_to(destination, amount)
                case '4':
                    print(account_1.get_history())
                case '5':
                    print(account_1)
                case _:
                    raise ValueError(Fore.RED + "Invalid Option\n" + Fore.RESET)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
