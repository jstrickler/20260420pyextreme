
instructor = ('John', 'Strickler', 'Durham', 'NC')
instructor = 'John', 'Strickler', 'Durham', 'NC'

t1 = 5,  # one-element tuple
t2 = ()  # zero-element tuple

print(f"{type(instructor) = }")

first_name, last_name, city, state = instructor  # iterable unpacking

first_name, last_name, *_ = instructor  # iterable unpacking   

*junk, state = instructor
print(f"{junk = }")
print(f"{state = }")

def ham():
    return 10, 'abc'

data = ham()
print(f"{data[0] = }")
print(f"{data[1] = }")

num, string = ham()
print(f"{num = }")
print(f"{string = }")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXt', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for first_name, last_name, *product, dob in people:
    print(first_name, last_name[0], product, dob)
print('-' * 60)
