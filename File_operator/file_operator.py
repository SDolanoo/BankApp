import pandas as pd
from pandas import DataFrame

FILE_PATH = "C:\\Users\\Dolan\\OneDrive - Wojskowa Akademia Techniczna\\Pulpit\\InWorkBankApp\\File_operator\\data.csv"

class FileOperator:

    def __init__(self):
        self.create_database()
        self.existing_csv = pd.read_csv(FILE_PATH)

    def create_database(self):
        admin_data_for_creation_only = {
            "username": ["Admin"],
            "password": ["VeryStrongPassword"],
            "balance": [999.0]
        }

        try:
            self.existing_csv = pd.read_csv(FILE_PATH)
        except FileNotFoundError:
            new_csv = pd.DataFrame(admin_data_for_creation_only)
            new_csv.to_csv(FILE_PATH)

    def register_user(self, new_user_data: dict) -> None:
        new_data = pd.DataFrame(new_user_data)
        self.existing_csv = pd.concat([self.existing_csv, new_data], ignore_index=True)
        self.existing_csv.to_csv(FILE_PATH, index=False)

    def check_balance(self, username: str):
        user_index = self.existing_csv.index.get_loc(
        self.existing_csv[self.existing_csv["username"] == f"{username}"].index[0])
        user_balance = self.existing_csv.loc[user_index, "balance"]
        print(user_balance)

    def check_credentials(self, username: str, password: str) -> bool:
        if (self.existing_csv["username"].isin([f"{username}"])).any():
            user_index = self.existing_csv.index.get_loc(
                self.existing_csv[self.existing_csv["username"] == f"{username}"].index[0])
            correct_password = self.existing_csv.loc[user_index, "password"]
            if str(correct_password) == password:
                return True
            else:
                print("invalid password")
        else:
            print("Invalid credentials")

    def add_balance(self, username: str, amount: float) -> None:
        self.existing_csv.loc[self.existing_csv["username"] == f"{username}", "balance"] = self.existing_csv["balance"] + amount
        self.existing_csv.to_csv(FILE_PATH, index=False)

    def minus_balance(self, username: str, amount: float) -> None:
        self.existing_csv.loc[self.existing_csv["username"] == f"{username}", "balance"] = self.existing_csv["balance"] - amount
        self.existing_csv.to_csv(FILE_PATH, index=False)

    def update_password(self, username: str, new_password: str) -> None:
        self.existing_csv.loc[self.existing_csv["username"] == f"{username}", "password"] \
                = f"{new_password}"
        self.existing_csv.to_csv(FILE_PATH, index=False)

    def get_all_users(self) -> list:
        return [i for i in self.existing_csv["username"]]


#file_op = FileOperator()
#var = file_op.existing_csv
#print(var)
# file_op.register_or_create_user(data)
#file_op.add_balance("Dolan", 190.9)
# file_op.minus_balance("Dubi", 190.9)
# file_op.update_password("Dubi", "XDDD")
# if file_op.check_credentials("Dolan", "123"):
#     print("dobrze się stało")
# else:
#     print("też dobrze bo nie przeszło")
# file_op.get_all_users()
#file_op.check_balance("Admin")
