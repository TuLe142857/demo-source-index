class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some generic sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"

def create_dog(name: str) -> Dog:
    return Dog(name)
