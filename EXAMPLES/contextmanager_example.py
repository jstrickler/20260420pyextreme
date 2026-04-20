from contextlib import contextmanager

@contextmanager
def spam(): # defines normal function (not a context-aware class)
    yield 25 # provide value for context variable (assigned by with statement)
    print("starting exit...") # code to be executed when block exits
    print("...finishing")


with spam() as s:  # s gets value yield'ed in function
    print("s is", s)
    print("in the context block...")
