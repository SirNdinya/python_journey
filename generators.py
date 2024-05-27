# Generators are functions that return value that can be iterated over
# they use yield keyword instead of return

def countdown(num):
    print('Starting')
    while num > 0:
        if num % 2 == 0:
            yield 'EVEN'
        else:
            yield 'ODD'
        num -= 1
    print('Finished!!')


cd = countdown(10)
while True:
    value = next(cd)
    print(value)
print("")
