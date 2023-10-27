from bank_system.client import Client, FileManager
from bank_system.history import History
from types_bank_account import *


def initialize_checking_account(client_data, account_data):
    client = Client(*client_data)
    client.add_clients(client_data)
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
    '''
    client_1, checking_account_1, history_1 = initialize_checking_account(client_1_data, account_1_data)
    client_2, saving_account_1, history_2 = initialize_saving_account(client_2_data, account_2_data)
    client_3, investment_account_1, history_3 = initialize_investment_account(client_3_data, account_3_data)

    checking_account_1.update()
    print(checking_account_1)

    saving_account_1.update()
    print(saving_account_1)

    investment_account_1.update()
    print(investment_account_1)
    '''

    clients_list = FileManager.load_data("files txt/client_list.txt")
    clients_list_str = Client.list_clients(clients_list)
    print(clients_list_str)


if __name__ == '__main__':
    main()
