# В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car.
# Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.


class Car:

    def __init__(self, color=None, type1=None, year=None):
        self.color = color
        self.type1 = type1
        self.year = year

    def launch(self):
        return f'Автомобиль {self.type1} {self.year} заведён'

    def disabling(self):
        return f'Автомобиль {self.type1} {self.year} заглушен'

    def release(self, rel):
        self.rel = rel
        if self.rel == self.year:
            print(f'Год выпуска {self.year}')
        else:
            print(f'Год выпуска {self.rel}')

    def vid(self, tp):
        self.tp = tp
        if self.tp == self.type1:
            print(f'Тип {self.type1}')
        else:
            print(f'Тип {self.tp}')

    def cr(self, cl):
        self.cl = cl
        if self.cl == self.color:
            print(f'Цвет {self.color}')
        else:
            print(f'Цвет {self.cl}')


toyota = Car('red', 'sedan', "2014")
print('Цвет ' + toyota.color + ' Тип ' + toyota.type1 + ' Год ' + toyota.year)

print(toyota.launch())
print('\n')
print(toyota.disabling())
print('\n')
print(toyota.release("2011"))
print('\n')
print(toyota.vid('хедж бек'))
print('\n')
print(toyota.cr('blue'))
