class PasswordChecker:
    def __init__(self):
        self.users = {
            "Alice": "C00peR",
            "Bob": "uNc1e",
            "Carl": "ClariNet"
        }

    def check_password(self, password):
        for user_name, user_password in self.users.items():
            if password == user_password:
                return user_name
        raise Exception("Unknown user")

    def add_user(self, user_name, user_password):
        self.users.update({user_name: user_password})

    def remove_user(self, user_name):
        self.users.pop(user_name)