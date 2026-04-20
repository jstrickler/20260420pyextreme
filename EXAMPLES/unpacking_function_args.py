people = [ # list of 4-element tuples
    ('Joe', 'Schmoe', 'Burbank', 'CA'),
    ('Mary', 'Brown', 'Madison', 'WI'),
    ('Jose', 'Ramirez', 'Ames', 'IA'),
]

def display_person(first_name, last_name, city, state): # function with four parameters
    print(f"{first_name:10} {last_name:10} {city:10} {state}")

display_person("Wanda", "Lefkowitz", "Albany", "NY")  # requires four arguments

for person in people:  # person is a tuple (one element of people list)
    display_person(*person)  # *person unpacks the tuple into four individual arguments
print()

def add_user(*, first_name, last_name, user_id):
    print(f"adding {first_name} {last_name} {user_id}")

user_info = {
    "user_id": "potus-16",
    "last_name": "Lincoln",
    "first_name": "Abraham",
}

add_user(**user_info)
