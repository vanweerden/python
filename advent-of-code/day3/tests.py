import unittest
from main import BinaryDiagnosticator

##############################################
### TESTS FOR ADVENT OF CODE: DAY 3
##############################################

class TestDay3(unittest.TestCase):
    file = 'test_input.txt'

    def test_get_gamma_rate(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_gamma_rate(), '10110')

    def test_get_epsilon_rate(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_epsilon_rate(), '01001')

    def test_get_power_consumption(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_power_consumption(), 198)

    def test_get_ox_generator_rating(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_ox_generator_rating(tester.input), '10111')

    def test_get_co2_scrubber_rating(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_co2_scrubber_rating(tester.input), '01010')

    def test_get_life_support_rating(self):
        tester = BinaryDiagnosticator(self.file)
        self.assertEqual(tester.get_life_support_rating(), 230)

if __name__ == '__main__':
    unittest.main()