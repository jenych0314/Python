from person import Person
from manager import Manager

class Department:
    def __init__(self, *args) -> None:
        self.members = list(args)

    def addMembers(self, person):
        self.members.append(person)
    
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 10000)
    tom = Manager('Tom Jones', 'mgr', 50000)
    development = Department(bob, sue)
    development.addMembers(tom)
    development.giveRaises(0.1)
    development.showAll()