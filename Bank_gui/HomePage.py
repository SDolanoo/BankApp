import tkinter as tk
from tkinter import messagebox
from Bank_gui.bank_gui import BankGui, THEME_COLOR, FONT
from Bank_gui.LoginPage import LoginPage
from Bank_gui.RegisterPage import RegisterPage


class MainPage(BankGui):

    def __init__(self):
        BankGui.__init__(self)
        self.main_page_setup()

    def main_page_setup(self):
        self.title("BankApp")
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.main_canvas = tk.Canvas(width=200, height=200, bg="white")
        self.text = self.main_canvas.create_text(100, 100, width=190, text="Welcome to the main page", font=FONT)
        self.main_canvas.grid(row=1, column=0, columnspan=3)
        # Buttons
        self.login_button = tk.Button(text="Login", command=self.user_want_to_login)
        self.login_button.grid(row=0, column=1, sticky=tk.E)
        self.register_button = tk.Button(text="Register", command=self.user_want_to_register)
        self.register_button.grid(row=0, column=2)
        self.mainloop()

    # def login_clicked_new(self):
    #     def login_clicked() -> None:
    #         username = str(username_entry.get())
    #         password = str(password_entry.get())
    #         if self.file_op.check_credentials(username, password):
    #             self.user_is_logged_in(str(username))
    #         else:
    #             messagebox.showinfo(title="Invalid credentials", message="Invalid credentials, forgot password?, "
    #                                                                      "maybe use it as red label popup")
    #     # Toplevel setup
    #     login_window = tk.Toplevel()
    #     login_window.title("Login")
    #     login_window.config(padx=20, pady=20, bg=THEME_COLOR)
    #     # Entries
    #     username_entry = tk.Entry(login_window)
    #     username_entry.grid(row=0, column=1)
    #     password_entry = tk.Entry(login_window)
    #     password_entry.config(show="*")
    #     password_entry.grid(row=1, column=1)
    #     # Labels
    #     username_label = tk.Label(login_window, text="Username", fg="white", bg=THEME_COLOR)
    #     username_label.grid(row=0, column=0)
    #     password_label = tk.Label(login_window, text="Password", fg="white", bg=THEME_COLOR)
    #     password_label.grid(row=1, column=0)
    #     # Button
    #     login_window_button = tk.Button(login_window, text="Login", command=login_clicked)
    #     login_window_button.grid(row=2, column=1)





    # def register_clicked_new(self):
    #     def register_clicked():
    #         username = str(username_entry.get())
    #         password = str(password_entry.get())
    #         data = {
    #             "username": [f"{username}"],
    #             "password": [f"{password}"],
    #             "balance": [0.0]
    #         }
    #
    #         if len(username) <= 0 and len(password) <= 0:
    #             messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    #         else:
    #             self.file_op.register_user(data)
    #     # Toplevel setup
    #     register_window = tk.Toplevel()
    #     register_window.title("Deposit")
    #     register_window.config(padx=20, pady=20, bg=THEME_COLOR)
    #     # Entries
    #     username_entry = tk.Entry(register_window)
    #     username_entry.grid(row=0, column=1)
    #     password_entry = tk.Entry(register_window)
    #     password_entry.config(show="*")
    #     password_entry.grid(row=1, column=1)
    #     # Labels
    #     username_label = tk.Label(register_window, text="Username", fg="white", bg=THEME_COLOR)
    #     username_label.grid(row=0, column=0)
    #     password_label = tk.Label(register_window, text="Password", fg="white", bg=THEME_COLOR)
    #     password_label.grid(row=1, column=0)
    #     # Button
    #     register_window_button = tk.Button(register_window, text="Register", command=register_clicked)
    #     register_window_button.grid(row=2, column=1)

    def user_want_to_login(self):
        # this function destroys MainPage and opens LoggedInUser window.
        # When LoggedInUser is logged-out User is redirected to MainPage
        self.destroy()
        log = LoginPage()
        while log.login_page_is_up:
            continue
        o = MainPage()

    def user_want_to_register(self):
        # this function destroys MainPage and opens LoggedInUser window.
        # When LoggedInUser is logged-out User is redirected to MainPage
        self.destroy()
        reg = RegisterPage()
        while reg.register_page_is_up:
            continue
        o = MainPage()





