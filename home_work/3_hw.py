# Задача 2.
# Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.
def max_numb(numb1, numb2):
    return max(numb1, numb2)
print(max_numb(4, 1))


# Задача 3.
# Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135,
# иначе вывести на экран “No”
def f_yes_no(x, y):
    if x-y == 135 or x-y == -135:
        print('yes')
    else:
        print('No')
f_yes_no(-135, 0)


# Задача 4.
# Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)
def season(mon: int):
    if mon == 12 or mon == 1 or mon == 2:
        print('Зима')
    elif mon in range(3, 6):
        print('Весна')
    elif mon in range(6, 9):
        print('Лето')
    elif 9 <= mon <= 11:
        print('Осень')
    else:
        print('Введите номер месяца от 1 до 12')
season(2)


# Задача 5.
# Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”;
def task_yes_no(x, y, z):
    if x > 10 and y > 10 and z > 10:
        print('yes')
    else:
        print('no')
task_yes_no(25, 19, 13)


# Задача 6.
# Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.
def summ_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        if elem > 0:
            result += 1
        elif elem < 0:
            result += 0
    return result
print(summ_list([1, -11, 3, 4, 5]))


# Задача 7. Функция на вход получает 2 переменные.
# 1. Кол-во лет (int)
# 2. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.


def summ_day(years: int, months: int):
    return ((years*12)*29)+(months*29)
print(summ_day(2, 1))
