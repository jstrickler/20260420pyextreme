class Spam:
    def __str__(self):  #  what is the object?
        return "Spam instance"
    
    def __repr__(self):  # how to recreate object
        return "Spam()"
    
    def __add__(self, other):
        return 42
    
    def __getitem__(self, index):
        return "foo!"
    
s = Spam()
t = Spam()

print(s)

print(s + t)

print(s[5])

