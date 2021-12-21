class vec2D:
    x = 0.0
    y = 0.0

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        msg = "(" + str(self.x) + ", " + str(self.y) + ")"
        return msg
    def __add__(self, other):
        return vec2D(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p = vec2D(3, 4)
    q = vec2D(-1, 2)
    r = p + q

    print(p)
    print(q)
    print(r)