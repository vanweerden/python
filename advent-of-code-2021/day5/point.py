class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print(self):
        print(f'({self.x}, {self.y})', end="")

    def equals(self, point):
        if self.x == point.x and self.y == point.y:
            return True
        else:
            return False