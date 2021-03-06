import matplotlib.pyplot as plt
import re

file = open('coordinate', 'r')  # r - открытие на чтение
strings = file.read()  # чтение всего содержимого из файла

for line in strings.split('\n'):  # разделения файла на строки
    x, y = (re.split('\s+', line))
    x = float(x)  # вещественные числа
    y = float(y)
    plt.scatter(x, y, color='black')
plt.xlabel('X', fontsize=10)
plt.ylabel('Y', fontsize=10)
plt.title('График значений', fontsize=20)
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.show()

# пока line принадлежит lines.split('\n'), это разделения файла на строки.
# x, y = re(регулярные выражения).split(разделить строку)('\s+'(до какого угодно числа пробелов),
# line (переменная которую надо разделить))
# разделяет на нескольк переменых, 1 из которых = x, 2 = у