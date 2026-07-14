class Speaker:
    def speak(self) -> str:
        return "Hello, from Speaker class!"

class Cat:
    def speak(self) -> str:
        return "Meow!"

class Dog:
    def speak(self) -> str:
        return "Woof!"

def say_hello(name: str):
    print(f"Hello, {name}!")
