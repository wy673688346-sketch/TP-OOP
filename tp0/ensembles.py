"""Opérations sur ensembles de robots."""


def robots_double_mission(robots_exploration, robots_transport):
    """Retourne robots présents dans les deux missions."""
    return robots_exploration & robots_transport


def robots_toutes_missions(robots_exploration, robots_transport):
    """Retourne tous les robots des deux missions."""
    return robots_exploration | robots_transport


def robots_exploration_seulement(robots_exploration, robots_transport):
    """Retourne robots uniquement en exploration."""
    return robots_exploration - robots_transport


def ajouter_robot_mission(robots_mission, robot_ajoute):
    """Retourne nouvel ensemble avec robot ajouté, ne modifie pas l'original."""
    return robots_mission | {robot_ajoute}


def retirer_robot_mission(robots_mission, robot_retire):
    """Retourne nouvel ensemble sans robot, ne modifie pas l'original."""
    return robots_mission - {robot_retire}


if __name__ == "__main__":
    robots_exploration = {"R2", "R5", "R7"}
    robots_transport = {"R5", "R9", "R7", "R3"}

    double_mission = robots_double_mission(robots_exploration, robots_transport)
    toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
    exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

    assert double_mission == {"R5", "R7"}
    assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
    assert exploration_seule == {"R2"}

    ajout = ajouter_robot_mission(robots_exploration, "R8")
    retrait = retirer_robot_mission(robots_transport, "R9")

    assert ajout == {"R2", "R5", "R7", "R8"}
    assert retrait == {"R3", "R5", "R7"}
    assert robots_transport == {"R5", "R9", "R7", "R3"}

    print("Tous les tests de l'exercice 4 sont passés.")
