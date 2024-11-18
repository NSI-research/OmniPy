# OmniPy

**OmniPy** est une bibliothèque Python polyvalente qui regroupe des structures de données, des algorithmes de tri, et des utilitaires mathématiques et textuels. Elle est conçue pour fournir un ensemble d'outils essentiels dans un module simple et efficace.

## 🚀 Fonctionnalités

- **Structures de données** :
  - `pile` : Simule une pile (stack) avec les opérations classiques (`add`, `remove`, etc.).
  - `file` : Implémente une file (queue) avec logique FIFO.
  - `node` : Gestion de nœuds avec pointeur.

- **Algorithmes de tri** :
  - Tri par insertion.
  - Tri par sélection.
  - Tri par fusion.

- **Outils mathématiques** :
  - PGCD et PPCM.
  - Génération de la suite de Fibonacci.
  - Test de primalité (Miller-Rabin).
  - Dérivée numérique.

- **Utilitaires textuels** :
  - Vérification des parenthèses équilibrées.
  - Analyse de fréquence des lettres et des mots.
  - Générateur de mots de passe aléatoires.

- **Statistiques** :
  - Calcul de la moyenne.
  - Calcul de la médiane.

## 🛠️ Installation

### Télécharger ou cloner le dépôt

Clonez le dépôt depuis l'organisation GitHub [NSI-research](https://github.com/NSI-research) avec la commande suivante :

```bash
git clone https://github.com/NSI-research/OmniPy.git
```

Ensuite, ajoutez simplement le fichier à votre projet et importez les classes ou fonctions nécessaires.

## 📖 Utilisation

### Exemple : Utiliser une pile

```python
from OmniPy import pile

ma_pile = pile()
ma_pile.add(10)
ma_pile.add(20)
print(ma_pile.peek())  # Renvoie 20
ma_pile.remove()
print(ma_pile.lenp())  # Renvoie 1
```

### Exemple : Générer un mot de passe

```python
from OmniPy import generateur_pwd

print(generateur_pwd(12))  # Renvoie un mot de passe aléatoire
```
