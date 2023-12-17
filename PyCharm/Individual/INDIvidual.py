#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_sum_repr(n, sum_repr=[], start=1):
    if n == 0:
        # Если число N равно 0, то печатаем представление суммы.
        print(sum_repr)
        return

    for i in range(start, n + 1):
        if n - i >= 0:
            # Добавляем i к текущему представлению суммы.
            print_sum_repr(n - i, sum_repr + [i], i)


if __name__ == '__main__':
    n = int(input("Введите натуральное число N: "))
    print(f"Возможные представления числа {n} "
          f"в виде суммы других натуральных чисел:")
    print_sum_repr(n)




