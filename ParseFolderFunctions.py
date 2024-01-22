from pathlib import Path

def parse_folder(path):
    files = []
    folders = []

    # Перевіряємо, чи існує заданий шлях та чи є це директорія
    if path.is_dir():
        # Проходимося по вмісту директорії
        for item in path.iterdir():
            # Перевіряємо, чи є це файл чи директорія
            if item.is_file():
                files.append(item.name)
            elif item.is_dir():
                folders.append(item.name)

    # Створюємо кортеж із двох списків
    result_tuple = (files, folders)
    return result_tuple

# Приклад використання:
directory_path = Path("/шлях/до/вашої/директорії")
result = parse_folder(directory_path)

if result is not None:
    print(result)
