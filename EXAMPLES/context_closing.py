from contextlib import closing


class Spam():  # define class containing close() method
    def close(self):  # close() method may be called explicitly, or implicitly via with
        print("I'm outta here...")


with closing(Spam()) as c:
    pass
    # c.close() is implicitly called
