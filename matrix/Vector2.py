class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def equal(self, v) -> bool:
        return v.x == self.x and v.y == self.y

    def getTranspositionDimension(self):
        return Vector2(self.y, self.x)

    def __str__(self) -> str:
        return "Vector2: x(cols) = {x}, y(rows) = {y}".format(x = self.x, y = self.y)

    def tuple(self):
        return (self.x, self.y)