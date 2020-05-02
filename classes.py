class Rocket():
    # Rocket simulates a rocket ship for a game or a physics simulation.
    
    def __init__(self):
    #  __init__() method sets values for parameters to be defined when an object is first created
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0
    
    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a Rocket object, and have it start to move up
my_rocket = Rocket()
print(my_rocket)
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)


# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    my_rockets = [Rocket() for x in range(0,5)]
    
# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)
    
# Move the first rocket up.
my_rockets[0].move_up()

# Show that only the first rocket has moved.
for rocket in my_rockets:
    print('Rocket altitude:', rocket.y)
    

'''General OOP Terminology

Class: Body of code that defines attributes and behaviors required to accurately model something needed for a program: something from the real world, e.g. a rocket ship or a guitar string; or something from a virtual world e.g. a rocket in a game or set of physical laws for a game engine.

Attribute: Piece of information; a variable that is part of a class.

Behaviour: An action defined within a class. These are made up of methods, which are functions defined for the class.

Object: Particular instance of a class. An object has a certain set of values for attributes in the class. There can be infinitely many objects for any class.
'''