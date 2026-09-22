"""Module definissant la classe Habitant du village."""


class Habitant:
    """Classe representant un habitant avec ses attributs et ses animaux."""

    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant."""
        self.nom = nom
        self.age = age
        self.adresse = adresse
        if animaux is None:
            self.animaux = {}
        else:
            self.animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant."""
        print(f"{self.nom} habite a {self.adresse}")

    def compte_animal(self, animal):
        """Renvoie le nombre d'animaux du type donne possedes par l'habitant."""
        return self.animaux.get(animal, 0)


if __name__ == "__main__":
    h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
    assert h1.nom == "Aldric"
    assert h1.compte_animal("vaches") == 3
    assert h1.compte_animal("moutons") == 0
    h1.affichage_adresse()
    print("Exercice 3 valide avec succes !")
