import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 10, 1)  # 0,1,2,3,4,5,6,7,8,9
y = x**2 - 5*x + 6

plt.figure(facecolor='lightblue')
plt.title("Joonise pealkiri")  # Название графика
plt.xlabel("x telg")           # Подпись оси X
plt.ylabel("y telg")           # Подпись оси Y
plt.grid(True)                 # Сетка на графике
plt.plot(x, y, color='blue', linestyle='-', marker='D', markersize=8, label="Joonise joon")
plt.legend()
plt.show()



x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [16, 9, 4, 1, 0]

plt.figure()
plt.plot(x, y1, linestyle='-', marker='o', color='blue',
         markersize=8, markerfacecolor='lightblue', label="Tõusev joon")
plt.plot(x, y2, linestyle='--', marker='x', color='green',
         markersize=8, label="Laskuv joon")

plt.title("Kahe joone näide")  # Название
plt.xlabel("x telg")            # Ось X
plt.ylabel("y telg")            # Ось Y
plt.legend()
plt.grid(True)
plt.show()

plt.scatter(x, y1, color='blue', label="Tõusev joon")
plt.show
plt.title("Scatter-joonis")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.legend()
plt.grid(True)
plt.show()

#Кит
import numpy as np
import matplotlib.pyplot as plt

# Первая часть графика
x1 = np.linspace(0, 9, 100)
y1 = (2/27)*x1**3 - 3

# Вторая часть
x2 = np.linspace(-10, 0, 100)
y2 = 0.04*x2**2 - 3

# Третья часть
x3 = np.linspace(-9, -3, 100)
y3 = (2/9)*(x3+6)**2 + 1

# Четвертая часть
x4 = np.linspace(-3, 9, 100)
y4 = (-1/12)*(x4-3)**2 + 6

# Пятая часть
x5 = np.linspace(5, 8.5, 100)
y5 = (1/9)*(x5-5)**2 + 2

# Шестая часть
x6 = np.linspace(5, 8.5, 100)
y6 = (1/9)*(5-x6)**2 + 1.5

# Седьмая часть
x7 = np.linspace(-13, -9, 100)
y7 = -0.75*(x7+11)**2 + 6

# Восьмая часть
x8 = np.linspace(-15, -10, 100)
y8 = -0.5*(x8+13)**2 + 3

# Девятая часть (прямая линия)
x9 = np.linspace(3, 4, 100)
y9 = np.full_like(x9, 3)

# Настройка окна
plt.figure(figsize=(12, 7), facecolor='lightgreen')  # Задний фон — зеленый

# Фон области графика
ax = plt.gca()
ax.set_facecolor('lightblue')  # Фон области графика — голубой

# Рисуем графики
plt.plot(x1, y1, 'bo-', markersize=5)
plt.plot(x2, y2, 'bo-', markersize=5)
plt.plot(x3, y3, 'bo-', markersize=5)
plt.plot(x4, y4, 'bo-', markersize=5)
plt.plot(x5, y5, 'bo-', markersize=5)
plt.plot(x6, y6, 'bo-', markersize=5)
plt.plot(x7, y7, 'bo-', markersize=5)
plt.plot(x8, y8, 'bo-', markersize=5)
plt.plot(x9, y9, 'bo-', markersize=5)

# Названия и сетка
plt.title("Vaal", fontsize=20)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Показать график
plt.show()