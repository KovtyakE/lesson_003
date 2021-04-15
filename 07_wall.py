# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.set_screen_size(1500, 750)
sd.background_color = (210, 105, 30)
# счетчик для определения сдвига, нужно ли сдвигать начало и конец вертикальной линии
count = 0
for y in range(-35, 800, 50):
    # левый край экрана
    point = sd.Point(0, y)
    # правый край экрана
    endpoint = sd.Point(1500, y)
    # рисуем горизонтальную линию
    sd.line(point, endpoint, color=(100, 100, 100), width=5)
    count += 1
    for x in range(-15, 1600, 100):
        # условие четности операции рисования линий относительно горизонтальной линии
        if count % 2 == 0:
            # если делится без остатка (кратно 2, чётное), то вертикальная линия без сдвигов
            point = sd.Point(x, y)
            endpoint = sd.Point(x, y + 50)
            sd.line(point, endpoint, color=(100, 100, 100), width=5)
        else:
            # если делится с остатком (нечётное), то сдвигаем начало и конец каждой линии на 50 по горизонтали (х)
            point = sd.Point(x + 50, y)
            endpoint = sd.Point(x + 50, y + 50)
            sd.line(point, endpoint, color=(100, 100, 100), width=5)

sd.pause()
