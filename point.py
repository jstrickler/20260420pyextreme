from dataclasses import dataclass

class OldPoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    # __repr__ and __str__

@dataclass
class Point:
    x: int
    y: int

p1 = Point(x=1, y=2)
p2 = Point(x=3, y=4)
print(f"{p1.x = }")
print(f"{p1.y = }")
print(f"{p1 = }")
print(f"{p2 = }")

