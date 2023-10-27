from bank_system.client import Client
from types_bank_account import *


def main():

    client_1 = Client("Nicole", "Watterson", "11111111111-11")
    client_2 = Client("Ricardo", "Watterson", "22222222222-22")
    client_3 = Client("Gumball", "Watterson", "33333333333-33")
    client_4 = Client("Darwin", "Watterson", "44444444444-44")
    client_5 = Client("Anais", "Watterson", "55555555555-55")

    checking_account_1 = CheckingAccount(client_1.name, "123-1", 2500.0, 5000.0)
    checking_account_2 = CheckingAccount(client_2.name, "123-2", 500, 3000)

    deposit_value = 50
    withdraw_value = 10
    transfer_value = 500

    try:
        checking_account_1.transfer_to(checking_account_2, transfer_value)
        print(f"{transfer_value} transfer successful")
    except ValueError as e:
        print(e)

    print(checking_account_1)
    print(checking_account_2)


if __name__ == '__main__':
    main()
