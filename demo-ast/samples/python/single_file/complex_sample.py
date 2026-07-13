#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module docstring - file mẫu (sample file) đầy đủ cú pháp Python
dùng để test tree-sitter (một thư viện parser - phân tích cú pháp - đa ngôn ngữ).

Mục tiêu: bao phủ càng nhiều node cú pháp Python càng tốt.
"""

from __future__ import annotations

import asyncio
import functools
import sys as system_module
from abc import ABC, abstractmethod
from collections import namedtuple
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Protocol,
    TypeVar,
    Union,
)

# ---------------------------------------------------------------------------
# 1. CONSTANT (hằng số) - quy ước viết HOA toàn bộ
# -------------------------------------------------------------------   --------
PI: float = 3.14159265358979
MAX_RETRY_COUNT: int = 5
APP_NAME = "TreeSitterSampleApp"
DEFAULT_CONFIG: Dict[str, Any] = {
    "debug": False,
    "timeout": 30,
    "tags": ["a", "b", "c"],
}
VERSION_TUPLE = (1, 0, 0)
EMPTY_SET = set()
NONE_VALUE = None
BOOL_FLAG = True

# Module-level namedtuple (kiểu tuple có tên trường - named field tuple)
Point = namedtuple("Point", ["x", "y"])


# ---------------------------------------------------------------------------
# 2. TYPE ALIAS & TYPE VAR (bí danh kiểu & biến kiểu tổng quát - generic type variable)
# ---------------------------------------------------------------------------
T = TypeVar("T")
JsonDict = Dict[str, Any]
Number = Union[int, float]


# ---------------------------------------------------------------------------
# 3. ENUM (kiểu liệt kê)
# ---------------------------------------------------------------------------
class Color(Enum):
    """Enum minh hoạ cho kiểu liệt kê."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()

    def describe(self) -> str:
        return f"Color.{self.name} = {self.value}"


# ---------------------------------------------------------------------------
# 4. PROTOCOL / INTERFACE (giao thức - kiểu interface trong Python)
# ---------------------------------------------------------------------------
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...


# ---------------------------------------------------------------------------
# 5. ABSTRACT BASE CLASS (lớp cơ sở trừu tượng)
# ---------------------------------------------------------------------------
class Shape(ABC):
    """Lớp trừu tượng đại diện cho một hình học."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def area(self) -> float:
        """Phương thức trừu tượng (abstract method) - lớp con bắt buộc cài đặt."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self) -> float:
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"<Shape name={self.name!r}>"


# ---------------------------------------------------------------------------
# 6. CLASS kế thừa đơn (single inheritance) + property + static/class method
# ---------------------------------------------------------------------------
class Circle(Shape):
    """Hình tròn kế thừa từ Shape."""

    unit: str = "cm"  # class attribute (thuộc tính lớp)

    def __init__(self, radius: float) -> None:
        super().__init__(name="circle")
        self._radius = radius

    @property
    def radius(self) -> float:
        """Getter cho bán kính (radius)."""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value < 0:
            raise ValueError("radius must be non-negative")
        self._radius = value

    def area(self) -> float:
        return PI * self._radius**2

    def perimeter(self) -> float:
        return 2 * PI * self._radius

    @staticmethod
    def unit_circle() -> "Circle":
        """Static method (phương thức tĩnh) - không phụ thuộc instance."""
        return Circle(1.0)

    @classmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        """Class method (phương thức lớp) - nhận cls thay vì self."""
        return cls(diameter / 2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

    def __lt__(self, other: "Circle") -> bool:
        return self.area() < other.area()


# ---------------------------------------------------------------------------
# 7. ĐA KẾ THỪA (multiple inheritance) + MRO (method resolution order)
# ---------------------------------------------------------------------------
class Drawable:
    def draw(self) -> str:
        return "drawing base"


class Colored:
    def __init__(self, color: Color = Color.RED) -> None:
        self.color = color


class ColoredCircle(Circle, Drawable, Colored):
    """Minh hoạ đa kế thừa (multiple inheritance)."""

    def __init__(self, radius: float, color: Color) -> None:
        Circle.__init__(self, radius)
        Colored.__init__(self, color)

    def draw(self) -> str:
        return f"drawing {self.color.name.lower()} circle r={self.radius}"


# ---------------------------------------------------------------------------
# 8. DATACLASS (lớp dữ liệu - tự sinh __init__, __repr__, ...)
# ---------------------------------------------------------------------------
@dataclass(frozen=True, order=True)
class Vector2D:
    """Dataclass bất biến (immutable) đại diện cho vector 2 chiều."""

    x: float = 0.0
    y: float = 0.0
    tags: List[str] = field(default_factory=list)

    def magnitude(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)


# ---------------------------------------------------------------------------
# 9. GENERIC CLASS (lớp tổng quát hoá)
# ---------------------------------------------------------------------------
class Stack(Generic[T]):
    """Cấu trúc dữ liệu ngăn xếp (stack) tổng quát cho kiểu T bất kỳ."""

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)


