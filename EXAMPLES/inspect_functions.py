import inspect

def spam(p1: int, p2='a', *p3: str, p4, p5='b', **p6) -> tuple:  # define a function
    print(p1, p2, p3, p4, p5, p6)
    return ()

# get argument specifications for a function
print("Function spec for Ham:", inspect.getfullargspec(spam))
print()
