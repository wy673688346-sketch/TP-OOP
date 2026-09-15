"""Tests unitaires pour les fonctions du TP."""
import unittest

from tuples import afficher_releve, recalibrer
from ensembles import robots_double_mission, ajouter_robot_mission
from dictionnaires import consommer_piece, total_pieces


class TestJournalDeBord(unittest.TestCase):
    """Tests sur les fonctions de relevés capteurs."""
    def test_recalibrer_capteur_existant(self):
        releves = [("laser_avant", 2.35, "m"), ("gyroscope", 87.5, "deg")]
        res = recalibrer(releves, "laser_avant", 2.40)
        self.assertEqual(res[0], ("laser_avant", 2.40, "m"))

    def test_recalibrer_capteur_absent(self):
        releves = [("laser_avant", 2.35, "m")]
        res = recalibrer(releves, "inconnu", 10.0)
        self.assertEqual(res, releves)


class TestFlotteRobots(unittest.TestCase):
    """Tests fonctions gestion flotte robots."""
    def test_robots_double_mission(self):
        exp = {"R5", "R7"}
        res = robots_double_mission({"R2", "R5", "R7"}, {"R5", "R9", "R7"})
        self.assertEqual(res, exp)

    def test_ajouter_robot_deja_present(self):
        ens = {"R2", "R5"}
        res = ajouter_robot_mission(ens, "R2")
        self.assertEqual(res, {"R2", "R5"})


class TestInventaire(unittest.TestCase):
    """Tests fonctions inventaire pièces."""
    def test_consommer_piece(self):
        stock = {"ModeleA": {"moteurs": 10, "capteurs":20, "roues":30}}
        consommer_piece(stock, "ModeleA", "moteurs", 3)
        self.assertEqual(stock["ModeleA"]["moteurs"],7)

    def test_total_pieces_stock_vide(self):
        res = total_pieces({})
        self.assertEqual(res, {"moteurs":0, "capteurs":0, "roues":0})


if __name__ == "__main__":
    unittest.main(verbosity=2)