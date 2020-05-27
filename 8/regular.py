import re

email = input("Введите свою почту: ")


def emailvalid(email):
    result = re.match(r"[\w\.]+@\w+\.\w+", email)
    assert result
    return result.group(0)


try:
    print(emailvalid(email))
except AssertionError:
    print("Ошибка ввода!")