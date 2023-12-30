registered_users = {
    "Alice": "C00peR",
    "Bob": "uNc1e",
    "Carl": "ClariNet"
}


def check_password(password):
    for username, registered_password in registered_users.items():
        if password.lower() == registered_password.lower():
            return username
    return "Intruder"


def check_auth_code(expected_auth_code='1111'):
    auth_code = input("Enter authentication code, please: ")
    return auth_code == expected_auth_code


def login_user():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter your password, please: ")
        username = check_password(password)

        if username != "Intruder":
            if check_auth_code():
                print(f"Welcome, {username}! It's nice to see you again")
                return
            else:
                print("Sorry, I don't know you")
                return
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Sorry, password is invalid. {remaining_attempts} attempt(s) left.\nTry again!")
            else:
                print("Sorry, I don't know you")


login_user()