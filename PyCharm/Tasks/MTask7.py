#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import timeit
from functools import lru_cache

import sys


# Выполнение функций без использования декоратора.


def factorial_iterable(n):
    # Итеративная версия функции factorial.
    multiply = 1
    while n > 1:
        multiply *= n
        n -= 1
    return multiply


def fib_iterable(n):
    # Итеративная версия функции fib.
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


# Выполнение функций с использованием декоратора.


@lru_cache
def factorial_recursion(n):
    # Рекурсивная версия функции factorial.
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)


@lru_cache
def fib_recursion(n):
    # Рекурсивная версия функции fib.
    if n == 0 or n == 1:
        return n
    else:
        return (fib_recursion(n - 2) +
                fib_recursion(n - 1))


if __name__ == "__main__":
    # Вводим натуральное число N.
    n = int(input("Введите любое число "
                  "натуральное число N: "))

    # Импортуруем декоратор для функций fib и factorial.
    setup1 = """from __main__ import fib_recursion"""
    setup2 = """from __main__ import factorial_recursion"""

    # Используем модуль timeit для функции fib.
    timer = timeit(stmt=f'fib_recursion({n})',
                   number=100,
                   setup=setup1)

    print(f'Время выполнения рекурсивной функции '
          f'fib c @lru_cache: '
          f'{timer}')

    # Используем модуль timeit для функции factorial.
    timer = timeit(stmt=f'factorial_recursion({n})',
                   number=100,
                   setup=setup2)

    print(f'Время выполнения рекурсивной функции '
          f'factorial с @lru_cache: '
          f'{timer}')
