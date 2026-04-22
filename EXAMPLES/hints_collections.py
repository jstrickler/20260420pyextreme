from typing import Iterable, Any

people: list[tuple[str, int]]

spam: list

ham: list[int] 

toast: tuple[str, int, str, float]

eggs: tuple[int, ...]

class Dog:
    pass

dogs: list[Dog]

clothes: dict[int, list[str]]

people: set[str]

def power(x: int|float, y: int|float) -> int|float:
    return x ** y

Number = int | float

def p(x: Number, y: Number) -> Number | None:
    pass


def read_files(files: Iterable) -> None:
    pass


def append_to_record(key: str, value: Any):
    pass


class Foo:
    def __init__(self, bar: 'Bar'):
        self.thing = bar


    def get_thing(self) -> 'Foo':
        return self

class Bar:
    pass


b = Bar()

f = Foo(b)

