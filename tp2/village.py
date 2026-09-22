"""Module definissant la classe Village avec composition et aggregation."""

from habitant import Habitant


# Explication (Exercice 5, question 3) :
# ajouter_habitant_composition illustre une relation de composition car le
# village cree et possede directement l'objet Habitant, qui depend du cycle
# de vie du village. En revanche, ajouter_habitant_agregation illustre une
# relation d'agregation car l'objet Habitant existe independamment a l'exterieur
# et peut etre partage simultanement entre plusieurs villages sans leur appartenir exclusivement.


class Village:
    """Classe representant un village regroupant des habitants."""

    def __init__(self, nom):
        """Initialise un village avec un nom et une liste vide d'habitants."""
        self._nom = nom
        self._habitants = []

    def get_nom(self):
        """Renvoie le nom du village."""
        return self._nom

    def get_habitants(self):
        """Renvoie la liste des habitants du village."""
        return self._habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """Cree un nouvel Habitant et l'ajoute a la liste (composition)."""
        nouvel_habitant = Habitant(nom, age, adresse, animaux)
        self._habitants.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute un Habitant deja existant a la liste (agregation)."""
        self._habitants.append(habitant)

    def afficher_habitants(self):
        """Affiche les informations de chaque habitant du village."""
        for hab in self._habitants:
            hab.affichage_adresse()


if __name__ == "__main__":
    # Tests demandes par l'enonce
    pytown = Village("PyTown")
    pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

    elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
    pytown.ajouter_habitant_agregation(elise)

    autre_village = Village("VillageVoisin")
    autre_village.ajouter_habitant_agregation(elise)  # meme habitant dans 2 villages

    assert len(pytown.get_habitants()) == 2
    assert elise in autre_village.get_habitants()

    print("Affichage des habitants de PyTown :")
    pytown.afficher_habitants()

    print("Exercice 5 valide avec succes !")
