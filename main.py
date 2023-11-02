import tkinter
from PIL import ImageTk, Image
import customtkinter as ctk
from types_bank_account import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("theme/indigo.json")

app = ctk.CTk()
app.geometry("800x600")
app.title("Login")
app.wm_attributes('-fullscreen', True)

# account_1 = CheckingAccount.load_account("12345")


def button_function():
    app.destroy()
    window = ctk.CTk()
    window.geometry("1280x720")
    window.title("Welcome")
    label1 = ctk.CTkLabel(master=window, text="Home Page", font=('SF Pro', 60))
    label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    window.mainloop()


def menu_frame():
    # background
    bg = ImageTk.PhotoImage(Image.open("images/sonoma_dark.png"))
    l1 = ctk.CTkLabel(master=app, image=bg)
    l1.pack()

    # custom frame
    frame = ctk.CTkFrame(master=l1, width=320, height=360)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    # log in text
    l2 = ctk.CTkLabel(master=frame, text="Log in to your account", font=('SF Pro', 20))
    l2.place(x=60, y=45)

    # usarname
    entry_username = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry_username.place(x=50, y=110)

    # password
    entry_password = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry_password.place(x=50, y=165)

    # button login
    btn_login = ctk.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
    btn_login.place(x=50, y=240)


menu_frame()
app.mainloop()
