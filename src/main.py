from fact_fibo.factorial import factorial
from fact_fibo.factorial import factorial_recursive
from fact_fibo.fibonacci import fibo
from fact_fibo.fibonacci import fibo_recursive
from sorts.bubble_sort import bubble_sort
from sorts.quick_sort import quick_sort
from sorts.counting_sort import counting_sort
from sorts.radix_sort import radix_sort
from sorts.bucket_sort import bucket_sort
from sorts.heap_sort import heap_sort
from class_stack import Stack
print("Привет!^_^")
command = input("Введите команду, которую хотите реализовать: factorial, fibonacci, sort или stack: ")
while True:
    if command not in ["factorial", "fibonacci", "sort", "stack"]:
        command = input("Неверная команда, попробуйте ещё раз: ")
        break
    else:
        break
if command == "factorial":
    fact = input("Хотите посчитать рекурсивно? Введите да или нет: ")
    while True:
        if fact == "да" or fact == "нет":
            number = int(input("Введите число, факториал которого хотите узнать: "))
            if fact == "да":
                print(factorial_recursive(number))
                print("Если хотите продолжить использовать программу, запустите её ещё раз :)")
                break
            else:
                print(factorial(number))
                print("Если хотите продолжить использовать программу, запустите её ещё раз :)")
                break
        else:
            fact = input("Ошибка ввода. Введите да или нет: ")

elif command == "fibonacci":
    fact = input("Хотите посчитать рекурсивно? Введите да или нет: ")
    while True:
        if fact == "да" or fact == "нет":
            number = int(input("Введите номер числа Фибоначчи, которое хотите узнать: "))
            if fact == "да":
                print(fibo_recursive(number))
                print("Если хотите продолжить использовать программу, запустите её ещё раз :)")
                break
            else:
                print(fibo(number))
                print("Если хотите продолжить использовать программу, запустите её ещё раз :)")
                break
        else:
            fact = input("Ошибка ввода. Введите да или нет: ")

elif command == "sort":
    method = input("Какой метод сортировки вы хотите использовать: bubble, quick, counting, radix, bucket или heap? ")
    while True:
        if method not in ["bubble", "quick", "counting", "radix", "bucket", "heap"]:
            method = input("Введите название метода сортировки: ")
            break
        else:
            break
    numbers = list(map(int, input("Введите через пробел числа, которые хотите отсортировать: ").split()))
    if method == "bubble":
        print(bubble_sort(numbers))
    elif method == "quick":
        print(quick_sort(numbers))
    elif method == "counting":
        print(counting_sort(numbers))
    elif method == "radix":
        print(radix_sort(numbers))
    elif method == "bucket":
        print(bucket_sort(numbers))
    else:
        print(heap_sort(numbers))
    print("Если хотите продолжить использовать программу, запустите её ещё раз :)")

elif command == "stack":
    stack = Stack()
    print("Создан пустой стек. Вы можете использовать для него команды push, pop, peek, is_empty, len и min. Вводите команды одну за одной. Для выхода из стека введите exit")

    while True:
        input_command = input("Введите команду: ")
        if input_command not in ["push", "pop", "peek", "is_empty", "len", "min", "exit"]:
            print("Ошибка, попробуйте ещё раз")
        else:
            if input_command == "push":
                input_number = int(input("Введите число: "))
                stack.push(input_number)
                print("the element was pushed")
            elif input_command == "pop":
                stack.pop()
                print("The element was popped")
            elif input_command == "peek":
                print(stack.peek())
            elif input_command == "is_empty":
                print(stack.is_empty())
            elif input_command == "len":
                print(stack.__len__())
            elif input_command == "min":
                print(stack.min())
            elif input_command == "exit":
                print("Если хотите продолжить использовать программу, запустите её ещё раз :)")
                break
