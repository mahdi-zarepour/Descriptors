"""

    __dict__
    Descriptor __get__

"""



# -------- __dict__

# class Person:
#     def __init__(self, name, car):
#         self.name = name
#         self.car = car



# print(Person.__dict__) # {'__module__': '__main__', '__init__': <function Person.__init__ at 0x7f97cc4c31f0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}


# p = Person('Mahdi', 'genessis')
# print(p.__dict__) # {'name': 'Mahdi', 'car': 'genessis'}
# print(p.__dict__['name']) # Mahdi

# --------



# -------- Descriptor __get__

class One:
    def __get__(self, instance, owner):
        return instance


class Person:
    name = One()



p = Person()

print(Person.name)