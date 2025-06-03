# Guide de la Syntaxe Python

Ce guide présente les éléments essentiels de la syntaxe Python pour débuter en programmation.

## Table des matières

1. [Variables et Types de données](#variables-et-types-de-données)
2. [Opérateurs](#opérateurs)
3. [Structures conditionnelles](#structures-conditionnelles)
4. [Boucles](#boucles)
5. [Fonctions](#fonctions)
6. [Structures de données](#structures-de-données)
7. [Gestion des erreurs](#gestion-des-erreurs)
8. [Modules et imports](#modules-et-imports)

## Variables et Types de données

### Déclaration de variables
```python
# Python est un langage à typage dynamique
nom = "Alice"
age = 25
taille = 1.65
est_etudiant = True
```

### Types de données principaux
```python
# Entier (int)
nombre = 42

# Flottant (float)
prix = 19.99

# Chaîne de caractères (str)
message = "Bonjour le monde!"
texte_multiligne = """Ceci est un texte
qui s'étend sur
plusieurs lignes"""

# Booléen (bool)
actif = True
inactif = False

# None (équivalent de null)
valeur_vide = None
```

## Opérateurs

### Opérateurs arithmétiques
```python
a = 10
b = 3

addition = a + b        # 13
soustraction = a - b    # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
division_entiere = a // b  # 3
modulo = a % b          # 1
puissance = a ** b      # 1000
```

### Opérateurs de comparaison
```python
x = 5
y = 10

egal = x == y           # False
different = x != y      # True
inferieur = x < y       # True
superieur = x > y       # False
inferieur_egal = x <= y # True
superieur_egal = x >= y # False
```

### Opérateurs logiques
```python
a = True
b = False

et = a and b    # False
ou = a or b     # True
non = not a     # False
```

## Structures conditionnelles

### If, elif, else
```python
age = 18

if age < 13:
    print("Enfant")
elif age < 18:
    print("Adolescent")
else:
    print("Adulte")
```

### Opérateur ternaire
```python
age = 20
statut = "majeur" if age >= 18 else "mineur"
```

## Boucles

### Boucle for
```python
# Itération sur une liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Boucle avec range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range avec début et fin
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# Range avec pas
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Boucle while
```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# Boucle infinie avec break
while True:
    reponse = input("Continuer? (o/n): ")
    if reponse == 'n':
        break
```

### Continue et break
```python
for i in range(10):
    if i == 3:
        continue  # Passer à l'itération suivante
    if i == 7:
        break     # Sortir de la boucle
    print(i)
```

## Fonctions

### Définition et appel
```python
def saluer(nom):
    return f"Bonjour {nom}!"

message = saluer("Alice")
print(message)
```

### Paramètres par défaut
```python
def calculer_aire(longueur, largeur=1):
    return longueur * largeur

aire1 = calculer_aire(5)      # largeur = 1 par défaut
aire2 = calculer_aire(5, 3)   # largeur = 3
```

### Arguments variables
```python
def somme(*nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    return total

resultat = somme(1, 2, 3, 4, 5)  # 15
```

### Arguments nommés
```python
def presenter(nom, age, ville="Paris"):
    return f"{nom}, {age} ans, habite à {ville}"

info = presenter(nom="Bob", age=30, ville="Lyon")
```

## Structures de données

### Listes
```python
# Création
ma_liste = [1, 2, 3, 4, 5]
liste_mixte = [1, "texte", 3.14, True]

# Accès aux éléments
premier = ma_liste[0]   # 1
dernier = ma_liste[-1]  # 5

# Méthodes utiles
ma_liste.append(6)      # Ajouter à la fin
ma_liste.insert(0, 0)   # Insérer à l'index 0
ma_liste.remove(3)      # Supprimer la première occurrence de 3
element = ma_liste.pop() # Supprimer et retourner le dernier élément
```

### Tuples
```python
# Immuables (non modifiables)
coordonnees = (10, 20)
couleurs = ("rouge", "vert", "bleu")

# Déballage
x, y = coordonnees
```

### Dictionnaires
```python
# Création
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès aux valeurs
nom = personne["nom"]
age = personne.get("age", 0)  # 0 si la clé n'existe pas

# Modification
personne["age"] = 26
personne["profession"] = "Développeuse"

# Parcours
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")
```

### Sets
```python
# Ensemble d'éléments uniques
nombres = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Opérations
nombres.add(5)
nombres.remove(1)
```

## Gestion des erreurs

### Try, except, finally
```python
try:
    nombre = int(input("Entrez un nombre: "))
    resultat = 10 / nombre
    print(f"Résultat: {resultat}")
except ValueError:
    print("Veuillez entrer un nombre valide")
except ZeroDivisionError:
    print("Division par zéro impossible")
except Exception as e:
    print(f"Une erreur s'est produite: {e}")
finally:
    print("Bloc finally toujours exécuté")
```

## Modules et imports

### Import simple
```python
import math

racine = math.sqrt(16)
pi = math.pi
```

### Import avec alias
```python
import datetime as dt

maintenant = dt.datetime.now()
```

### Import spécifique
```python
from math import sqrt, pi

racine = sqrt(25)
```

### Import tout (à éviter)
```python
from math import *
```

## Conseils et bonnes pratiques

### Conventions de nommage
- Variables et fonctions : `snake_case`
- Constantes : `MAJUSCULES`
- Classes : `PascalCase`

### Commentaires
```python
# Commentaire sur une ligne

"""
Commentaire sur
plusieurs lignes
ou docstring
"""

def ma_fonction():
    """
    Description de la fonction
    """
    pass
```

### Compréhensions de listes
```python
# Création d'une liste avec une boucle
carres = [x**2 for x in range(10)]

# Avec condition
pairs = [x for x in range(20) if x % 2 == 0]
```

### F-strings (formatage moderne)
```python
nom = "Alice"
age = 25
message = f"Je m'appelle {nom} et j'ai {age} ans"
```

## Ressources utiles

- [Documentation officielle Python](https://docs.python.org/fr/)
- [PEP 8 - Guide de style](https://peps.python.org/pep-0008/)
- [Python.org - Tutoriel officiel](https://docs.python.org/fr/tutorial/)

---

Ce guide couvre les bases essentielles de Python. Pour approfondir vos connaissances, explorez les concepts avancés comme les classes, les décorateurs, les générateurs et la programmation orientée objet.