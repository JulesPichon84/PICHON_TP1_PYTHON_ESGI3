# Importation du module unittest pour effectuer des tests unitaires.
import unittest
from calculatrice import addition, multiplication, division, soustraction

class TestCalculatrice(unittest.TestCase):
    # Test de la fonction addition.
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(0, 0), 0)
    # Test de la fonction soustraction.
    def test_soustraction(self):
        self.assertEqual(soustraction(5, 2), 3)
        self.assertEqual(soustraction(1, 1), 0)
        self.assertEqual(soustraction(0, 5), -5)
    # Test de la fonction multiplication.
    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(5, 0), 0)
        self.assertEqual(multiplication(4, -2), -8)
    # Test de la fonction division.
    def test_division(self):
        self.assertEqual(division(6, 2), 3)
        self.assertEqual(division(5, 0), ValueError)
        self.assertEqual(division(0, 4), 0.0)
        
if __name__ == "__main__":
    unittest.main()
