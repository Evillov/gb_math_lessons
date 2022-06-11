import math

import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import itertools


# TODO: /
#  1. Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).

def go_roulette(counter: int, mode: str, num=-1) -> int:
    zero = "Zero"
    times = int()

    for i in range(0, counter):
        rand = np.random.randint(0, 36)
        if mode == "print_mode":
            print(f"You got {rand if rand != 0 else zero} on the table!")

        if (mode == "tick") and (num == rand):
            times += 1
    if mode == "tick":
        return times if times != 0 else "no values"


# 2.
# TODO: /
#  2.1 Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или подбрасывания монетки.
# TODO: /
#  2.2 Сгенерируйте десять выборок случайных чисел х0, …, х9. /
#  и постройте гистограмму распределения случайной суммы  +х0+ …+ х 9.
def task_2_1():
    """
    Теорема сложения. Вероятность выпадения "8" или "12" = 1/37 + 1/37 = 2/37.
    """
    tryies = 10000
    result_8 = go_roulette(tryies, 'tick', 8)
    result_12 = go_roulette(tryies, 'tick', 12)

    print(result_8 if result_8 else "no result")
    print(result_12 if result_12 else "no result")
    print(
        f"Вероятность выпадения {1 / 37}. По т.сложения 8 и 12 = {1 / 37 + 1 / 37} . "
        f"\n Из опытов:"
        f"\n для 8 {result_8 / tryies}, "
        f"\n для 12 {result_12 / tryies}, "
        f"\n вероятность 2х событий по т.сложения из опытов = {(result_8 + result_12) / tryies}")


def task_2_2():
    sum = []

    for i in range(0, 10):
        x = reduce(lambda x, y: x + y, np.random.randint(0, 100, size=10))
        sum.append(x)

    num_bins = 10
    n, bins, patches = plt.hist(sum, num_bins)

    plt.show()


# 3.
# Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через биномиальное распределение)
# и сравните результаты.
# Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности из n независимых испытаний, взяв другие значения n и k.

def task_3_1():
    k, n = 0, 10
    a = np.random.randint(0, 2, n)
    b = np.random.randint(0, 2, n)
    c = np.random.randint(0, 2, n)
    d = np.random.randint(0, 2, n)

    x = a + b + c + d
    for i in range(0, n):
        if x[i] == 2:  # считаем сколько колько раз выпало "2"
            k = k + 1

    p = k / n  # вероятность выпадения 2 при 4 испытаниях по 10 подбросов

    print(f"Вероятность 2 при 4х испытаниях с 10 исходами: {p}")

    # Общая формула Бернулли Pn(k) = Cnk * p^k * q^(n-k).
    # Cnk = n! / k!*(n-k)! - Коэффициент
    # k = 5  # успехов
    n = 10  # исходов
    Cnk = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    print(f"Cnk = {Cnk}")

    Pnk = Cnk * (1 / (2 ** n))

    print(f"Pnk = {Pnk}")


#***********************************************************************************************************************

if __name__ == "__main__":
    task_n = input("Task n:")
    if (task_n == "1"):
        go_roulette(10, "print_mode")
    elif task_n == "2.1":
        task_2_1()
    elif task_n == "2.2":
        task_2_2()
    elif task_n == "3.1":
        task_3_1()
