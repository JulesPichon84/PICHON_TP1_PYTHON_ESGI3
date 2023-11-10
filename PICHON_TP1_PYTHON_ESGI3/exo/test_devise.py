# Importation du module unittest pour effectuer des tests unitaires.
import unittest
from devise import convertir_devises

class TestConvertisseurDeDevises(unittest.TestCase):
    
    def test_convertir_devises(self):
        # Testez la conversion de devises avec des taux connus.
        result = convertir_devises(100, 'euro', 'dollar')  # 100 euros en dollars.
        self.assertAlmostEqual(result, 104.9, places=1)  # Utilisation de `assertAlmostEqual` pour gérer les arrondis.
        
        result = convertir_devises(50, 'dollar', 'euro')  # 50 dollars en euros.
        self.assertAlmostEqual(result, 47.5, places=1)
        
        result = convertir_devises(75, 'livre', 'yen')  # 75 livres en yens.
        self.assertAlmostEqual(result, 13650.0, places=1)
        
    def test_erreur_conversion_non_prise_en_charge(self):
        # Teste une conversion non prise en charge.
        with self.assertRaises(ValueError):
            convertir_devises(100, 'euro', 'inconnu')
        
        with self.assertRaises(ValueError):
            convertir_devises(100, 'inconnu', 'euro')
        
if __name__ == "__main__":
    unittest.main()
