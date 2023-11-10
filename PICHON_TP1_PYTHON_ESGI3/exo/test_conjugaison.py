# Importation du module unittest pour effectuer des tests unitaires.
import unittest
from conjugaison import bescherelle

class TestBescherelle(unittest.TestCase):
    # Testez la conjugaison d'un verbe connu
    def test_bescherelle(self):
        result = bescherelle("manger")  # Conjugue le verbe "manger".
        self.assertIn("manger", result)  # On s'assure que le verbe "manger" est dans le résultat.
        
        result = bescherelle("aimer")  # Conjugue le verbe "aimer".
        self.assertIn("aimer", result)  # On s'assure que le verbe "aimer" est dans le résultat.
        
    def test_erreur_entree_non_valide(self):
        # Testez une entrée non valide (par exemple, un verbe vide)
        with self.assertRaises(Exception):
            bescherelle("")
        
        # Testez une entrée non valide (par exemple, un verbe inexistant)
        with self.assertRaises(Exception):
            bescherelle("xyz123")
        
if __name__ == "__main__":
    unittest.main()
