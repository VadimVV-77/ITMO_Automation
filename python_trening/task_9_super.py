class A:
    def __init__(self, x):
                self.x = x




class B(A):

    def __init__(self, y):
        super().__init__(self.x)
        self.y = y
        y = x + 5


wd=B(x+5)
print(wd.y)
