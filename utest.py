# This is an example script for unit testing
import unittest
import module

class MathTest(unittest.TestCase):

    # This test will pass
    def test_add(self):
        # Arrange
        a = [5, 3, -2, 200, 10000543, 0, 2.34]
        b = 3
        # Act
        for i in a:
            sum = module.math.add(i, b)
            print(sum)
        # Assert
            self.assertEqual(sum, i + b)
    # This test will fail
    def test_sub(self):
        # Arrange
        a = [5, 3, -2, 200, 10000543, 0, 2.34]
        b = 3
        # Act
        for i in a:
            sub = module.math.sub(i, b)
            print(sub)
        # Assert
            self.assertEqual(sub, i + b)


if __name__ == "__main__":
    unittest.main()
