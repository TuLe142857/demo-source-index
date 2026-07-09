from typing import Protocol, TypeVar

T = TypeVar("T")


class Formatter[T](Protocol):
    def format(self, data: T) -> str:
        pass
