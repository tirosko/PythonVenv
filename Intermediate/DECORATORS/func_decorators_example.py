# def start_end_decorator(func):

#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper


# def print_name():
#     print('Alex')


# print_name = start_end_decorator(print_name)
# print_name()
# ---------------------------------------
# proužitie dekorátora na funkciu
# @start_end_decorator

""" def start_end_decorator(func):

    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


# nie je potrebné volať dekorátor, je to automatické
# print_name = start_end_decorator(print_name)
print_name() """

# ---------------------------------------
# iný príklad s funkciou s argumentom


# def start_end_decorator(func):

#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x + 5

# # print_name = start_end_decorator(print_name)


# result = add5(10)
# print(result)

# print(help(add5))
# print(add5.__name__)
# print(add5.__doc__)
# ---------------------------------------
# oprava nesprávnym interpretovaním funkcie wrapper

# import functools


# def start_end_decorator(func):

#     @functools.wraps(func)  # Preserve the original function's metadata
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper


# @start_end_decorator
# def add5(x):
#     return x + 5

# # print_name = start_end_decorator(print_name)


# result = add5(10)
# print(result)

# -----------------------------------------

# import functools


# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, ** kwargs):
#             for _ in range(num_times):
#                 result = func(*args, ** kwargs)
#             return result
#         return wrapper
#     return decorator_repeat


# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')


# greet('Alex')

# ------------------------------------------
# Nested decorators - veľmi zložitý príklad, ale zaujímavý
#  ------------------------------------------

import functools


def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        print('Start')
        result = func(*args, ** kwargs)
        print('End')
        return result
    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, ** kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, ** kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello('Alex')
# ------------------------------------------
