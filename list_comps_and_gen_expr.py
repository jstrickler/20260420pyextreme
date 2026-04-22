fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f.upper() for f in fruits if f.startswith('p') if len(f) > 6]
print(f"{f3 = }\n")

f4 = [f for f in fruits if len(f) < 6]
print(f"{f4 = }\n")

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()

cards = [f"{r}-{s}" for s in suits for r in ranks]
print(f"{cards = }\n")

