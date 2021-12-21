class Ball:
    color = 'white'
    size = 5
    direction = 'default'

    # def __init__(self, color = 'red', size = '5', direction = 'down'):
    #     self.color = color
    #     self.size = size
    #     self.direction = direction

    def bounce(self):
        if self.direction == 'down':
            self.direction == 'up'

myball = Ball()
print(myball.direction)

myball.direction = 'down'
print(myball.direction)
print(myball.__class__.direction)

myball.__class__.direction = 'left'
print(myball.direction)
print(myball.__class__.direction)

urball = Ball()
print(urball.direction)

urball.size = 10
print(urball.size)
print(myball.size)