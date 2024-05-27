# Decorator allows a function to take in another function as an argument...and can return from another function

################DECORATOR TEMPLATE###############
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before.....
        result = func(*args, **kwargs)  ###The function
        # Do something after......
        return result

    return wrapper()


##################################################
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("Stop")

    return wrapper()


@start_end_decorator
def print_name():
    print("LUCKY")


# print_name = start_end_decorator(print_name)

print_name()

###############################################
import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("Stop")
        return result

    return wrapper()


@start_end_decorator
def add100(x):
    return x + 100


result = add100(400)
print(result)


#######################################################
#######################################################
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=10)
def greet(name):
    print(f'Hello {name}')


greet('LUCKY')
