class PasswordMismatch(Exception):
    pass


password = input("Input your password: ")


def check_password():
    password_input = input("Confirm your password: ")
    if password_input != password:
        raise PasswordMismatch("Passwords does not match")


try:
    check_password()
except PasswordMismatch as e:
    print(e)
