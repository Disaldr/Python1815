day = input()

try:
    if int(day) > 31:
        raise ValueError("Такой даты не может быть")
except ValueError as msg:
    print("ОШИБКА!", msg )
except ZeroDivisionError as msg:
    print("ОШИБКА!", msg )
else:
    print(day)
