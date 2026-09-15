"""Gestion relevés capteurs robot."""


def afficher_releve(releve):
    """Formate un relevé capteur en chaîne de caractères."""
    nom_capteur, valeur, unite = releve
    return f"Capteur {nom_capteur} : {valeur} {unite}"


def recalibrer(releves, nom_capteur_cible, nouvelle_valeur):
    """Crée nouvelle liste relevés avec valeur mise à jour pour un capteur."""
    return [
        (nom, nouvelle_valeur, unite) if nom == nom_capteur_cible else (nom, valeur, unite)
        for nom, valeur, unite in releves
    ]


if __name__ == "__main__":
    releve1 = ("laser_avant", 2.35, "m")
    releve2 = ("laser_arriere", 1.10, "m")
    releve3 = ("gyroscope", 87.5, "deg")
    releves = [releve1, releve2, releve3]

    assert len(releves) == 3
    assert releves[0][0] == "laser_avant"
    assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

    nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
    assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
    assert nouveaux_releves[1] == releve2
    assert nouveaux_releves[2] == releve3

    # Test supplémentaire : recalibrer un capteur inexistant
    releves_copy = releves.copy()
    resultats_inexistant = recalibrer(releves, "capteur_inexistant", 99.9)
    assert resultats_inexistant == releves_copy
    assert releves == releves_copy  # Vérifier que l'original n'a pas changé

    # Test supplémentaire : recalibrer le dernier capteur
    nouveaux_releves2 = recalibrer(releves, "gyroscope", 45.0)
    assert nouveaux_releves2[0] == releve1
    assert nouveaux_releves2[1] == releve2
    assert nouveaux_releves2[2] == ("gyroscope", 45.0, "deg")

    print("Tous les tests de l'exercice 3 sont passés.")
