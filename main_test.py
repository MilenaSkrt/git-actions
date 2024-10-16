import unittest
import math
from main import simpson, rectangle, trapezoid, f   # Replace 'your_module' with the actual module name

class IntegrationTests(unittest.TestCase):
    
    def test_simpson(self):
        expected = 0  # The integral of sin(x) from 0 to 2π
        result = simpson(0, 2 * math.pi, 1000, f)
        self.assertAlmostEqual(result, expected, places=5)

    def test_rectangle(self):
        expected = 0  # The integral of sin(x) from 0 to 2π
        result = rectangle(0, 2 * math.pi, 1000, f)
        self.assertAlmostEqual(result, expected, places=5)

    def test_trapezoid(self):
        expected = 0  # The integral of sin(x) from 0 to 2π
        result = trapezoid(0, 2 * math.pi, 1000, f)
        self.assertAlmostEqual(result, expected, places=5)

if __name__ == '__main__':
    unittest.main()
