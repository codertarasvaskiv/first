class Cl1:
    def __init__(self):
        self.name = 'taras'


class Cl2(Cl1):
    def __init__(self):
        Cl1.__init__(self)
        self.age = 45


