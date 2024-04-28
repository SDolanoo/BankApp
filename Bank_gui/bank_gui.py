from File_operator.file_operator import FileOperator
import tkinter as tk
from tkinter import messagebox


THEME_COLOR = "#375362"
FONT = ("Arial", 20)


class BankGui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.file_op = FileOperator()
        self.set_menubar()

    def set_menubar(self):
        # setup of menubar for all pages
        menu_bar = tk.Menu(self)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.send_messagebox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menu_bar)

    def send_messagebox(self):
        messagebox.showinfo(title="About", message="This bank application is an application\n"
                                                   "created for learning purposes\n"
                                                   "the user can register or login\n"
                                                   "after login the user can do certain actions\n"
                                                   "such as transfering money between accounts\n"
                                                   "Created by SDolanoo")

#file = FileOperator()
#log = LoggedInUser(file, "Dolan")
