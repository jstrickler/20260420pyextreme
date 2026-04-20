import inspect
import geometry
from carddeck import CardDeck

deck = CardDeck("Leonard")

things = (
    geometry,
    geometry.circle_area,
    CardDeck,
    CardDeck.get_ranks,
    deck,
    deck.shuffle,
)

def get_instance_type_name(obj):
    return f"{type(thing).__name__} instance" 

print("Name               Module?  Function?  Class?  Method?")
for thing in things:
    thing_name = getattr(thing, '__name__',  get_instance_type_name(thing))
    print("{:18s} {!s:6s}   {!s:6s}     {!s:6s}  {!s:6s}".format(
        thing_name,
        inspect.ismodule(thing),  # test for module
        inspect.isfunction(thing),  # test for function
        inspect.isclass(thing),  # test for class
        inspect.ismethod(thing),
    ))
