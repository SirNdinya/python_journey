def factorial():
    prompt = 'Enter an integer to find the factorial: '

    number = int(input(prompt))

    control = 1
    fact = 1
    while control <= number:
        fact = fact * control
        control = control + 1

    return fact


print(int(factorial()))

