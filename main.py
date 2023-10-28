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


def menu():
    print("Type Banck Account:"
          "\n1. Deposit"
          "\n2. Withdraw"
          "\n3. Transfer"
          "\n4. History")
    user_input = input("Option: ")

    match user_input:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case _:
            raise ValueError(f"Invalid Option: {user_input}")


def main():
    # types accounts: checking | saving | investment
    # deposit | withdraw | transfer | history | list clients | list accounts
    account_1 = CheckingAccount.load_account("12345")
    account_1.deposit(10)
    print(account_1)


if __name__ == '__main__':
    main()
