class Person:
    '''Represents a person.'''
    population = 0

    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print('(Initializing %s)',self.name)

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        return 'Hi, my name is %s'%self.name