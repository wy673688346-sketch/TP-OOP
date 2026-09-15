"""Gestion stock pièces robots."""


def quantite_piece(pieces_stock, modele, nom_piece):
    """Renvoie quantité d'une pièce pour un modèle donné."""
    return pieces_stock[modele][nom_piece]


def consommer_piece(pieces_stock, modele, nom_piece, quantite):
    """Décrémente stock d'une pièce après réparation."""
    pieces_stock[modele][nom_piece] -= quantite


def ajouter_modele(pieces_stock, modele, moteurs, capteurs, roues):
    """Ajoute nouveau modèle robot au stock."""
    pieces_stock[modele] = {
        "moteurs": moteurs,
        "capteurs": capteurs,
        "roues": roues
    }


def total_pieces(pieces_stock):
    """Calcule somme totale des pièces tous modèles confondus."""
    totaux = {"moteurs": 0, "capteurs": 0, "roues": 0}
    for stock in pieces_stock.values():
        totaux["moteurs"] += stock["moteurs"]
        totaux["capteurs"] += stock["capteurs"]
        totaux["roues"] += stock["roues"]
    return totaux


if __name__ == "__main__":
    pieces_stock = {
        "ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
        "ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
    }

    assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10

    consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
    assert pieces_stock["ModeleA"]["moteurs"] == 7

    ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
    assert pieces_stock["ModeleC"] == {"moteurs": 4, "capteurs": 10, "roues": 16}

    totaux = total_pieces(pieces_stock)
    assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}

    assert total_pieces({}) == {"moteurs": 0, "capteurs": 0, "roues": 0}

    print("Tous les tests de l'exercice 5 sont passés.")
