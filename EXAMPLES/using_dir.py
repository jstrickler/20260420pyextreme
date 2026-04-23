class Dog:
    def bark(self):
        print("woof! woof!")

    def wag(self):
        print("wag wag wag wag wag")

d = Dog()
print(f"{dir(d) = }\n")

colors = ['red', 'blue']
attributes = [name for name in dir(colors) if not name.startswith('_')]
print(f"{attributes = }\n")
