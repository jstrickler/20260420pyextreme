def doit(a, b):
    print(a * b)

doit('-', 60)
doit(5, 88)

data = [(8, 10), ('Python', 4), (4.9, 6.2323)]

for item in data:
    doit(item[0], item[1])
print('-' * 60)

for item in data:
    doit(*item)  # passes 2 args to doit

#    spam(*args, **kwargs)