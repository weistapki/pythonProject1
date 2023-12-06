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


def check_password_change(login):
    registration_date = registered_users[login]['registration_date']
    current_date = datetime.now()
    thirty_days_after_registration = registration_date + timedelta(days=30)

    if current_date > thirty_days_after_registration:
        print(f"Пройшло більше 30 днів з моменту реєстрації, {login}. Будь ласка, змініть свій пароль.")
    else:
        print("Не потрібно змінювати пароль поки що.")


def login_user():
    login = input("Введіть свій логін: ")
    password = input("Введіть ваш пароль: ")

    if login in registered_users and registered_users[login]['password'] == password:
        print(f"Вітаю, {login}! Ви увiшли в систему!")
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