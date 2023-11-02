import tkinter
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter as ctk
from file_manager import FileManager
from types_bank_account import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/indigo.json")

app = ctk.CTk()
app.geometry("1280x720")
app.title("Login")
app.wm_attributes('-fullscreen', True)


def load_data():
    try:
        FileManager.load_data('files_json/accounts_list.json')
    except Exception as e:
        messagebox.showerror("Error", str(e))


def save_data():
    try:
        data = {}
        FileManager.save_data('files_json/accounts_list.json', data)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def button_function(username, password):
    data = FileManager.load_data('files_json/accounts_list.json')

    for client in data:
        if client['holder'] == username and client['password'] == password:
            app.destroy()
            window = ctk.CTk()
            window.geometry("1280x720")
            window.title("Welcome")
            label1 = ctk.CTkLabel(master=window, text="Home Page", font=('SF Pro', 60))
            label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
            window.mainloop()
            return

    messagebox.showerror("Error", "Invalid username or password")


def menu_frame():
    images = ctk.CTkImage(light_image=Image.open("images/sonoma_light.png"),
                          dark_image=Image.open("images/sonoma_dark.png"),
                          size=(1920, 1080))

    background = ctk.CTkLabel(master=app, image=images)
    background.pack()

    custom_frame = ctk.CTkFrame(master=background, width=320, height=360)
    custom_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login_text = ctk.CTkLabel(master=custom_frame, text="Log in to your account", font=('SF Pro', 22))
    login_text.place(x=55, y=40)

    entry_username = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Username')
    entry_username.place(x=50, y=110)

    entry_password = ctk.CTkEntry(master=custom_frame, width=220, height=35, placeholder_text='Password', show="*")
    entry_password.place(x=50, y=165)

    btn_login = ctk.CTkButton(master=custom_frame, width=220, height=35, text="Login",
                              command=lambda: button_function(entry_username.get(), entry_password.get()),
                              corner_radius=6)
    btn_login.place(x=50, y=240)


menu_frame()
app.mainloop()
