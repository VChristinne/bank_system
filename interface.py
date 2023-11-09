import tkinter
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from bank_system.account import Account
from file_manager import FileManager

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/indigo.json")

root = ctk.CTk()
root.title("Cashinator")
root.geometry("1280x720")
root.wm_attributes('-fullscreen', False)
root.resizable(True, True)
root.minsize(600, 700)
root.maxsize(3840, 2160)

images = ctk.CTkImage(light_image=Image.open("images/sonoma_light.png"),
                      dark_image=Image.open("images/sonoma_dark.png"),
                      size=(3840, 2160))  # render to 4K monitor

background = ctk.CTkLabel(master=root, image=images)
background.pack()


def deposit_function(username):
    data = FileManager.load_data('files_json/accounts_list.json')

    try:
        for client in data:
            if client['holder'] == username:
                account = Account(client['id_'], client['holder'], client['balance'], client['limit'],
                                  client['password'])
                amount_to_deposit = float(tkinter.simpledialog.askfloat("Deposit", "Enter amount to be deposited:"))
                account.deposit(amount_to_deposit)
                client['balance'] = account.balance
                break
        FileManager.save_data('files_json/accounts_list.json', data)
        create_home_page(username=client['holder'], balance=account.balance)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for deposit amount.")


def withdraw_function(username):
    data = FileManager.load_data('files_json/accounts_list.json')

    try:
        for client in data:
            if client['holder'] == username:
                account = Account(client['id_'], client['holder'], client['balance'], client['limit'],
                                  client['password'])
                amount_to_withdraw = float(tkinter.simpledialog.askfloat("Withdraw", "Enter amount to be withdrew:"))
                account.withdraw(amount_to_withdraw)
                client['balance'] = account.balance
                break
        FileManager.save_data('files_json/accounts_list.json', data)
        create_home_page(username=client['holder'], balance=account.balance)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for withdraw amount.")


# TODO: fix account to transfer error
def transfer_function(username):
    data = FileManager.load_data('files_json/accounts_list.json')

    try:
        for client in data:
            if client['holder'] == username:
                account = Account(client['id_'], client['holder'], client['balance'], client['limit'],
                                  client['password'])
                account_to_transfer = float(tkinter.simpledialog.askstring("Transfer", "Enter account to transfer:"))
                amount_to_transfer = float(tkinter.simpledialog.askfloat("Transfer", "Enter amount to be transfer:"))
                account.transfer_to(account_to_transfer, amount_to_transfer)
                client['balance'] = account.balance
                break
        FileManager.save_data('files_json/accounts_list.json', data)
        create_home_page(username=client['holder'], balance=account.balance)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for transfer amount.")


# TODO: fix show history error
def history_function(username):
    data = FileManager.load_data('files_json/accounts_list.json')

    try:
        for client in data:
            if client['holder'] == username:
                account = Account(client['id_'], client['holder'], client['balance'], client['limit'],
                                  client['password'])
                account.get_history()
                break
        create_home_page(username=client['holder'], balance=account.balance)
    except ValueError:
        messagebox.showerror("Error", "Invalid input for withdraw amount.")


def create_home_page(username, balance):
    custom_frame = ctk.CTkFrame(master=background, width=600, height=700)
    custom_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    head_1 = ctk.CTkLabel(master=custom_frame,
                          text=f'Hey, {username}!',
                          font=('SF Pro', 25))
    head_1.place(x=60, y=60)

    head_2 = ctk.CTkLabel(master=custom_frame,
                          text='Account',
                          font=('SF Pro', 20),
                          text_color=('#727272', '#CFCFCF'))
    head_2.place(x=60, y=120)

    budget_info_frame = ctk.CTkFrame(master=custom_frame,
                                     width=480,
                                     height=80,
                                     fg_color=('#A1A0E8', '#69648E'))
    budget_info_frame.place(x=60, y=180)

    budget_info = ctk.CTkLabel(master=budget_info_frame,
                               text=f'$ {float(balance):,.2f}',
                               font=('SF Pro', 20))
    budget_info.place(x=20, y=28)

    deposit_btn = ctk.CTkButton(master=custom_frame,
                                width=90,
                                height=80,
                                text=f'⤵\nDeposit',
                                font=('SF Pro', 18),
                                command=lambda: deposit_function(username))
    deposit_btn.place(x=80, y=300)

    withdraw_btn = ctk.CTkButton(master=custom_frame,
                                 width=90,
                                 height=80,
                                 text=f'⤴\nWithdraw',
                                 font=('SF Pro', 18),
                                 command=lambda: withdraw_function(username))
    withdraw_btn.place(x=190, y=300)

    transfer_btn = ctk.CTkButton(master=custom_frame,
                                 width=90,
                                 height=80,
                                 text=f'↪\nTransfer',
                                 font=('SF Pro', 18),
                                 command=lambda: transfer_function(username))
    transfer_btn.place(x=300, y=300)

    history_btn = ctk.CTkButton(master=custom_frame,
                                width=90,
                                height=80,
                                text=f'↔\nHistory',
                                font=('SF Pro', 18),
                                command=lambda: history_function(username))
    history_btn.place(x=410, y=300)

    return custom_frame


