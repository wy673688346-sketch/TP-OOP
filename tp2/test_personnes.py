"""Module de tests unitaires pour les classes Adulte et Enfant."""

import unittest
from personnes import Adulte, Enfant


class TestPersonnes(unittest.TestCase):
    """Cas de tests unitaires pour verifier le comportement des classes."""

    def test_adulte_retraite(self):
        """Teste le calcul des annees de retraite pour un adulte."""
        adulte1 = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(adulte1.calcul_nombre_annee_avant_retraite(), 27)

        adulte2 = Adulte("Durand", "Pierre", 65, "Rue B")
        self.assertEqual(adulte2.calcul_nombre_annee_avant_retraite(), "Deja a la retraite")

    def test_adulte_age_invalide(self):
        """Verifie qu'une exception est levee si un adulte a moins de 18 ans."""
        with self.assertRaises(ValueError):
            Adulte("Ado", "Jean", 16, "Rue C")

    def test_enfant_retraite(self):
        """Verifie le message de retour pour le calcul de retraite d'un enfant."""
        enfant = Enfant("Martin", "Lucas", 12, "Rue D")
        resultat = enfant.calcul_nombre_annee_avant_retraite()
        self.assertIn("enfant", resultat)

    def test_enfant_age_invalide(self):
        """Verifie qu'une exception est levee si un enfant a 18 ans ou plus."""
        with self.assertRaises(ValueError):
            Enfant("Grand", "Paul", 19, "Rue E")


if __name__ == "__main__":
    unittest.main()
