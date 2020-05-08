def discount(product, amount):
    price = product['price'] * (1-amount)
    assert 0 <= price <= product["price"]
    return product['name'], price, price



keyboard = {"name": "Клавиатура У731", "price": 4000}

print(discount(keyboard, 5))