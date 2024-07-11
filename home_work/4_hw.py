# Задача 1.
# создайте класс прямоугольника:
# а. Атрибуты - прямоугольнику можно задать ширину и высоту
# б. Методы - реализуйте 2 метода:
# 1.1. расчет площади прямоугольника
# 1.2. расчет периметра прямоугольника
# в. создайте 3 объекта, рассчитайте площадь и периметр для каждого.
# Результаты выводить в консоль.
import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))

    def perimetr(self):
        return self.a + self.b + self.c


equilateral = Triangle(3, 3, 3)

isosceles = Triangle(7, 7, 3)

versatile = Triangle(7, 5, 3)

print('Площадь равностороннего треугольника = ', equilateral.area())
print('Периметр равностороннего треугольника = ', equilateral.perimetr())
print('\n')
print('Площадь равнобедренного треугольника = ', isosceles.area())
print('Периметр равнобедренного треугольника = ', isosceles.perimetr())
print('\n')
print('Площадь разностороннего треугольника = ', versatile.area())
print('Периметр разностороннего треугольника = ', versatile.perimetr())

# Задача 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия
# и печатать ответ.


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


primer = Math(3, 4)
print('Сумма равна', primer.addition())

primer = Math(5, 7)
print('Произведение равно', primer.multiplication())

primer = Math(5, 7)
print('Частное равно', primer.division())

primer = Math(5, 7)
print('Разность равна', primer.subtraction())

# Задача 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует "сайдбар" (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод.
# Метод возвращает текст “Клик по кнопке {ТЕКСТ КНОПКИ}”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки


class Button:
    def __init__(self, text, tipe="Кнопка", loc=None):
        self.text = text
        self.tipe = tipe
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'


textbox = Button("Text Box")
checkbox = Button("Check Box")
radiobutton = Button("Radio Button")
wtables = Button("Web Tables")
buttonsTwo = Button("Buttons")
links = Button("Links")
images = Button("Broken Links - Images")
upload = Button("Upload")
download = Button("Download")
dynamic = Button("Dynamic Properties")
print('\n')
print('Кнопки')
print(textbox.text)
print(textbox.click())
print('\n')
print(checkbox.text)
print(checkbox.click())
print('\n')
print(radiobutton.text)
print(radiobutton.click())
print('\n')
print(wtables.text)
print(wtables.click())
print('\n')
print(buttonsTwo.text)
print(buttonsTwo.click())
print('\n')
print(links.text)
print(links.click())
print('\n')
print(images.text)
print(images.click())
print('\n')
print(upload.text)
print(upload.click())
print('\n')
print(download.text)
print(download.click())
print('\n')
print(dynamic.text)
print(dynamic.click())
