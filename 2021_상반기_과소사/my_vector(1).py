class vec2D:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        return vec2D(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return vec2D(self.x * other.x, self.y * other.y)

    # def __mod__(self, other):
    #     return vec2D(self.x % other.x, self.y % other.y)

    def __sub__(self, other):
        return vec2D(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return vec2D(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return vec2D(self.x // other.x, self.y // other.y)

#1 나쁜 예시
# p = vec2D()
# p.x = 1
# p.y = 2

#2
if __name__ == "__main__": 
    p = vec2D(1, 2)
    q = vec2D(3, -1)
    print(p)
    print(p+q)