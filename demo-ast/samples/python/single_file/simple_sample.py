# import
import os



class Calculator:
    def __int__(self):
        pass

    def sum(self, a, b):
        """
        Sum the two numbers
        Args:
            a: number
            b: number

        Returns: the sum of the two numbers

        """
        return a + b

# Constant
NAME: str = "World"
""" doc..."""

def say_hi(name: str=NAME):
    """
    Docstring ...
    Args:
        name: name

    Returns: None

    """
    print("Hello, " + name)


if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.sum(1, 2))
    say_hi()
