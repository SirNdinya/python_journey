
class GuessTooBig(Exception):
    pass


class GuessTooSmall(Exception):
    def __int__(self, message, value):
        self.message = message
        self.value = value


magic_number = 2582


def guess_number():
    guess = int(input("Guess the magic number: "))
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
