from tools import add

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return self.name

person_1 = Person("Heike", 33)
person_2 = Person("Uwe", 54)
person_3 = Person("Mathilde", 77)

personen_alter = add(person_1.age, person_2.age, person_3.age)
print(personen_alter)

class Vehicle:
    def __init__(self, wheels, engine):
        self.wheels = wheels
        self.engine = engine
