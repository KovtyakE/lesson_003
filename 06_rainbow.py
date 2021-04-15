# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
sd.background_color = (122, 122, 122)
sd.set_screen_size(1500, 750)
# x_1 = 45
# x_2 = 345
# for color in rainbow_colors:
#     x_1 += 5
#     x_2 += 5
#     point_1 = sd.Point(x_1, 50)
#     point_2 = sd.Point(x_2, 450)
#     sd.line(point_1, point_2, color, 4)
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.Point(750, -50)
radius = 750
for color in rainbow_colors:
    radius -=30
    sd.circle(point, radius, color, 30)

sd.pause()
