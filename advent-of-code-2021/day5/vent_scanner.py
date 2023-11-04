from matrix import Matrix
from input_parser import InputParser

class VentScanner:
    def __init__(self, input):
        parser = InputParser(input)
        self.lines = parser.lines
        self.matrix = Matrix(parser.max_x, parser.max_y, 0)

    def scan(self):
        for line in self.lines:
            for point in line.describe():
                val = self.matrix.get(point)
                self.matrix.set(point, val+1)

    def count_danger_zones(self):
        # Count the nmber of points that are two or more
        danger_zone_count = 0
        for val in self.matrix:
            if val >= 2:
                danger_zone_count += 1
        return danger_zone_count