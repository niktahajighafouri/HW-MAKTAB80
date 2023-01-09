from functools import lru_cache
import time

def process_timer(factorial):
    def inner_function(n):
        t1=time.time()
        result = factorial(n)
        t2=time.time()
        return t2-t1
    return inner_function

@process_timer
@lru_cache(maxsize = None)
def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ('Wrong number')
    else:
        return n * factorial(n - 1)

print(f'process time : {factorial(300)} sec')