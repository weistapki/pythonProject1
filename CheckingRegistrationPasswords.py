registered_users = {
    "Alice": "C00peR",
    "Bob": "uNc1e",
    "Carl": "ClariNet"
}
def login_user():
    password = input("Enter your password, please: ")

    for username, registered_password in registered_users.items():
        if password == registered_password:
            print(f"Welcome, {username}! It's nice to see you again")
            return

    print("Sorry, I don't know you")
login_user()
