from typing import TypeVar, Protocol

T = TypeVar("T")


class Formatter[T](Protocol):
    def format(self, data: T) -> str:
        pass
