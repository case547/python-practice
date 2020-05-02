from math import sqrt

class Rocket():
    # Rocket simulates a rocket ship for a game or a physics simulation.
    
    def __init__(self, x=0, y=0, height=100, crew_size=3):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        self.height = height
        self.crew = crew_size
        
    def move_rocket(self, x_inc=0, y_inc=1):
        # Move the rocket according to the paremeters given.
        # Default behavior is to move the rocket up one unit.
        self.x += x_inc
        self.y += y_inc

    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
    def launch(self):
        return 'The rocket %s has lifted off!' % self

    def land_rocket(self):
        print('Position before landing: (%d, %d)' % (self.x, self.y))
        self.x = 0
        self.y = 0
        print('Position after landing: (%d, %d)' % (self.x, self.y))

    def safety_check(self, other_rocket):
        distance = self.get_distance(other_rocket)
        if distance > 20:
            return 'The rockets are a self distance away from each other.'
        elif distance < 0:
            return 'The rockets are getting a bit too close for comfort!'
        else:
            return 'The rockets have crashed!'

# Make a series of rockets at different starting places.
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,10))
rockets.append(Rocket(100,0))

'''# Create three rockets.
rockets = [Rocket() for x in range(0,3)]
'''

# Move each rocket a different amount.
rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)

# Show where each rocket is.
for index, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (index, rocket.x, rocket.y))

# Make two rockets, at different places.
rocket0 = rockets[0]
rocket1 = rockets[1]

# Show the distance between them.
distance = rocket0.get_distance(rocket1)
print("Rockets 0 and 1 are %f units apart." % distance)