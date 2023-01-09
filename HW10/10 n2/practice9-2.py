from time import time
from functools import lru_cache

def process_timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


@process_timer
@lru_cache(maxsize=1000)
def fib(num: int) -> int:
    """
    The nth sentences of fib series.
    :param num:
    :return:
    """
    sent_1 = 0
    sent_2 = 1
    if num == 1:
        return sent_1
    elif num == 2:
        return sent_2
    elif num > 2:
        num -= 1
        return fib(num) + fib(num-1)


def fib_sent(num: int):
    """
    return n first sentences of fibo.
    :param num:
    :return:
    """
    for i in range(1, num+1):
        print ( f"sent[{i}]: {fib(i)}")


@process_timer
@lru_cache(maxsize=1000)
def fact(num):
    s = 1
    if num in [0, 1]:
        return s
    elif num > 1:
        return num*fact(num-1)


fact(250)
#fib(20)





