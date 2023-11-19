

def break_password():
    length = int(input("Please, input password length: "))
    symbols_count = int(input("Please, input password alphabet quantity: "))
    speed = int(input("Please, input password cracking productivity: "))

    total_combinations = symbols_count ** length
    seconds = total_combinations / speed

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    months, days = divmod(days, 30)  # Приблизна кількість днів у місяці
    years, months = divmod(months, 12)  # Приблизна кількість місяців у році



    result_text = f"The password cracking is expected in {years} years {months} months {days} days {hours} hours {minutes} minutes {seconds} seconds"
    print(result_text)  # Вивід у термінал

# Виклик функції для вводу даних і виведення результату
break_password()
