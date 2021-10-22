"""

    __set__
    __get__, __set__ in real code
    
"""



# -------- __set__

# class One:
#     def __get__(self, instance, owner):
#         return instance

#     def __set__(self, instance, value):
#         print(instance, value, sep='------')


# class Person:
#     name = One()


# p = Person()
# p.name = "Mahdi"

# --------



# -------- Descriptors in real code

class One:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")

        instance.__dict__[self.attribute_name] = value


class Person:
    name = One('name')

    def __init__(self, name):
        self.name = name


p = Person("Mahdi")
p.name = "Rose"
print(p.name)