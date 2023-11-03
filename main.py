import tkinter
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
from file_manager import FileManager

ctk.set_appearance_mode("Dark")
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
    app = ctk.CTk()
    app.title("Login")
    app.geometry("1280x720")
    app.resizable(True, True)
    app.minsize(500, 700)
    app.maxsize(3840, 2160)

    for client in data:
        if client['holder'] == username and client['password'] == password:
            app.destroy()  # TODO: app destroy not working
            design_window()
    messagebox.showerror("Error", "Invalid username or password")


def design_window():
    window = ctk.CTk()
    window.title("Welcome")
    window.geometry("1280x720")
    window.resizable(True, True)
    window.minsize(500, 700)
    window.maxsize(3840, 2160)

    label1 = ctk.CTkLabel(master=window, text="Home Page", font=('SF Pro', 60))
    label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    window.mainloop()


def menu_frame():
    background = ctk.CTkLabel(master=root, image=images)
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
root.mainloop()
