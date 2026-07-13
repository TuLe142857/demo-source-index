# import
import os

# Constant
YEAR: int = 2026


# Function
def calc_sum(a: int | float, b: int | float) -> int | float:
    return a + b


if __name__ == "__main__":
    print(os.getcwd())
    print(calc_sum(3, 4))
