x = -10
if x < 0:
    raise Exception(" x should be positive")

i = -10
assert (x >= 0), 'i should be positive'

# --------->
try:
    d = 10 / 0
except:
    print('Error occurred')
# --------->
try:
    p = 100 / 0
except Exception as e:
    print(e)

# ------->
try:
    bb = 6 / 1
    # dd = 10/0
    # gg = 10 + '10'
    cc = bb * 10

except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("No errors occured")
finally:  # ====>>>  RUNS WHETHER AN ERROR IS MET OR NOT
    print("Successfull..")


#           DEFINING OWN EXCEPTIONS   #

class PasswordMismatch(Exception):
    pass


password = "@#Code_XVII!"


def check_password():
    password_input = input("Input your password")
    if password_input != password:
        raise PasswordMismatch("Passwords does not match")


try:
    check_password()
except PasswordMismatch as e:
    print(e)


# ============================================#

class GuessTooBig(Exception):
    pass


class GuessTooSmall(Exception):
    def __int__(self, message, value):
        self.message = message
        self.value = value


magic_number = 2582


def guess_number():
    guess = int(input("Guess the magic number"))
    if guess > magic_number:
        raise GuessTooBig("The guess is higher than the magic number")
    if guess < magic_number:
        raise GuessTooSmall("The guess is lower than the magic number", guess)


try:
    guess_number()
except GuessTooBig as e:
    print(e)
except GuessTooSmall as e:
    print(e.message, e.value)
