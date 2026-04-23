
def x(func):
    return 42

@x
def my_function():
    pass

my_function = x(my_function)

print(f"{my_function = }")


def y(a, b, c):
    return "wombat"

@y(1, 2, 3)
def func2():
    pass

wrapper = y(1, 2, 3)  # decorator returns wrapper
func2 = wrapper(func2)

func2 = y(1, 2, 3)(func2)