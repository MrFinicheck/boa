#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from timeit import timeit

# Выполнение функций без использования интроспекции стека.


def factorial(n):
    # Функция для вычисления факториала.
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    # Функция для чисел фибоначчи.
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

# Выполнение функций с использованием интроспекции стека.


def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    else:
        return factorial_tail(n - 1, acc * n)


def fib_tail(n, a=0, b=1):
    if n == 0:
        return a
    else:
        return fib_tail(n - 1, b, a + b)


if __name__ == "__main__":
    # Вводим натуральное число N.
    n = int(input("Введите любое число "
                  "натуральное число N: "))

    # Импортуруем декоратор для функций fib и factorial.
    setup1 = """from __main__ import fib_tail"""
    setup2 = """from __main__ import factorial_tail"""

    # Используем модуль timeit для функции fib.
    timer = timeit(stmt=f'fib_tail({n})',
                   number=100,
                   setup=setup1)

    print(f'Время выполнения рекурсивной функции '
          f'fib с хвостовыми вызовами: '
          f'{timer}')

    # Используем модуль timeit для функции factorial.
    timer = timeit(stmt=f'factorial_tail({n})',
                   number=100,
                   setup=setup2)

    print(f'Время выполнения рекурсивной функции '
          f'factorial с хвостовыми вызовами: '
          f'{timer}')






