from bank_system.client import Client
from bank_system.history import History
from types_bank_account import *


def initialize_checking_account(client_data, account_data):
    client = Client(*client_data)
    account = CheckingAccount(client.name, *account_data)
    history = History(account.number)

    with open("checking-accounts.txt", "r") as file:
        existing_accounts = file.readlines()
        for line in existing_accounts:
            if all(item in line for item in [client_data[0], account_data[1], str(account_data[2]), str(account_data[3])]):
                return client, account, history

    with open("checking-accounts.txt", "a") as file:
        file.write(f"{client_data[0]} | {account_data[1]} | {account_data[2]} | {account_data[3]}\n")

    return client, account, history


def initialize_saving_account(client_data, account_data):
    client = Client(*client_data)
    account = SavingAccount(client.name, *account_data)
    history = History(account.number)

    # name | number | balance | limit
    with open("saving-accounts.txt", "a") as file:
        file.write(f"{client_data[0]} | {account_data[1]} | {account_data[2]} | {account_data[3]}\n")

    return client, account, history


def initialize_investment_account(client_data, account_data):
    client = Client(*client_data)
    account = InvestmentAccount(client.name, *account_data)
    history = History(account.number)

    # name | number | balance | limit
    with open("investment-accounts.txt", "a") as file:
        file.write(f"{client_data[0]} | {account_data[1]} | {account_data[2]} | {account_data[3]}\n")

    return client, account, history


def load_existing_accounts():
    accounts = []
    with open("checking-accounts.txt", "r") as file:
        for line in file:
            cpf, number, balance, limit = line.strip().split("|")
            client = Client("", "", cpf)
            account = CheckingAccount(client.name, number, float(balance), float(limit))
            accounts.append(account)
    return accounts


def main():
    deposit_value = 10
    # transfer_value = 500

    '''
    try:
        checking_account_1.deposit(deposit_value)
    except ValueError as e:
        print(e)
    '''

    '''
    try:
        checking_account_1.transfer_to(checking_account_2, 50)
    except ValueError as e:
        print(e)
    '''

    print(load_existing_accounts())


if __name__ == '__main__':
    main()
