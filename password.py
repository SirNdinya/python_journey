class PasswordMismatch(Exception):
    pass


class UpperCaseInPassword(Exception):
    pass


class LowerCaseInPassword(Exception):
    pass


class IntegerInPassword(Exception):
    pass


class SymbolInPassword(Exception):
    pass


create_password = input("Create a strong password: ")


def check_combinations():
    for i in create_password:
        if i[i+1] != i.upper():
            raise UpperCaseInPassword("Password must contain at least one upper case letter")
        if i[i+2] != i.lower():
            raise LowerCaseInPassword("Password must contain at least one lower case letter")
        if i[i+3] != i.integer():
            raise IntegerInPassword("Password must contain at least one number")
        if i[i+4] != '.' or i != '@' or i != '/' or i != ',' or i != '!' or i != '#' or i != '$' or i != '%' or i != '&':
            raise SymbolInPassword("Password must contain at a symbol")


def password_checker():
    confirm_password = input("Confirm password: ")
    if confirm_password != create_password:
        raise PasswordMismatch("Passwords are not the same")
    else:
        print('Success')
