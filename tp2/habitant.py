"""Module definissant la classe abstraite Habitant."""

from abc import ABC, abstractmethod
from multipledispatch import dispatch


class Habitant(ABC):
    """Classe abstraite representant un habitant."""

    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant."""
        self._nom = nom
        self._adresse = adresse
        self._animaux = {} if animaux is None else animaux
        self.age = age

    def __str__(self):
        """Representation textuelle d'un habitant."""
        return f"{self.get_nom()}, {self.get_age()} ans, habite a {self.get_adresse()}"

    @property
    def age(self):
        """Getter de age."""
        return self._age

    @age.setter
    def age(self, nouvelle_valeur):
        """Setter de age."""
        if nouvelle_valeur < 0 or nouvelle_valeur > 130:
            raise ValueError("L'age doit etre compris entre 0 et 130.")
        self._age = nouvelle_valeur

    def get_nom(self):
        """Renvoie le nom."""
        return self._nom

    def set_nom(self, nom):
        """Modifie le nom."""
        self._nom = nom

    def get_age(self):
        """Renvoie l'age."""
        return self._age

    def set_age(self, age):
        """Modifie l'age."""
        self.age = age

    def get_adresse(self):
        """Renvoie l'adresse."""
        return self._adresse

    def set_adresse(self, adresse):
        """Modifie l'adresse."""
        self._adresse = adresse

    def get_animaux(self):
        """Renvoie les animaux."""
        return self._animaux

    def set_animaux(self, animaux):
        """Modifie les animaux."""
        self._animaux = animaux

    def affichage_adresse(self):
        """Affiche l'adresse."""
        print(f"{self.get_nom()} habite a {self.get_adresse()}")

    def compte_animal(self, animal):
        """Renvoie le compte d'un animal."""
        return self.get_animaux().get(animal, 0)

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Methode abstraite calculant la retraite."""


# pylint: disable=function-redefined
@dispatch(object, str)
def set_info(habitant, nom):
    """Met a jour le nom."""
    habitant.set_nom(nom)


@dispatch(object, str, int)
def set_info(habitant, nom, age):
    """Met a jour le nom et l'age."""
    habitant.set_nom(nom)
    habitant.set_age(age)
