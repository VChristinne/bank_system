from colorama import Fore
from types_bank_account import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

def main():
    # types accounts: checking | saving | investment
    # deposit | withdraw | transfer | history | list clients | list accounts
    account_1 = CheckingAccount.load_account("12345")

    while True:
        print("\nActions:"
              "\n1. Deposit"
              "\n2. Withdraw"
              "\n3. Transfer"
              "\n4. History"
              "\n5. Account Info")
        user_input = input("Option: ")

        try:
            match user_input:
                case '1':
                    amount = float(input("Amount to be deposited: "))
                    account_1.deposit(amount)
                case '2':
                    amount = float(input("Amount to be withdrawn: "))
                    account_1.withdraw(amount)
                case '3':
                    destination = str(input("Account to transfer: "))
                    amount = float(input("Amount to transfer: "))
                    account_1.transfer_to(destination, amount)
                case '4':
                    print(account_1.get_history())
                case '5':
                    print(account_1)
                case _:
                    print(Fore.RED + "\nInvalid Option" + Fore.RESET)
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    main()
