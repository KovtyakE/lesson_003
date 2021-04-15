# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 1
summary_expenses = expenses
while month in range(10):
    month += 1
    next_expenses = expenses * 0.03
    expenses += next_expenses
    summary_expenses += expenses
    print(round(summary_expenses, 2))
print(round(summary_expenses, 2))
result = summary_expenses - educational_grant * 10 + 0.01
print('Студенту нужно попросить', round(result, 2), 'рублей')
