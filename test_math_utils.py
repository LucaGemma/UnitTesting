import unittest
from math_utils import MathUtils
# from scriptDoveAveteMessoLaClasse import NomeClasse

class TestMathUtils(unittest.TestCase):
    """
    """

    def test_add(self):
        """
        """
        self.assertEqual(MathUtils.add(1, 2), 3)
        self.assertEqual(MathUtils.add(1.5, 2.5), 4.0)
        self.assertEqual(MathUtils.add(-1, 1), 0)
        self.assertEqual(MathUtils.add(-1.5, 1.5), 0.0)

    def test_subtract(self):
        """
        """
        self.assertEqual(MathUtils.subtract(1, 2), -1)
        self.assertEqual(MathUtils.subtract(1.5, 2.5), -1.0)
        self.assertEqual(MathUtils.subtract(-1, 1), -2)
        self.assertEqual(MathUtils.subtract(-1.5, 1.5), -3.0)

    def test_divide(self):
        """
        """
        self.assertEqual(MathUtils.divide(1, 2), 0.5)
        self.assertEqual(MathUtils.divide(1.5, 2.5), 0.6)
        self.assertEqual(MathUtils.divide(-1, 1), -1)
        self.assertEqual(MathUtils.divide(-1.5, 1.5), -1.0)
        with self.assertRaises(ValueError):
            MathUtils.divide(1, 0)

    def test_assertions(self):
        """
        Shows additional assert functions like assertTrue and assertIn.
        """

        self.assertTrue(1 == 1) # value identity
        self.assertFalse(1 == 2)
        self.assertIs(None, None) # object identity
        self.assertIsNot(None, 1)
        self.assertIn(3, [1, 2, 3, 4]) # checking if 3 is in [1, 2, 3, 4]
        self.assertNotIn(5, [1, 2, 3, 4]) # checking if 5 is not in [1, 2, 3, 4]

    def test_add_parametrized(self):
        """
        Using subTest to test multiple cases with the same test function.
        """
        test_cases = [(3, 2, 5), (-1, 1, 0), (0, 0, 0), (10, -10, 0)] 
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(MathUtils.add(a, b), expected)


if __name__ == "__main__":
    unittest.main()