from datetime import datetime, timedelta

registered_users = {}


def register_user():
    login = input("Введіть свій логін: ")
    password = input("Введіть ваш пароль: ")

    registered_users[login] = {
        'password': password,
        'registration_date': datetime.now()
    }

    print(f"Вітаю, {login}! Вас зареєстровано в системі! Не забудьте змінити пароль через 30 днів.")


def login_user():
    login = input("Введіть свій логін: ")
    password = input("Введіть ваш пароль: ")

    if login in registered_users and registered_users[login]['password'] == password:
        print(f"Вітаю, {login}! Вас зареєстровано в системі!")
    else:
        print("Неправильний логін або пароль.")


while True:
    option = input("Виберіть варіант: 1 - Зареєструватися, 2 - Увійти, q - Вийти: ")
    if option == '1':
        register_user()
    elif option == '2':
        login_user()
    elif option.lower() == 'q':
        break
    else:
        print("Недійсний варіант. Будь ласка спробуйте ще раз.")