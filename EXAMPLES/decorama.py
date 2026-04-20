"""
decorama -- demo of 8 combinations of decorator implementation

decorators applied to functions:
    1. decorator without args   @deco_func
        decorator returns replacement function
    2. decorator with args  @deco_func(arg, ...)
        decorator returns wrapper
        wrapper returns replacement function
    3. class without args   @deco_class
        __call__ IS replacement function
    4. class with args   @deco_class(arg, ...)
        __call__ RETURNS replacement function

decorators applied to classes:
    (NOTE: replacement class is frequently the original class, but doesn't have to be)
    5. decorator function without args @deco_func
        decorator returns replacement class
    6. decorator function with args @deco_func(arg, ...)
        decorator returns wrapper
        wrapper return replacement class
    7. decorator class without args @deco_class
        __call__ returns replacement class
    8. decorator class with args @deco_class(arg, ...)
        ???
"""
#TODO: implement 8 different use cases
import logging
from functools import wraps

def print_header(decorator_name):
    print('-' * 60)
    print(f"** {decorator_name} **")
    print('-' * 60)

DETAILED_FORMAT = "%(levelname)s %(filename)s %(lineno)s %(asctime)s %(message)s"
TERSE_FORMAT = "%(levelname)s %(asctime)s %(message)s"

logging.basicConfig(
    filename="functioncalls.log",
    format=DETAILED_FORMAT,
    level=logging.INFO,
)

# Use case 1: Log function calls with a timestamp
print_header("log_timestamp()")


def log_timestamp(wrapped_function):
    """
    function without params decorating a function -- the simplest kind of decorator

    @log_timestamp
    def bar():
        pass

    same as
    bar = log_timestamp(bar)

    :param wrapped_function: function to decorate
    :return: replacement function
    """
    @wraps(wrapped_function)
    def _wrapper(*args, **kwargs):
        logging.info(wrapped_function.__name__)
        result = wrapped_function(*args, **kwargs)
        return result

    return _wrapper

@log_timestamp
def target_one_alpha():
    print("Hello from target_one_alpha()")

@log_timestamp
def target_one_beta():
    print("Hello from target_one_beta()")


target_one_alpha()
target_one_beta()

# Use case 2: Log function calls with a timestamp and select whether to log details
print_header("log_details()")

def log_details(show_details=True):
    """
    function with params decorating a function

    The decorator gets the args, and then returns a wrapper
    function.

    The wrapper gets the function being wrapped, and returns
    the replacement function.

    @log_details(show_details=False)
    def bar():
        pass

    :param value: named parameter toggle for logging details
    :return: wrapper function (which returns replacement function)
    """

    def _wrapper_factory(wrapped_function):
        @wraps(wrapped_function)
        def _wrapper(*args, **kwargs):
            if show_details:
                logger.fo
            logging.info(wrapped_function.__name__)
            return wrapped_function(*args, **kwargs)

        return _wrapper

    return _wrapper_factory

@log_details()
def target_two_alpha():
    print("Hello from target_one_alpha()")

@log_details(show_details=False)
def target_two_beta():
    print("Hello from target_one_beta()")

target_one_alpha()
target_two_beta()

exit()

class DecoThree():
    """
    class without params decorating a function

    __call__() is the replacement function

    __init__() is passed the wrapped function

    @DecoThree
    def bar():
        pass

    same as
    bar  = DecoThree(bar)


    """

    def __init__(self, wrapped_function):
        self._wrapped_function = wrapped_function

    def __call__(self, *args, **kwargs):
        print("GREETINGS from deco_three!")
        return self._wrapped_function(*args, **kwargs)


class DecoFour():
    """
    class with params decorating a function

    __call__() RETURNS the replacement function


    @deco_four('blah')
    def bar():
        pass

    same as
    bar  = deco_four('blah')(bar)
    or,
    wrapper = deco_four('blah')
    bar = wrapper(bar)
    """

    def __init__(self, value):
        self._value = value

    def __call__(self, wrapped_function):
        @wraps(wrapped_function)
        def _replacement(*args, **kwargs):
            print(f"GREETINGS from deco_four -- value is {self._value}!")
            result = wrapped_function(*args, **kwargs)
            return result + 4

        return _replacement


print("Function decorators:")


print_header("DecoThree()")
print_header("DecoFour()")

@DecoThree
@DecoFour('BANANA')
def target_function(color, value):
    """
    Target function for decorators 1-4

    :param color: Color as string
    :param value: Any value
    :return: None
    """
    print(("Hello from target_function -- color is {} and value is {}".format(color, value)))
    # print(("Target function's name is", target_function.__name__))
    return 10 * value


TF_RESULT = target_function('red', 10)
print(("RESULT is", TF_RESULT))
print(('-' * 50))
TF_RESULT = target_function('green', 45)
print(("RESULT is", TF_RESULT))
print(('-' * 50))
print()
print()


def deco_five(target_class):
    """
    function without params decorating a class

    :param target_class: class to be decorated
    :return: modified class
    """
    print("GREETINGS from deco_five!")

    @property
    def _temp(self):
        return self._value1

    target_class.value_one = _temp

    return target_class


def deco_six(fruit):
    """
    function with params decorating a class; returns wrapper which is applied to target class

    :param fruit:
    :return: modified class
    """
    print("GREETINGS from deco_six!")

    def wrapper(target_class):
        target_class._fruit = fruit

        @property
        def _temp(self):
            return self._fruit

        target_class.fruit = _temp

        return target_class

    return wrapper


@deco_five
@deco_six('MANGO')
class TargetClass():

    def __init__(self, v1, v2, v3, v4):
        self._value1 = v1
        self._value2 = v2
        self._value3 = v3
        self._value4 = v4


T1 = TargetClass('fee', 'fi', 'fo', 'fum')
print(("T1 is", T1))
print(("value_one:", T1.value_one))

print(('-' * 50))
T2 = TargetClass('eeny', 'meeny', 'miny', 'mo')
print(("T2:", T2))
print(("T2.value_one:", T2.value_one))
print(("T2.fruit:", T2.fruit))

print(('-' * 50))


class DecoSeven():
    """
    class without params decorating a class

    __new__() returns the modified class (not __init__, because __init__ is *instance* initializer)

    """

    def __new__(cls, class_):   # class_ is the original class
        print("GREETINGS from deco_seven!")
        class_.color = 'blue'
        return class_


@DecoSeven
class TargetClass():
    pass

T1 = TargetClass()
print((T1.color))
print(("T1 id:", id(T1)))
print((TargetClass.__name__, T1))

T2 = TargetClass()
print((T2.color))
print(("T2 id:", id(T2)))

print(('-' * 50))


class DecoEight():
    """
    class with params decorating a class

    __call__() returns the modified class
    """

    def __init__(self, color):
        print("GREETINGS from deco_eight!")
        self._color = color

    def __call__(self, old_class):
        old_class.color = self._color
        return old_class


@DecoEight('purple')
class TargetClass():
    pass

T1 = TargetClass()
print((T1.color))
