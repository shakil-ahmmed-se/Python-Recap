class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    pass

class Dog(Mammal):
    pass

dog1 = Dog()
dog1.walk()