# ---------------------------------------------------------------------------
# 10. METACLASS (siêu lớp - lớp của lớp)
# ---------------------------------------------------------------------------
class SingletonMeta(type):
    """Metaclass hiện thực mẫu thiết kế Singleton (chỉ một instance duy nhất)."""

    _instances: Dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class ConfigManager(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.settings: JsonDict = dict(DEFAULT_CONFIG)


# ---------------------------------------------------------------------------
# 11. CUSTOM EXCEPTION (ngoại lệ tự định nghĩa)
# ---------------------------------------------------------------------------
class ValidationError(Exception):
    """Ngoại lệ tuỳ chỉnh khi dữ liệu không hợp lệ."""

    def __init__(self, message: str, code: int = 400) -> None:
        super().__init__(message)
        self.code = code


# ---------------------------------------------------------------------------
# 12. FUNCTION cơ bản, mặc định, *args/**kwargs, keyword-only, positional-only
# ---------------------------------------------------------------------------
def add(a: int, b: int = 10) -> int:
    """Hàm cộng đơn giản với tham số mặc định (default parameter)."""
    return a + b


def make_summary(*args: int, **kwargs: Any) -> str:
    """Hàm dùng *args (đối số vị trí biến thiên) và **kwargs (đối số từ khoá biến thiên)."""
    total = sum(args)
    meta = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"total={total}; {meta}"


def strict_signature(pos_only, /, normal, *, kw_only):
    """Hàm minh hoạ positional-only (chỉ theo vị trí) và keyword-only (chỉ theo từ khoá)."""
    return pos_only, normal, kw_only


# ---------------------------------------------------------------------------
# 13. LAMBDA (hàm ẩn danh)
# ---------------------------------------------------------------------------
square = lambda x: x * x
adder = lambda a, b=1: a + b


# ---------------------------------------------------------------------------
# 14. DECORATOR (hàm trang trí) tự định nghĩa
# ---------------------------------------------------------------------------
def retry(times: int = MAX_RETRY_COUNT):
    """Decorator factory - hàm sinh ra decorator, cho phép truyền tham số."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Optional[Exception] = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:  # noqa: BLE001
                    last_exc = exc
            raise last_exc  # type: ignore[misc]

        return wrapper

    return decorator


@retry(times=3)
def unstable_operation(value: int) -> int:
    """Hàm được áp dụng decorator @retry."""
    if value < 0:
        raise ValidationError("value must be positive", code=422)
    return value * 2


# ---------------------------------------------------------------------------
# 15. GENERATOR FUNCTION (hàm sinh dùng yield) & GENERATOR EXPRESSION
# ---------------------------------------------------------------------------
def fibonacci_gen(limit: int):
    """Generator (hàm sinh) trả về dãy Fibonacci bằng yield."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


squares_gen = (n * n for n in range(10))


# ---------------------------------------------------------------------------
# 16. COMPREHENSIONS: list / dict / set
# ---------------------------------------------------------------------------
list_comp = [x * 2 for x in range(10) if x % 2 == 0]
dict_comp = {k: k * k for k in range(5)}
set_comp = {x % 3 for x in range(20)}
nested_comp = [[i * j for j in range(3)] for i in range(3)]


# ---------------------------------------------------------------------------
# 17. CONTEXT MANAGER (trình quản lý ngữ cảnh - dùng với with)
# ---------------------------------------------------------------------------
@contextmanager
def open_resource(name: str):
    """Context manager tự định nghĩa bằng decorator @contextmanager."""
    print(f"Opening resource {name}")
    try:
        yield {"name": name, "status": "open"}
    finally:
        print(f"Closing resource {name}")


class FileLikeResource:
    """Context manager theo giao thức __enter__/__exit__."""

    def __enter__(self) -> "FileLikeResource":
        self.data = []
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        self.data.clear()
        return False


# ---------------------------------------------------------------------------
# 18. CONTROL FLOW: if/elif/else, for/else, while/else, try/except/else/finally
# ---------------------------------------------------------------------------
def classify_number(n: int) -> str:
    if n < 0:
        result = "negative"
    elif n == 0:
        result = "zero"
    else:
        result = "positive"
    return result


def find_first_even(numbers: List[int]) -> Optional[int]:
    for n in numbers:
        if n % 2 == 0:
            break
    else:
        return None
    return n


def safe_divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError as exc:
        raise ValidationError("division by zero") from exc
    except (TypeError, ValueError) as exc:
        print(f"Unexpected error: {exc}")
        raise
    else:
        print("Division succeeded")
        return result
    finally:
        print("safe_divide finished")


# ---------------------------------------------------------------------------
# 19. MATCH-CASE (cấu trúc so khớp mẫu - structural pattern matching, Python 3.10+)
# ---------------------------------------------------------------------------
def handle_command(command: JsonDict) -> str:
    match command:
        case {"action": "move", "x": x, "y": y}:
            return f"move to ({x}, {y})"
        case {"action": "stop"}:
            return "stopping"
        case Point(x=0, y=0):
            return "at origin"
        case [first, *rest] if rest:
            return f"list starting with {first}"
        case str() as s:
            return f"string command: {s}"
        case _:
            return "unknown command"


# ---------------------------------------------------------------------------
# 20. WALRUS OPERATOR (toán tử gán trong biểu thức, :=) & UNPACKING
# ---------------------------------------------------------------------------
def process_stream(data: List[int]) -> List[int]:
    results = []
    index = 0
    while (current := data[index] if index < len(data) else None) is not None:
        results.append(current)
        index += 1
    return results


first, *middle, last = [1, 2, 3, 4, 5]
a_val, b_val = b_val_tmp, a_val_tmp = 1, 2


# ---------------------------------------------------------------------------
# 21. F-STRING, MULTILINE STRING, RAW STRING, BYTES
# ---------------------------------------------------------------------------
def format_report(user: str, score: float) -> str:
    header = f"Report for {user.upper()}"
    body = f"""
    Score: {score:.2f}
    Grade: {"A" if score >= 90 else "B"}
    """
    return header + body


RAW_PATH = r"C:\Users\example\path"
BYTE_DATA = b"\x00\x01\x02binary"


# ---------------------------------------------------------------------------
# 22. ASYNC / AWAIT (bất đồng bộ) + async generator + async context manager
# ---------------------------------------------------------------------------
async def fetch_data(url: str) -> JsonDict:
    """Hàm bất đồng bộ (coroutine) mô phỏng gọi mạng."""
    await asyncio.sleep(0.1)
    return {"url": url, "status": 200}


async def fetch_many(urls: List[str]) -> List[JsonDict]:
    tasks = [fetch_data(u) for u in urls]
    return await asyncio.gather(*tasks)


async def async_number_stream(limit: int):
    """Async generator (bộ sinh bất đồng bộ)."""
    for i in range(limit):
        await asyncio.sleep(0)
        yield i


class AsyncResource:
    async def __aenter__(self) -> "AsyncResource":
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        await asyncio.sleep(0)


async def main_async() -> None:
    async with AsyncResource() as res:
        async for value in async_number_stream(3):
            print(value, res)


# ---------------------------------------------------------------------------
# 23. GLOBAL / NONLOCAL, CLOSURE (bao đóng), NESTED FUNCTION
# ---------------------------------------------------------------------------
counter = 0


def increment_global() -> int:
    global counter
    counter += 1
    return counter


def make_counter() -> Callable[[], int]:
    """Closure (bao đóng) - hàm lồng ghi nhớ biến ngoại vi."""
    count = 0

    def inner() -> int:
        nonlocal count
        count += 1
        return count

    return inner


# ---------------------------------------------------------------------------
# 24. DECORATED CLASS, OPERATOR OVERLOAD, __slots__
# ---------------------------------------------------------------------------
class ImmutablePoint:
    """Class dùng __slots__ để giới hạn thuộc tính, tiết kiệm bộ nhớ."""

    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "ImmutablePoint") -> "ImmutablePoint":
        return ImmutablePoint(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))


