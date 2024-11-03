import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Параметри для методу Монте-Карло
num_points = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, num_points)  # Генерація випадкових точок для x
y_random = np.random.uniform(0, max(f(x_random)), num_points)  # Генерація випадкових точок для y

# Обчислення площі методом Монте-Карло
under_curve = y_random < f(x_random)
area_estimate = (b - a) * max(f(x_random)) * np.sum(under_curve) / num_points

print("Наближене значення інтеграла методом Монте-Карло:", area_estimate)

# Перевірка точності з функцією quad
result, error = spi.quad(f, a, b)
print("Аналітичне значення інтеграла (quad):", result)
print("Абсолютна похибка:", abs(result - area_estimate))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.3)
ax.set_title("Графік інтегрування f(x) = x^2 від 0 до 2")

# Позначення випадкових точок на графіку
ax.scatter(x_random, y_random, s=1, color='blue', alpha=0.1)
plt.show()
