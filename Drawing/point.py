
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def draw(self):
        print(f"X:{self.x}, Y:{self.y}")
