import unittest
import submarine

Submarine = submarine.Submarine

##############################################
### TESTS FOR ADVENT OF CODE: DAY 2
##############################################

class TestSubmarineMethods(unittest.TestCase):
    def test_initialization(self):
        # Without __init__ arguments
        test_sub1 = Submarine()
        self.assertEqual(test_sub1.h_position, 0)
        self.assertEqual(test_sub1.depth, 0)
        self.assertEqual(test_sub1.aim, 0)

        # With __init__ arguments
        test_sub2 = Submarine(5, 6, 1)
        self.assertEqual(test_sub2.h_position, 5)
        self.assertEqual(test_sub2.depth, 6)
        self.assertEqual(test_sub2.aim, 1)

    def test_forward(self):
        sub = Submarine(0, 0, 5)
        sub.forward(5)
        expected_depth = 25
        self.assertEqual(sub.h_position, 5)
        self.assertEqual(sub.depth, expected_depth)
    
    def test_depth_limit(self):
        # Depth shouldn't go below 0
        sub = Submarine(0, 0, -5)
        sub.forward(10)
        self.assertEqual(sub.depth, 0)

    def test_up(self):
        test_sub = Submarine(0, 0, 10)
        test_sub.up(6)
        self.assertEqual(test_sub.aim, 4)

    def test_down(self):
        test_sub = Submarine()
        test_sub.down(6)
        self.assertEqual(test_sub.aim, 6)

    def test_puzzle_example(self):
        test_sub = Submarine()
        test_sub.forward(5)
        test_sub.down(5)
        test_sub.forward(8)
        test_sub.up(3)
        test_sub.down(8)
        test_sub.forward(2)

        result = test_sub.depth * test_sub.h_position
        self.assertEqual(result, 900)

if __name__ == '__main__':
    unittest.main()