from types import TracebackType
from typing import Protocol, Any

class Reader(Protocol):
    def read(self) -> str | bytes:
        """Read something and return a string or bytes object"""
        ...

class TextFile:
    def read(self) -> str:
        return "contents"

class ToasterOven:
    def toast(self):
        return "toasting"

class TextSlurper:
    def slurp(self) -> str:
        return "slurpage"

class ByteReader:
    def read(self) -> bytes:
        return b"bytes read..."

readers: list[Reader] = [
    t := TextFile(), 
    f := open('../DATA/mary.txt'),
    ts := TextSlurper(),
    br := ByteReader()
]

for reader in readers:
    try:
        result = reader.read()
    except Exception as err:
        print(err)
    else:
        print(result)

class Iterator(Protocol):
    def __next__(self) -> Any:
        ...

class Iterable(Protocol):
    def __iter__(self) -> Iterator:
        ...

nums = [1, 2, 3]
nums_gen = (float(n) for n in nums)
x: list[Iterable] = [nums, nums_gen, range(5)]

for i in x:
    ii = iter(i)
    for j in range(2):
        print(next(ii))

