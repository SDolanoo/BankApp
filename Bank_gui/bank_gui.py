import tkinter as tk
from File_operator.file_operator import FileOperator

THEME_COLOR = "#375362"
FONT = ("Arial", 20)


class BankGui(tk.Tk):

    def __init__(self):
        super().__init__()
        self.file_op = FileOperator()




#file = FileOperator()
#log = LoggedInUser(file, "Dolan")
