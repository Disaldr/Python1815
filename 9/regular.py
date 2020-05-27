import  re

password = input("Придумайте пароль:")

if re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[0-9a-zA-Z!@#$%^&*]{6,25}', password):
    print("Хороший пароль")
else:
    print("Плохой пароль")