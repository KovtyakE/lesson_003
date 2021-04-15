# -*- coding: utf-8 -*-

from random import randint

import simple_draw as sd

sd.background_color = (0, 0, 0)
sd.set_screen_size(1500, 750)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
def smile(x, y, color):
    point = sd.Point(x, y)
    sd.circle(point, 50, color, 3)
    nose_left = sd.Point(x - 6, y - 5)
    nose_right = sd.Point(x + 6, y - 5)
    sd.circle(nose_left, 5, color, 2)
    sd.circle(nose_right, 5, color, 2)
    nose_ellipse_left = sd.Point(x - 15, y - 15)
    nose_ellipse_right = sd.Point(x + 15, y + 5)
    sd.ellipse(nose_ellipse_left, nose_ellipse_right, color, 2)
    eye_left = sd.Point(x - 20, y + 20)
    eye_right = sd.Point(x + 20, y + 20)
    sd.circle(eye_left, 10, color, 3)
    sd.circle(eye_right, 10, color, 3)
    mouth_left = sd.Point(x - 25, y - 20)
    mouth_right = sd.Point(x + 25, y - 20)
    sd.line(mouth_left, mouth_right, color, 3)
    ear_left = sd.Point(x - 50, y + 50)
    ear_right = sd.Point(x + 50, y + 50)
    sd.circle(ear_left, 25, color, 3)
    sd.circle(ear_right, 25, color, 3)

for _ in range(10):
    color = sd.random_color()
    horiz = randint(50, 1450)
    vertic = randint(50, 700)
    smile(horiz, vertic, color)

sd.pause()
