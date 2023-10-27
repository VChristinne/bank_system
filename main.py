from bank_system.client import Client
from bank_system.history import History
from types_bank_account import *


def initialize_client_and_account(client_data, account_data):
    client = Client(*client_data)
    account = CheckingAccount(client.name, *account_data)
    history = History(account.number)

    return client, account, history


def main():
    client_1_data = ("Nicole", "Watterson", "11111111111-1")
    account_1_data = ("123", 2500.0, 5000.0)

    client_2_data = ("Ricardo", "Watterson", "22222222222-2")
    account_2_data = ("456", 500.0, 2000.0)

    client_1, checking_account_1, history_1 = initialize_client_and_account(client_1_data, account_1_data)
    client_2, checking_account_2, history_2 = initialize_client_and_account(client_2_data, account_2_data)

    # deposit_value = 10
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

    print(checking_account_1)
    print(checking_account_2)


if __name__ == '__main__':
    main()
