from functools import lru_cache
import time

def process_timer(fibonacci):
    def inner_function(n):
        t1=time.time()
        fibonacci(n)
        t2=time.time()
        return t2-t1
    return inner_function

@process_timer
@lru_cache(maxsize = None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f'process time: {fibonacci(300)} sec')