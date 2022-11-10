import unittest
from point import Point
from line import Line
from input_parser import InputParser
from vent_scanner import VentScanner

class TestDay5(unittest.TestCase):
    test_input = 'test_input.txt'

    def test_line_equals__same_lines__true(self):
        point_a = Point(0, 9)
        point_b = Point(3, 9)
        line_a = Line(point_a, point_b)
        line_b = Line(point_a, point_b)

        result = line_a.equals(line_b)

        self.assertTrue(result)

    def test_line_equals__different_lines__false(self):
        point_a = Point(0, 9)
        point_b = Point(3, 9)
        point_c = Point(0, 3)

        line_a = Line(point_a, point_b)
        line_b = Line(point_a, point_c)

        result = line_a.equals(line_b)

        self.assertFalse(result)

    def test_line_horizontal_ascending(self):
        point_a = Point(0, 9)
        point_b = Point(3, 9)
        line = Line(point_a, point_b)

        actual = line.describe()
        expected = [Point(0, 9), Point(1, 9), Point(2, 9), Point(3, 9)]

        result = True
        for point_a, point_b in zip(actual, expected):
            if not point_a.equals(point_b):
                result = False

        self.assertTrue(result)

    def test_line_horizontal_descending(self):
        point_a = Point(0, 9)
        point_b = Point(3, 9)
        line_asc = Line(point_a, point_b)
        line_desc = Line(point_b, point_a)

        self.assertTrue(line_desc.equals(line_asc))

    def test_line_vertical_ascending(self):
        point_a = Point(2, 1)
        point_b = Point(2, 3)
        line = Line(point_a, point_b)

        actual = line.describe()
        expected = [Point(2, 1), Point(2, 2), Point(2, 3)]

        result = True
        for point_a, point_b in zip(actual, expected):
            if not point_a.equals(point_b):
                result = False

        self.assertTrue(result)

    def test_line_vertical_descending(self):
        point_a = Point(2, 1)
        point_b = Point(2, 3)
        line_asc = Line(point_a, point_b)
        line_desc = Line(point_b, point_a)

        self.assertTrue(line_desc.equals(line_asc))

    def test_line_diagonal_decline_ascending(self):
        point_a = Point(4, 3)
        point_b = Point(6, 5)
        line = Line(point_a, point_b)

        actual = line.describe()
        expected = [Point(4, 3), Point(5, 4), Point(6, 5)]

        result = True
        for point_a, point_b in zip(actual, expected):
            if not point_a.equals(point_b):
                result = False

        self.assertTrue(result)

    def test_line_diagonal_decline_descending(self):
        point_a = Point(4, 3)
        point_b = Point(6, 5)
        line_asc = Line(point_a, point_b)
        line_desc = Line(point_b, point_a)

        self.assertTrue(line_desc.equals(line_asc))

    def test_line_diagonal_incline_ascending(self):
        point_a = Point(4, 3)
        point_b = Point(6, 1)
        line = Line(point_a, point_b)

        actual = line.describe()
        expected = [Point(4, 3), Point(5, 2), Point(6, 1)]

        result = True
        for point_a, point_b in zip(actual, expected):
            if not point_a.equals(point_b):
                result = False

        self.assertTrue(result)

    def test_line_diagonal_incline_descending(self):
        point_a = Point(4, 3)
        point_b = Point(6, 1)
        line_asc = Line(point_a, point_b)
        line_desc = Line(point_b, point_a)

        self.assertTrue(line_desc.equals(line_asc))

    def test_parse_line(self):
        parser = InputParser(self.test_input)
        
        actual = parser.parse_line("0,9 -> 5,9").describe()
        expected = [Point(0, 9), Point(1, 9), Point(2, 9), Point(3, 9), Point(4, 9), Point(5, 9)]

        result = True
        for point_a, point_b in zip(actual, expected):
            if not point_a.equals(point_b):
                result = False

        self.assertTrue(result)

    def test_danger_zone(self):
        vent_scanner = VentScanner(self.test_input)

        vent_scanner.scan()
        actual = vent_scanner.count_danger_zones()
        expected = 12

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()