# пошук ключів у словнику за певним значенням:
def lookup_key(data, value):
    keys = []  # Створення порожнього списку для зберігання ключів
    for key, val in data.items():  # Цикл, що перебирає пари ключ-значення у словнику
        if val == value:  # Перевірка, чи значення відповідає шуканому значенню
            keys.append(key)  # Якщо так, то додаємо ключ до списку
    return keys  # Повертаємо список знайдених ключів


# Приклад використання:
programming_languages = {
    'Python': 1991,
    'Java': 1995,
    'JavaScript': 1995,
    'Ruby': 1995,
    'C++': 1985
}

result = lookup_key(programming_languages, 1995)
print(result)  # Виведе: ['Java', 'JavaScript', 'Ruby']