"""

    Property(getter), setter, deleter

"""

class Person:
    def __init__(self, name):
        self._name = name

    @property # getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        self._name = value

    @name.deleter
    def name(self):
        self._name = None



p = Person("Mahdi")
p.name = "Rose"
del p.name
print(p.name)