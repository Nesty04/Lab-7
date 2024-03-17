# Бархоткина Анастасия 408226
import numpy as np
from time import perf_counter
from random import random
import matplotlib.pyplot as plt

def time_comparison():
    a = []
    b = []
    for i in range(10**6):
        a.append(random())
        b.append(random())

    np_a = np.array(a)
    np_b = np.array(b)

    mult = []
    start_time = perf_counter()
    for i in range(10**6):
        mult.append(a[i]*b[i])
    end_1 = perf_counter() - start_time

    start_time = perf_counter()
    np.multiply(np_a, np_b)
    end_2 = perf_counter() - start_time

    print(f'Время поэлементного перемножения стандартных списков - {end_1}\n'
          f'Время перемножения массивов NumPy - {end_2}\n'
          f'Перемножение массивов NumPy было проведено на {end_1 - end_2} быстрее')


def hist():
    data = np.genfromtxt('data2.csv', delimiter=',')
    arr = np.array(data[:,2])[1:]
    
    plt.figure(figsize=(5,5))

    plt.hist(arr, bins=20, color='blue', edgecolor='black')
    plt.title('Гистограмма')
    plt.xlabel('значения')
    plt.ylabel('частота')
    plt.grid()
    plt.show()

    plt.hist(arr, bins=20, density=True, color='blue', edgecolor='black')
    plt.title('Выровненная гистогрмма')
    plt.xlabel('значения')
    plt.ylabel('частота')
    plt.grid()
    plt.show()

    print(f'Среднеквадратичное отклонение - {np.std(arr)}')


def plot3d():
    xs = np.linspace(-1*np.pi, np.pi, 50)
    ys = 1 / xs
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, c='green')
    plt.title('3D-график')
    plt.show()

if __name__ == '__main__':
    time_comparison()
    hist()
    plot3d()




    