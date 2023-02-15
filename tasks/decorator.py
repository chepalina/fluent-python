# Что выведет код
# supper-easy

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')


target()


# Декоратор времени выполнения функции
# Fluent Python. Chapter 7.

import time
from functools import wraps


def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = f"{name}({args}, {kwargs}) -> {elapsed}"
        return result

    return clocked