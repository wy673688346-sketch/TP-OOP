# TP-OOP

Dépôt de travaux pratiques pour l'apprentissage de la programmation orientée objet en Python.

## 📁 Contenu du dossier `tp0/`

Le dossier `tp0/` contient des exercices fondamentaux de Python :

| Fichier | Description |
|---------|-------------|
| `tuples.py` | Gestion des relevés capteurs avec tuples — opérations de formatage et recalibration |
| `ensembles.py` | Manipulation des ensembles (set) — opérations d'union, intersection, différence |
| `dictionnaires.py` | Travail avec les dictionnaires — stockage et récupération de données structurées |
| `qualite.py` | Vérification de la qualité du code — analyse et validation des bonnes pratiques |
| `test.py` | Suite de tests unitaires — validation globale des exercices |

## 🛠️ Configuration de l'environnement

### Prérequis

- **Conda** ou **Miniconda** (optionnel : un script `Miniconda3-latest-Linux-x86_64.sh` est fourni)

### Activation de l'environnement `tp_oop`

```bash
# Activer l'environnement conda
conda activate tp_oop

# Vérifier que l'environnement est actif (le prompt affiche "(tp_oop)")
python --version  # Devrait afficher Python 3.11.x
```

### Création de l'environnement (si nécessaire)

```bash
conda env create -f environment.yml
```

## 🧪 Lancer les tests unitaires

Une fois l'environnement activé, exécutez les tests :

```bash
# Exécuter tous les tests du dossier tp0
python tp0/test.py

# Exécuter les tests d'un exercice spécifique
python tp0/tuples.py
python tp0/ensembles.py
python tp0/dictionnaires.py
```

### Résultat attendu

Si tous les tests passent, vous verrez des messages comme :
```
Tous les tests de l'exercice X sont passés.
```

## 📋 Vérification de la qualité du code

Utilisez le linter `pylint` pour vérifier la qualité du code :

```bash
pylint tp0/*.py
```

## 📝 Notes

- Les fichiers d'exercices contiennent des tests unitaires inline (bloc `if __name__ == "__main__"`)
- Chaque exercice est indépendant et peut être exécuté séparément
- L'environnement conda inclut les outils de développement : `pylint`, `astroid`, `isort`

## 📞 Support

Pour toute question ou problème :
- Vérifiez que l'environnement est activé : `conda activate tp_oop`
- Exécutez les tests pour identifier les erreurs
- Consultez les docstrings des fonctions pour comprendre les spécifications

## Exercice 8 : Retour sur GitHub Copilot
### 8.2 Remarques sur la fonction recalibrer
#### Points positifs
✓ List comprehension pythonique — L'utilisation de la list comprehension est idiomatique et efficace
✓ Pas de modification in-place — La fonction crée une nouvelle liste, préservant les données originales
✓ Logique correcte — Le tuple unpacking et la condition ternaire fonctionnent bien
✓ Complexité O(n) — Parcourt la liste une seule fois
✓ Robuste aux cas limites — Gère correctement si le capteur n'existe pas ou si la liste est vide

#### Points à améliorer
- Docstring trop minimaliste — Elle ne décrit pas les paramètres ni la valeur de retour. Exemple attendu : releves est une liste de tuples (nom, valeur, unite)
- Pas d'annotations de type — Ajouter des type hints améliorerait la lisibilité et la maintenabilité
- Comportement implicite — Si le capteur n'existe pas, la fonction ne le signale pas (silencieusement ignoré). Selon vos besoins, une validation ou une exception pourrait être utile
- Petite optimisation possible : Si vous avez besoin de recalibrer plusieurs capteurs, il serait plus efficace de passer un dictionnaire {nom: nouvelle_valeur} au lieu d'appeler la fonction plusieurs fois

### 8.3 Test unitaire supplémentaire
Le test généré par Copilot a été ajouté directement dans `tests.py`.
> Résultat du test : Le test passe sans erreur.
> Observation : Il couvre le cas d'une liste vide de relevés, un cas limite que je n'avais pas prévu initialement.

### 8.5 Message de commit généré par Copilot
> Observation : Copilot propose un message concis, mais il reste moins précis qu'un message écrit manuellement, car il ne détaille pas le contexte du TP.

### 8.6 Réflexion
GitHub Copilot est très utile pour analyser du code existant et proposer des tests unitaires. En revanche, il faut toujours vérifier ses suggestions, car il peut proposer des améliorations non nécessaires pour les consignes du TP. C'est un bon outil d'aide, mais il ne remplace pas la réflexion personnelle.
