from point import Point 

class Matrix: 
    def __init__(self, x_max, y_max, init_val):
        self._matrix = []
        self.x_max = x_max
        self.y_max = y_max
        self.width = x_max+1
        self.height = y_max+1

        for y in range(0, self.height):
            row = []
            for x in range(0, self.width):
                row.append(init_val)
            self._matrix.append(row)
          
    def print(self):
        for row in self._matrix:
            for col in row:
                print(col, end='')
            print()

    def get(self, point):
        self.throw_if_invalid(point)
        return self._matrix[point.x][point.y]

    def set(self, point, val):
        self.throw_if_invalid(point)
        self._matrix[point.x][point.y] = val

    def dump():
        for x in range(0, self.width):
            for y in range(0, self.height):
                return _matrix[x][y]
    
    def throw_if_invalid(self, point):
        error_msg = []
        if point.x > self.x_max:
            error_msg.append(f'x value ({str(point.x)}) is out of bounds (max is {str(self.x_max)})')
        elif point.x < 0:
            error_msg.append(f'x cannot be negative (passed {str(point.x)})')

        if point.y > self.y_max:
            error_msg.append(f'x value ({str(point.y)}) is out of bounds (max is {str(self.y_max)})')
        elif point.y < 0:
            error_msg.append(f'y cannot be negative (passed {str(point.y)})')

        if len(error_msg) > 0:
            raise ValueError(". Also, ".join(error_msg))

    def __iter__(self):
        self.x = 0
        self.y = 0
        return self

    def __next__(self):
        if self.x < self.x_max:
            point = Point(self.x, self.y)
            self.x += 1
            return self.get(point)
        elif self.x == self.x_max and self.y < self.y_max:
            point = Point(self.x, self.y)
            self.x = 0
            self.y += 1
            return self.get(point)
        elif self.x == self.x_max and self.y == self.y_max:
            point = Point(self.x, self.y)
            self.x+=1
            return self.get(point)
        else:
            raise StopIteration