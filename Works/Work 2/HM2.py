import numpy as np


def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)

    integral = (h / 3) * (fx[0] + 4 * sum(fx[1:-1:2]) + 2 * sum(fx[2:-2:2]) + fx[-1])
    return integral


def area_between_curves(x):
    return (3 * x ** 2 - 2 * x) - (-x ** 2 + 6 * x)


if __name__ == "__main__":
    x1, x2 = 5, 7

    # Определяем пределы y для метода Монте-Карло
    x_samples = np.linspace(x1, x2, 1000)
    y_upper = 3 * x_samples ** 2 - 2 * x_samples
    y_lower = -x_samples ** 2 + 6 * x_samples
    y1, y2 = min(y_lower), max(y_upper)

    n = int(input("Введите количество точек N: "))
    print()

    # Вычисление методом Симпсона
    simp_area = simpson_rule(area_between_curves, x1, x2, n)

    print(f"Площадь методом Симпсона: {simp_area:.6f}")