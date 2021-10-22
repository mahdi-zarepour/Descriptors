"""

    __delete__


"""



# ---------
class One:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

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
    name = One('name')

    def __init__(self, name):
        self.name = name


p = Person("Mahdi")
p.name = "Rose"

del p.name
print(p.name)
p.name = "Mahdi"
print(p.name)
