class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    pass # Метод не перевизначено

animals = [Dog(), Cat(), Fish()]
for animal in animals:
    print(f"{animal.__class__.__name__} каже: {animal.speak()}")