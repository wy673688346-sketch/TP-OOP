"""Module definissant les classes derivees Adulte et Enfant."""

from habitant import Habitant


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


if __name__ == "__main__":
    try:
        # pylint: disable=abstract-class-instantiated
        Habitant("Test", 20, "Rue X")
        assert False, "L'instanciation directe de Habitant aurait du echouer"
    except TypeError:
        pass

    adulte = Adulte("Dupont", "Marie", 35, "Rue A")
    enfant = Enfant("Martin", "Lucas", 12, "Rue B")

    assert isinstance(adulte, Habitant)
    assert adulte.calcul_nombre_annee_avant_retraite() == 27
    assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

    try:
        Enfant("Oups", "Jean", 25, "Rue C")
        assert False, "une ValueError aurait du etre levee"
    except ValueError:
        pass

    print("Exercice 7 valide avec succes !")
