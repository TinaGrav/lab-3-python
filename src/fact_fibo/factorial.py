def factorial(n):
    res = 1
    if n < 0:
        raise ValueError("ValueError: negative number for factorial\n Введите другое число, перезапустив программу")
    elif n > 50000:
        raise ValueError("ValueError: the number is too big for factorial\n Введите другое число, перезапустив программу")
    else:
        for nelement in range(1, n + 1):
            res *= nelement
    return res

def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("ValueError: negative number for factorial\n Введите другое число, перезапустив программу")
    elif n > 995:
        raise ValueError("ValueError: the number is too big for recursive factorial\n Введите другое число, перезапустив программу")
    elif n == 1 or n == 0:
        return 1
    else:
        res = n * factorial_recursive(n-1)
        return res
