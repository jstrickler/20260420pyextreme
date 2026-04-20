class ClearList():
    def __init__(self, alist):
        self._list = alist

    def __enter__(self):
        return self._list

    def __exit__(self, c_type, exc_value, tb):
        for i in range(len(self._list)):
            self._list[i] = 0


my_list = list(range(25))

with ClearList(my_list) as t:
    print(t)

print(my_list)
