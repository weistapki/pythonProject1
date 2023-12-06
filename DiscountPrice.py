def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)

    apply_discount()
    return price
price = 100
discount = 0.1
result =  discount_price(price, discount)
print(result)