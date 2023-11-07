import tkinter
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from file_manager import FileManager

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("theme/indigo.json")

root = ctk.CTk()
root.title("Login")
root.geometry("1280x720")
root.wm_attributes('-fullscreen', True)
root.resizable(True, True)
root.minsize(500, 700)
root.maxsize(3840, 2160)

images = ctk.CTkImage(light_image=Image.open("images/sonoma_light.png"),
                      dark_image=Image.open("images/sonoma_dark.png"),
                      size=(3840, 2160))  # render to 4K monitor


def login_function(username, password):
    data = FileManager.load_data('files_json/accounts_list.json')

    def check_credentials():
        for client in data:
            if client['holder'] == username and client['password'] == password:
                root.destroy()
                design_window()
                return True
        return False

    if not check_credentials():
        messagebox.showerror("Error", "Invalid username or password")


def design_window():
    window = ctk.CTk()
    window.title("Welcome")
    window.geometry("1280x720")
    window.resizable(True, True)
    window.minsize(500, 700)
    window.maxsize(3840, 2160)

    head_1 = ctk.CTkLabel(master=window,
                          text="Welcome back!",
                          font=('SF Pro', 35))
    head_1.place(x=120, y=180)

    head_2 = ctk.CTkLabel(master=window,
                          text="Operations Bank",
                          font=('SF Pro', 30),
                          text_color=("#404040", "#cfcfcf"))
    head_2.place(x=120, y=240)

    window.mainloop()


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


background = ctk.CTkLabel(master=root, image=images)
background.pack()

login_frame = create_login_frame()


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
