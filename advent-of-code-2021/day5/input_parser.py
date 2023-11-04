from line import Line
from point import Point

class InputParser:
    def __init__(self, input_file):
        self.lines = []
        self.max_x = 0
        self.max_y = 0
        self.parse_input(input_file)

    def parse_input(self, file):
        with open(file) as f:
            raw_input = f.read().splitlines()
            for l in raw_input:
                line = self.parse_line(l)
                self.lines.append(line)

    def parse_line(self, line):
        raw_points = line.split("->")
        point_a = self.parse_point(raw_points[0].strip())
        point_b = self.parse_point(raw_points[1].strip())
        line = Line(point_a, point_b)
        return line
    
    def parse_point(self, point):
        point = point.split(",")
        x = int(point[0])
        y = int(point[1])

        # jank: this should not be here
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        return Point(x, y)