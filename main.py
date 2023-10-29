import ttkbootstrap as ttkb
from types_bank_account import *

account_1 = CheckingAccount.load_account("12345")


def handle_button_click():
    selected_option = option_menu.get()

    if selected_option == '1':
        amount = input("Amount to be deposited: ")
        account_1.deposit(amount)
    elif selected_option == '2':
        amount = input("Amount to be withdrawn: ")
        account_1.withdraw(amount)
    elif selected_option == '3':
        destination = input("Account to transfer: ")
        amount = input("Amount to transfer: ")
        account_1.transfer_to(destination, amount)
    elif selected_option == '4':
        account_1.get_history()
    elif selected_option == '5':
        print(account_1)
    else:
        print("Invalid Option")


root = ttkb.Window(title="Christinne S.A.",
                   themename="vapor",
                   size=[800, 500],
                   position=[450, 180])

label = ttkb.Label(text="Christinne S.A.",
                   font=("SF Pro", 30),
                   style="default",
                   padding=50)

label_frame = ttkb.LabelFrame(root,
                              text="MENU",
                              style="info",
                              width=600,
                              height=200,
                              relief="solid",
                              padding=20)

menu = ttkb.Label(label_frame,
                  text="1. deposit"
                       "\n2. withdraw"
                       "\n3. transfer"
                       "\n4. history"
                       "\n5. account info",
                  font=("SF Pro", 18))

option_menu = ttkb.Entry(root,
                         style="sucess")

button = ttkb.Button(root,
                     text="Selecionar Opção",
                     style="success",
                     command=handle_button_click)

label.pack()
label_frame.pack()
menu.pack()
option_menu.pack()
button.pack()
root.mainloop()
