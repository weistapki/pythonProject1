message = input("Enter a message: ")
offset = int(input("Enter the offset: "))

encoded_message = ""

for ch in message:
    if ch.isalpha():
        shift = 0

        if ch.islower():
            shift = ord('a')
        elif ch.isupper():
            shift = ord('A')

        encoded_char = chr((ord(ch) - shift + offset) % 26 + shift)
        encoded_message += encoded_char
    elif ch.isdigit():  # Додана перевірка на цифру
        shift = 0
        encoded_message += chr((ord(ch) - shift + offset) % 10 + shift)  # Шифрування цифри
    else:
        encoded_message += ch

print("Encoded message:", encoded_message)
