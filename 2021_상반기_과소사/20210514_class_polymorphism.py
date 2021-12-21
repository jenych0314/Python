class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height / 2

class Square:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    def getArea(self):
        area = self.width * self.height