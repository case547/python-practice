class Person():
    def __init__(self, name, age, birthplace):
        self.name = name.title()
        self.age = age
        self.birthplace = birthplace.title()

    def introduce_yourself(self):
        print('Hello, my name is %s.' % self.name)

    def age_person(self, years=1):
        self.age += years
        return '%s is now %d year(s) old.' % (self.name, self.age)