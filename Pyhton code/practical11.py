
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return ""

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"

# Test cases
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Gray")
print(dog.make_sound())
print(cat.make_sound())
