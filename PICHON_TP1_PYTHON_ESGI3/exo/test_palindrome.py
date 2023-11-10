# Importation du module unittest pour effectuer des tests unitaires.
import unittest
from palindrome import est_palindrome, traitement_mot

class TestPalindromeFunctions(unittest.TestCase):
    def test_est_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertTrue(est_palindrome("civic"))
        self.assertFalse(est_palindrome("hello"))
        self.assertTrue(est_palindrome("A man a plan a canal Panama"))
        self.assertTrue(est_palindrome("Was it a car or a cat I saw?"))

    def test_traitement_mot(self):
        self.assertEqual(traitement_mot("Radar"), "radar")
        self.assertEqual(traitement_mot("A man, a plan, a canal, Panama!"), "amanaplanacanalpanama")
        self.assertEqual(traitement_mot("Hello!"), "hello")
        self.assertEqual(traitement_mot("Test1"), "test1")
        with self.assertRaises(ValueError):
            traitement_mot("Test@123")  # Vérifie que ValueError est levée pour les caractères spéciaux.

if __name__ == '__main__':
    unittest.main()
