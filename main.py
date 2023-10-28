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
    print("Type Banck Account:")
    print("1. Checking")
    print("2. Saving")
    print("3. Investment")
    user_input = input("Opção: ")

    match user_input:
        case '1':
            return 'checking'
        case '2':
            return 'saving'
        case '3':
            return 'investment'
        case _:
            raise ValueError(f"Invalid Option: {user_input}")


def main():
    # types accounts: checking | saving | investment
    # deposit | withdraw | transfer | history | list clients | list accounts
    account_1 = CheckingAccount.load_account("12345")
    print(account_1)


if __name__ == '__main__':
    main()
