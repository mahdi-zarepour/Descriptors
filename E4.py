"""

    __set_name__


"""



# ---------
class One:
    def __set_name__(self, owner, name):
        # print(name) # name car
        self.attribute_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        instance.__dict__[self.attribute_name] = value

    def __delete__(self, instance):
        # del instance.__dict__[self.attribute_name]
        instance.__dict__[self.attribute_name] = None


class Person:
    name = One()
    car = One()

    def __init__(self, name, car):
        self.name = name
        self.car = car


p = Person("Mahdi", 'Cope')

print(p.name, p.car, sep='---')