def login_function(username, password):
    data = FileManager.load_data('files_json/accounts_list.json')

    def check_credentials():
        for client in data:
            if client['holder'] == username and client['password'] == password:
                account = Account(client['id_'], client['holder'], client['balance'], client['limit'],
                                  client['password'])
                create_home_page(username, account.balance)
                return True
        return False

    if not check_credentials():
        messagebox.showerror("Error", "Invalid username or password")


def show_login_menu():
    global login_frame
    login_frame.destroy()
    login_frame = create_login_frame()


def register_function(id_, holder, balance, limit, password):
    try:
        data = FileManager.load_data('files_json/accounts_list.json')

        if check_already_exist(data, holder, id_):
            messagebox.showerror("Error", "Account already exists.")
            return

        new_account = {
            "id_": id_,
            "holder": holder,
            "balance": balance,
            "limit": limit,
            "password": password
        }
        data.append(new_account)

        FileManager.save_data('files_json/accounts_list.json', data)
        show_success_message()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def check_already_exist(data, username, number):
    for client in data:
        if client['holder'] == username and client['id'] == number:
            return True
    return False


def create_login_frame():
    custom_frame = ctk.CTkFrame(master=background, width=320, height=360)
    custom_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login_text = ctk.CTkLabel(master=custom_frame, text="Log in to your account", font=('SF Pro', 22))
    login_text.place(x=55, y=40)

    entry_username = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Username')
    entry_username.place(x=50, y=110)

    entry_password = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Password', show="*")
    entry_password.place(x=50, y=165)

    create_account = ctk.CTkButton(master=custom_frame,
                                   width=150,
                                   height=25,
                                   text="Register your account",
                                   font=('SF Pro', 12),
                                   fg_color="#838383",
                                   hover_color="#5d5d5d",
                                   command=lambda: toggle_to_register_frame())
    create_account.place(x=120, y=270)

    btn_login = ctk.CTkButton(master=custom_frame, width=220, height=35, text="Login",
                              command=lambda: login_function(entry_username.get(), entry_password.get()))
    btn_login.place(x=50, y=230)

    return custom_frame


login_frame = create_login_frame()  # toggle_to_register_frame


def toggle_to_register_frame():
    login_frame.destroy()
    create_register_frame()


def show_success_message():
    messagebox.showinfo("Success", "Account created successfully.")
    show_login_menu()


def create_register_frame():
    custom_frame = ctk.CTkFrame(master=background, width=320, height=390)
    custom_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    register_text = ctk.CTkLabel(master=custom_frame, text="Create your account", font=('SF Pro', 22))
    register_text.place(x=62, y=40)

    entry_number = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Number')
    entry_number.place(x=50, y=90)

    entry_username = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Holder')
    entry_username.place(x=50, y=135)

    entry_balance = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Balance')
    entry_balance.place(x=50, y=180)

    entry_limit = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Limit')
    entry_limit.place(x=50, y=225)

    entry_password = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Password', show="*")
    entry_password.place(x=50, y=270)

    btn_register = ctk.CTkButton(master=custom_frame, width=220, height=35, text="Create",
                                 command=lambda: register_function(entry_number.get(),
                                                                   entry_username.get(),
                                                                   entry_balance.get(),
                                                                   entry_limit.get(),
                                                                   entry_password.get()))
    btn_register.place(x=50, y=330)

    return custom_frame


create_login_frame()
root.mainloop()
