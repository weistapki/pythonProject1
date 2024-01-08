from random import randint

# Функція для генерації випадкових паролів
def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result

# Функція для перевірки надійності паролю
def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num

# Функція для отримання надійного паролю
def get_password():
    max_attempts = 100
    attempts = 0

    while attempts < max_attempts:
        password = get_random_password()

        if is_valid_password(password):
            return password

        attempts += 1

    return "Не вдалося згенерувати надійний пароль після {} спроб".format(max_attempts)

# Перевірка роботи функції get_password
generated_password = get_password()
print(generated_password)
