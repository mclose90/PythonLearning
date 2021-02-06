
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def IncrementAge(self):
        self.age += 1
    
class DeadPerson(Person):
    def __init__(self, name, age, dead):
        super().__init__(name, age)
        self.dead = dead

    @classmethod
    def Get(self, person, dead):
        dPerson = DeadPerson(person.name, person.age, dead)
        return dPerson