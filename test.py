import numpy as np


d = {1: 1, 0: 0}


def fib(n: int) -> int:
    if n in d:
        return d[n]
    num = fib(n - 1) + fib(n - 2)
    d[n] = num
    return num


print(fib(100))


