import math

class Car():
    def __init__(self, make, model, year, num_doors, owner, mileage, x=0, y=0):
        self.make = make.title()
        self.model = make.title()
        self.year = year
        self.doors = num_doors
        self.owner = owner.title()
        self.mileage = mileage
        self.x = x
        self.y = y

    def describe_car(self):
        print('The car is a %s %s from %d. It has %d doors and is owner by %s'
              % (self.make, self.model, self.year, self.doors, self.owner))

    def journey(self, x_inc=0, y_inc=0):
        self.x += x_inc
        self.y += y_inc

        print('Prior to the journey, the car had travelled %d km.' % self.mileage)
        
        distance = math.sqrt(x_inc**2 + y_inc**2)
        self.mileage += distance
        
        print('After the journey, it has now travelled %d km.' % self.mileage)

    def position(self):
        return 'The car is at (%d, %d).' % (self.x, self.y)
