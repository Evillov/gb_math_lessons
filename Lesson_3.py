from functools import reduce

import numpy as np
import matplotlib.pyplot as plt
import math


def length_vector_1(vector: list) -> float:
    return math.sqrt(reduce(lambda x, y: x ** 2 + y ** 2, vector))


def show_linear_2():
    x = np.linspace(-5, 5, 20)
    y = 3 * x + 1
    y2 = (-1 / 3) * x + 1
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.ylim([-5, 5])
    plt.xlim([-5, 5])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def show_circle_3():
    x = np.linspace(-3, 3, 200000)
    y = np.sqrt(1 - x ** 2)
    y1 = -np.sqrt(1 - x ** 2)
    plt.plot(x, y)
    plt.plot(x, y1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def show_ellipse_3():
    x = np.linspace(-5, 5, 200000)
    y = np.sqrt(1 - x ** 2)
    y1 = -y

    y2 = np.sqrt(0.05 - (x ** 2 / 16))
    y3 = -y2

    plt.plot(x, y, color='red', label='Circle')
    plt.plot(x, y1, color='red')
    plt.plot(x, y2, color='blue', label="Ellipse")
    plt.plot(x, y3, color='blue')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.scatter(x=0, y=0, color="green", label='Center')
    plt.legend()
    plt.show()


def show_3d_planes_5():
    x = np.arange(-20, 20, 2)
    y = np.arange(-20, 20, 2)
    x, y = np.meshgrid(x, y)
    x1 = x+8
    y1 = y+8

    z = (x + y - 2) * 2
    z1 = z + 8

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_wireframe(x, y, z)
    ax.plot_wireframe(x1, y1, z1)

    plt.show()


def show_3d_2grade_surface():
    """
    Гиперболический параболоид
    :return:
    """
    x = np.arange(-10, 10, 0.5)
    y = np.arange(-10, 10, 0.5)
    x, y = np.meshgrid(x, y)

    z = x ** 2 - y ** 2
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_wireframe(x, y, z)
    plt.show()


if __name__ == "__main__":
    task_n = int(input("task_N:"))
    if task_n == 1:
        length_vector_1([1, 2, 3, 4, 5])
    elif task_n == 2:
        show_linear_2()
    elif task_n == 31:
        show_circle_3()

    elif task_n == 32:
        show_ellipse_3()
    elif task_n == 5:
        show_3d_2grade_surface()

    elif task_n == 51:
        show_3d_planes_5()

    print("Finish")
