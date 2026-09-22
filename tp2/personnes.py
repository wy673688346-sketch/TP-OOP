"""Module definissant les classes derivees Adulte et Enfant et le polymorphisme."""

from habitant import Habitant


# Explication (Exercice 8, question 3) :
# Rendre la methode abstraite garantit a l'instanciation que chaque sous-classe
# implemente sa version, empechant tout appel silencieux a une fonction vide.


class Adulte(Habitant):
    """Classe representant un habitant adulte."""

    def __init__(self, nom, prenom, age, adresse, animaux=None):
        """Initialise un adulte."""
        super().__init__(f"{prenom} {nom}", age, adresse, animaux)
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")

    def calcul_nombre_annee_avant_retraite(self):
        """Calcule les annees avant retraite pour un adulte."""
        if self.age >= 62:
            return "Deja a la retraite"
        return 62 - self.age


class Enfant(Habitant):
    """Classe representant un habitant enfant."""

    def __init__(self, nom, prenom, age, adresse, animaux=None):
        """Initialise un enfant."""
        super().__init__(f"{prenom} {nom}", age, adresse, animaux)
        if age >= 18:
            raise ValueError("Un enfant doit avoir strictement moins de 18 ans.")

    def calcul_nombre_annee_avant_retraite(self):
        """Calcule les annees avant retraite pour un enfant."""
        return "Erreur: un enfant ne peut pas calculer sa retraite"


def affichage(habitant: Habitant):
    """Affiche un habitant via le polymorphisme sans verification de type."""
    print(str(habitant))


if __name__ == "__main__":
    adulte = Adulte("Dupont", "Marie", 35, "Rue A")
    enfant = Enfant("Martin", "Lucas", 12, "Rue B")

    assert str(adulte) == "Marie Dupont, 35 ans, habite a Rue A"
    assert str(enfant) == "Lucas Martin, 12 ans, habite a Rue B"

    affichage(adulte)
    affichage(enfant)

    print("Exercice 8 valide avec succes !")
