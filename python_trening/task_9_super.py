class A:
    def __init__(self, x):
                self.x = x




class B(A):

    def __init__(self, y):
        super().__init__(x)
        self.y = y


wd=B(x+5)
print(wg.y)
