from datetime import datetime
from functools import wraps

def timestamp(original_function):

    @wraps(original_function)
    def _wrapper(*args, **kwargs):
        print(f"{original_function.__name__} called at {datetime.now().ctime()}")
        return original_function(*args, **kwargs)

    return _wrapper


@timestamp
def spam(spam_count):
    print("SPAM" * spam_count)

@timestamp
def ham():
    print("HAM HAM HAM")


spam(10)
ham()
spam(5)
ham()
print(spam.__name__, ham.__name__)