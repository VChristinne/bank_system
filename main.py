from bank_system.client import Client
from bank_system.history import History
from types_bank_account import *


def initialize_checking_account(client_data, account_data):
    client = Client(*client_data)
    account = CheckingAccount(client.name, *account_data)
    history = History(account.number)

    # name | number | balance | limit
    with open("checking-accounts.txt", "a") as file:
        file.write(f"{client_data[2]} | {account_data[1]} | {account_data[2]} | {account_data[3]}\n")

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
    clients = []
    accounts = []
    with open("accounts.txt", "r") as file:
        for line in file:
            cpf, number, balance, limit = line.strip().split("|")
            client = Client("", "", cpf)
            account = CheckingAccount(client.name, number, float(balance), float(limit))
            clients.append(client)
            accounts.append(account)
    return clients, accounts


def main():
    client_1_data = ("Nicole", "Watterson", "11111111111-1")
    account_1_data = ("123", 2500.0, 5000.0)

    client_2_data = ("Ricardo", "Watterson", "22222222222-2")
    account_2_data = ("456", 500.0, 2000.0)

    client_3_data = ("Gumball", "Watterson", "33333333333-3")
    account_3_data = ("789", 5.0, 500.0)

    client_1, checking_account_1, history_1 = initialize_checking_account(client_1_data, account_1_data)
    client_2, saving_account_1, history_2 = initialize_saving_account(client_2_data, account_2_data)
    client_3, investment_account_1, history_3 = initialize_investment_account(client_3_data, account_3_data)

    deposit_value = 10
    # withdraw_value = 10
    # transfer_value = 500

    '''
    try:
        checking_account_1.withdraw(withdraw_value)
    except ValueError as e:
        print(e)
    '''

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

    checking_account_1.update()
    print(checking_account_1)

    saving_account_1.update()
    print(saving_account_1)

    investment_account_1.update()
    print(investment_account_1)


if __name__ == '__main__':
    main()
