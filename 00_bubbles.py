# -*- coding: utf-8 -*-
import random
import simple_draw as sd

sd.resolution = (1600, 750)
center = sd.Point(150, 150)
rand_1 = int(random.randint(160, 250))
rand_2 = int(random.randint(1, 254))
rand_3 = int(random.randint(1, 5))

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
radius = 45
for i in range(3):
    radius += 5
    sd.circle(center, radius, color = (rand_1, rand_2, rand_3), width = 1)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 45
    for i in range(3):
        radius -= step
        sd.circle(center, radius, color=(rand_1, rand_2, rand_3), width=1)
bubble(point=center, step=5)

# Нарисовать 10 пузырьков в ряд
for x in range(100,1100,100):
    center = sd.Point(x,150)
    radius = 55
    for i in range(3):
        radius -= 5
        rand_1 = int(random.randint(160, 250))
        rand_2 = int(random.randint(1, 254))
        rand_3 = int(random.randint(1, 5))
        sd.circle(center, radius, color=(rand_1, rand_2, rand_3), width=1)

# Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 100):
    for x in range(100, 1100, 100):
        center = sd.Point(x, y)
        radius = 55
        for i in range(3):
            radius -= 5
            rand_1 = int(random.randint(160, 250))
            rand_2 = int(random.randint(1, 254))
            rand_3 = int(random.randint(1, 50))
            sd.circle(center, radius, color=(rand_1, rand_2, rand_3), width=1)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(1000):
    x = random.randint(0, 1600)
    y = random.randint(0, 750)
    center = sd.Point(x, y)
    radius = 55
    rand_1 = int(random.randint(1, 250))
    rand_2 = int(random.randint(1, 254))
    rand_3 = int(random.randint(1, 250))
    sd.circle(center, radius, color=(rand_1, rand_2, rand_3), width=1)

#
sd.pause()