# ---------------------------------------------------------------------------
# 25. TERNARY EXPRESSION, ASSERT, DEL, CONDITIONAL IMPORT
# ---------------------------------------------------------------------------
def sign(n: int) -> int:
    return 1 if n > 0 else (-1 if n < 0 else 0)


def demo_assert_del() -> None:
    temp_list = [1, 2, 3]
    assert len(temp_list) == 3, "temp_list phải có 3 phần tử"
    del temp_list[0]


if system_module.version_info >= (3, 8):
    from typing import Literal  # conditional import (nhập điều kiện)
else:  # pragma: no cover
    Literal = None  # type: ignore


Mode = Literal["read", "write", "append"]


# ---------------------------------------------------------------------------
# 26. MAIN ENTRY POINT
# ---------------------------------------------------------------------------
def main() -> None:
    """Điểm vào chính của chương trình (entry point)."""
    circle = Circle(radius=2.0)
    colored = ColoredCircle(radius=1.5, color=Color.BLUE)
    vector = Vector2D(1.0, 2.0) + Vector2D(3.0, 4.0)

    stack: Stack[int] = Stack()
    for value in [1, 2, 3]:
        stack.push(value)

    print(circle, circle.area(), colored.draw(), vector)
    print(add(5), make_summary(1, 2, 3, unit="cm"))
    print(list(fibonacci_gen(20)))
    print(handle_command({"action": "move", "x": 1, "y": 2}))

    with open_resource("db-connection") as resource:
        print(resource)

    asyncio.run(main_async())


if __name__ == "__main__":
    main()
