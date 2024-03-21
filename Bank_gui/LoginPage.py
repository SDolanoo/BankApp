import tkinter as tk
from tkinter import messagebox
from Bank_gui.bank_gui import BankGui, THEME_COLOR, FONT
from Bank_gui.LoggedInUser import LoggedInUser

class LoginPage(BankGui):

    def __init__(self):
        BankGui.__init__(self)
        self.login_page_is_up = True
        self.login_page_setup()

    def login_page_setup(self):
        self.title("BankApp")
        self.config(padx=20, pady=20, bg=THEME_COLOR)
        # Canvas
        self.main_canvas = tk.Canvas(width=200, height=200, bg="white")
        self.text = self.main_canvas.create_text(100, 100, width=190, text="Welcome to the login page", font=FONT)
        self.main_canvas.grid(row=1, column=0, columnspan=2)
        # Entries
        self.username_entry = tk.Entry()
        self.username_entry.grid(row=2, column=1)
        self.password_entry = tk.Entry()
        self.password_entry.config(show="*")
        self.password_entry.grid(row=3, column=1)
        # Labels
        self.username_label = tk.Label( text="Username", fg="white", bg=THEME_COLOR)
        self.username_label.grid(row=2, column=0)
        self.password_label = tk.Label(text="Password", fg="white", bg=THEME_COLOR)
        self.password_label.grid(row=3, column=0)
        # Button
        self.login_window_button = tk.Button(text="Login", command=self.login_clicked)
        self.login_window_button.grid(row=4, column=1)
        self.exit_button = tk.Button(text="Go back", command=self.go_back)
        self.exit_button.grid(row=0, column=1)
        #self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()

    def login_clicked(self):
        username = str(self.username_entry.get())
        password = str(self.password_entry.get())
        if self.file_op.check_credentials(username, password):
            self.user_is_logged_in(str(username))
        else:
            messagebox.showinfo(title="Invalid credentials", message="Invalid credentials, forgot password?, "
                                                                     "maybe use it as red label popup")

    def user_is_logged_in(self, username: str):
        # this function destroys MainPage and opens LoggedInUser window.
        # When LoggedInUser is logged-out User is redirected to MainPage
        self.destroy()
        log = LoggedInUser(user=username)
        while log.is_logged_in:
            continue
        o = LoginPage()

    def go_back(self):
        self.login_page_is_up = False
        self.destroy()

