# Importation du module unittest pour effectuer des tests unitaires.
import unittest
from factorielle import somme, factorielle

class TestFactorielle(unittest.TestCase):
    def test_somme(self):
        pass
    def test_factorielle(self):
        pass

if __name__ == "__main__":
    unittest.main()