"""Module definissant la classe Habitant avec encapsulation et surcharge."""

from multipledispatch import dispatch


class Habitant:
    """Classe representant un habitant avec attributs prives et proprietes."""

    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant avec validation de l'age."""
        self._nom = nom
        self._adresse = adresse
        if animaux is None:
            self._animaux = {}
        else:
            self._animaux = animaux
        self.age = age

    @property
    def age(self):
        """Getter de la propriete age."""
        return self._age

    @age.setter
    def age(self, nouvelle_valeur):
        """Setter de age validant l'intervalle [0, 130]."""
        if nouvelle_valeur < 0 or nouvelle_valeur > 130:
            raise ValueError("L'age doit etre compris entre 0 et 130.")
        self._age = nouvelle_valeur

    def get_nom(self):
        """Renvoie le nom de l'habitant."""
        return self._nom

    def set_nom(self, nom):
        """Modifie le nom de l'habitant."""
        self._nom = nom

    def get_age(self):
        """Renvoie l'age de l'habitant."""
        return self._age

    def set_age(self, age):
        """Modifie l'age en utilisant la propriete securisee."""
        self.age = age

    def get_adresse(self):
        """Renvoie l'adresse de l'habitant."""
        return self._adresse

    def set_adresse(self, adresse):
        """Modifie l'adresse de l'habitant."""
        self._adresse = adresse

    def get_animaux(self):
        """Renvoie le dictionnaire d'animaux."""
        return self._animaux

    def set_animaux(self, animaux):
        """Modifie le dictionnaire d'animaux."""
        self._animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant."""
        print(f"{self.get_nom()} habite a {self.get_adresse()}")

    def compte_animal(self, animal):
        """Renvoie le nombre d'animaux du type donne."""
        return self.get_animaux().get(animal, 0)


# --- Surcharge de set_info avec multipledispatch (Exercice 6) ---
@dispatch(object, str)
def set_info(habitant, nom):
    """Met a jour uniquement le nom de l'habitant."""
    habitant.set_nom(nom)


@dispatch(object, str, int)
def set_info(habitant, nom, age):
    """Met a jour le nom et l'age de l'habitant."""
    habitant.set_nom(nom)
    habitant.set_age(age)


if __name__ == "__main__":
    # Tests Exercice 3 & 4
    h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})
    assert h1.get_nom() == "Aldric"
    assert h1.compte_animal("vaches") == 3
    assert h1.compte_animal("moutons") == 0
    h1.affichage_adresse()

    h1.age = 26
    assert h1.age == 26

    # Tests Exercice 6
    h2 = Habitant("Bob", 40, "Rue C")
    set_info(h2, "Robert")
    assert h2.get_nom() == "Robert"
    assert h2.get_age() == 40

    set_info(h2, "Robert", 41)
    assert h2.get_nom() == "Robert"
    assert h2.get_age() == 41

    print("Exercice 6 valide avec succes !")
