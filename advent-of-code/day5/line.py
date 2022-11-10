from point import Point

class Line:
    def __init__(self, point_a, point_b):
        self._points = []

        lowest_x = point_a.x if point_a.x < point_b.x else point_b.x
        highest_x = point_a.x if point_a.x > point_b.x else point_b.x
        lowest_y = point_a.y if point_a.y < point_b.y else point_b.y
        highest_y = point_a.y if point_a.y > point_b.y else point_b.y

        self.x_range = []
        self.y_range = []

        self.x_range.extend(range(lowest_x, highest_x+1))
        self.y_range.extend(range(lowest_y, highest_y+1))

        if lowest_x == highest_x and len(self.y_range) > 1:
            self.prepare_vertical_line()

        elif lowest_y == highest_y and len(self.x_range) > 1:
            self.prepare_horizontal_line()


        elif len(self.x_range) == len(self.y_range):
            self.prepare_diagonal_line(point_a, point_b)

        else:
            raise ValueError("Could not make line from those points")

        self.create_line()

    def prepare_vertical_line(self):
        difference = len(self.y_range) - len(self.x_range)
        val = self.x_range[0]
        for n in range(0, difference):
            self.x_range.append(val)

    def prepare_horizontal_line(self):
        difference = len(self.x_range) - len(self.y_range)
        val = self.y_range[0]
        for n in range(0, difference):
            self.y_range.append(val)

    def prepare_diagonal_line(self, point_a, point_b):
        if self.is_diagonal_incline(point_a, point_b):
            self.y_range.reverse()

    def is_diagonal_incline(self, point_a, point_b):
        x_increases = point_a.x < point_b.x
        y_increases = point_a.y < point_b.y

        return (x_increases and not y_increases) or (y_increases and not x_increases) 

    def create_line(self):
        for x, y in zip(self.x_range, self.y_range):
            self._points.append(Point(x, y))

    def describe(self):
        return self._points

    def print(self):
        for point in self._points:
            point.print()
        print()

    def equals(self, other_line):
        this_line = self
        if len(this_line.describe()) != len(other_line.describe()):
            return False

        for this_point, other_point in zip(this_line.describe(), other_line.describe()):
            if not (this_point.equals(other_point)):
                return False
        return True