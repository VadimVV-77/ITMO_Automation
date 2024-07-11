from task_9_checks import Checks


class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc


class Title(Checks):

    def __init__(self, text, loc):
        super().__init__()
        self.text = text
        self.loc = loc


class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

# Создаем объекты классов


search = Input(' search ', ' поиск ')

click = Button(' click ', ' Клик ')

main = Title(' mein ', ' главный ')

sting = Link(' sting ', ' стинг ')

# print(search.text + search.loc)
# print('\n')
# print(click.text + click.loc)
# print('\n')
# print(main.text + main.loc)
# print('\n')
# print(sting.text + sting.loc)
# print('\n')
print(search.check_text())
print(click.check_text())
print(main.check_text())
print(sting.check_text())
