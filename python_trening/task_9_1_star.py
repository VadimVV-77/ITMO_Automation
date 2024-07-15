class Input:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

# Создаем объекты классов


search = Input(' search ', ' поиск ')

click = Button(' click ', ' Клик ')

main = Title(' mein ', ' главный ')

sting = Link(' sting ', ' стинг ')

print(search.text + search.loc)
print('\n')
print(click.text + click.loc)
print('\n')
print(main.text + main.loc)
print('\n')
print(sting.text + sting.loc)
print('\n')
