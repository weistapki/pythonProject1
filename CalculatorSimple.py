result = None
operand = None
operator = None
wait_for_number = True

while True:
    if operator == '=':
        print(f"Result: {result}")
        break
    elif wait_for_number == True:
        while True:
            try:
                operand = float(input("Enter number: "))
            except ValueError:
                print("Oops! It is not a number. Try again.")
            else:
                if result == None:
                    result = operand
                else:
                    if operator == '+':
                        result = result + operand
                    elif operator == '-':
                        result = result - operand
                    elif operator == '*':
                        result = result * operand
                    elif operator == '/':
                        result = result / operand
                break
        wait_for_number = False
    else:
        while True:
            operator = input("Enter one of operators +, -, *, /, =: ")
            if operator in ('+', '-', '*', '/', '='):
                break
            else:
                print("Oops! It is not a valid operator. Try again.")
        wait_for_number = True