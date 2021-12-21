class Person:
    def __init__(self, name, job = None, pay = 0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    
    def __str__(self):
        return '[Person: %s, %s]' %(self.name, self.pay)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 10000)
    # print(bob.name, bob.pay)
    # print(sue.name, sue.pay)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.1)
    print(sue.pay)