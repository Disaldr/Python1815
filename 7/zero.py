while True:
    first = input("Введите делимое или q:\n")
    if first == "q":
        exit(0)
    second = input("Введите делитель или q:\n")
    if second == "q":
        exit(0)
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("Алло!? На ноль делить нельзя!")
    except ValueError:
        print("Вы ввели не число")
    else:
        print(answer)
    finally:
        print("Спасибо за использование сервиса.")