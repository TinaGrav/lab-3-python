import functools
def fibo(n: int) -> int:
    el_1 = 0
    el_2 = 1
    if n <= 0:
        raise ValueError("ValueError: negative number or zero for Fibonacci")
    if n > 500000:
        raise ValueError("ValueError: the number is too big for Fibonacci")
    for nelement in range(1, n):
        el_1, el_2 = el_2, el_1 + el_2
    return el_2

@functools.cache
def fibo_recursive(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    if n <= 0:
        raise ValueError("ValueError: negative number or zero for Fibonacci")
    if n > 500:
        raise ValueError("ValueError: the number is too big for recursive Fibonacci")
    res = fibo_recursive(n-1) + fibo_recursive(n-2)
    return res
print(fibo_recursive(500))