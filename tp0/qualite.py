"""Calcul coût énergétique déplacement robot."""


def cout_deplacement_propre(type_terrain, x_depart, y_depart, x_arrivee, y_arrivee):
    """Calcule coût énergétique selon type de terrain."""
    distance = ((x_arrivee - x_depart) ** 2 + (y_arrivee - y_depart) ** 2) ** 0.5
    coeff_terrain = {
        'R': 1.0,
        'H': 1.5,
        'S': 2.0
    }
    coeff = coeff_terrain.get(type_terrain, 3.0)
    return distance * coeff


if __name__ == "__main__":
    cout_route = cout_deplacement_propre('R', 0, 0, 3, 4)
    assert abs(cout_route - 5.0) < 1e-6

    cout_sable = cout_deplacement_propre('S', 0, 0, 3, 4)
    assert abs(cout_sable - 10.0) < 1e-6

    cout_terrain_difficile = cout_deplacement_propre('X', 0, 0, 3, 4)
    assert abs(cout_terrain_difficile - 15.0) < 1e-6

    print("Tous les tests de l'exercice 6 sont passés.")
