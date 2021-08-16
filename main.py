import json
import os

CWD = os.path.dirname(__file__)

class Auth:
    def __init__(self, db_path):
        if type(db_path) != str:
            raise ValueError("The db_path has to be an str instance")
        self.db_path = db_path
    
    @property
    def users(self):
        with open(self.db_path, "r", encoding="utf8") as file:
            return json.load(file)["data"]
    
    def create_user(self, user):
        if type(user) != dict:
            raise ValueError("The user has to be an dictionary instance")
        users = self.users.copy()
        users.append(user)
        with open(self.db_path, "w", encoding="utf8") as file:
            json.dump({"data": users}, file, ensure_ascii=False, indent=4)
    
    @staticmethod
    def create_form():
        user_name = input("Name: ")
        user_pwd = input("PWD: ")
        return {
            "user_name": user_name,
            "user_pwd": user_pwd
        }
    
    def login(self, user_to_log):
        if type(user_to_log) != dict:
            raise ValueError("The user has to be an dictionary instance")
        users = self.users.copy()
        user_exist = next(filter(lambda user: user["user_name"] == user_to_log["user_name"], users), False)
        if user_exist:
            return True if user_to_log["user_pwd"] == user_exist["user_pwd"] else False
    
    @staticmethod
    def login_form():
        user_name = input("Name: ")
        user_pwd = input("PWD: ")
        return {
            "user_name": user_name,
            "user_pwd": user_pwd
        }

test = Auth(f"{CWD}/users.json")
# test_user = test.create_form()
# test.create_user(test_user)
# print(test.login(test_user))
test_user = test.login_form()
print(test.login(test_user))