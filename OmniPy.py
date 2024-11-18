# -------------------
#
#   Date : 2024-09-30
#   Auteur : Lodjo28 / Anto
#   Nom du fichier : Integ
#   Version : 0.1
#
# -------------------

# Imports :
import random  # Module utilisé pour générer des valeurs aléatoires

# Définition de la classe "pile"
class pile():
    """
    Cette classe permet de simuler le fonctionnement d'une pile (stack) via des tableaux (listes Python).
    
    Méthodes disponibles :
    - add(item): Ajoute un élément à la pile.
    - remove(): Retire et renvoie le dernier élément ajouté (sommet de la pile).
    - peek(): Renvoie l'élément au sommet sans l'enlever.
    - lenp(): Renvoie la longueur actuelle de la pile.
    """

    def __init__(self) -> None:
        """Initialise une pile vide."""
        self.content = []
    
    def add(self, item) -> None:
        """Ajoute un élément au sommet de la pile."""
        self.content.append(item)
    
    def remove(self):
        """
        Retire et retourne le dernier élément de la pile.
        Lève une exception IndexError si la pile est vide.
        """
        if len(self.content) > 0:
            return self.content.pop(-1)
        else: 
            print("La pile que vous essayez de dépiler est vide")
            raise IndexError
    
    def peek(self):
        """
        Renvoie l'élément au sommet de la pile sans le retirer.
        Retourne None si la pile est vide.
        """
        if len(self.content) > 0:
            return self.content[-1]
        else:
            print("La pile est vide")
    
    def lenp(self) -> int:
        """Renvoie la taille actuelle de la pile."""
        return len(self.content)

# Définition de la classe "file"
class file():
    """
    Cette classe implémente une file (queue) en utilisant une liste Python.
    Une file suit une logique FIFO (First In, First Out).
    """

    def __init__(self) -> None:
        """Initialise une file vide."""
        self.content = []
    
    def add(self, item) -> None:
        """Ajoute un élément à la fin de la file."""
        self.content.append(item)
    
    def remove(self):
        """
        Retire et renvoie le premier élément de la file.
        Lève une exception IndexError si la file est vide.
        """
        if len(self.content) > 0:
            return self.content.pop(0)
        else: 
            print("La file que vous essayez de dépiler est vide")
            raise IndexError
    
    def lenf(self) -> int:
        """Renvoie la taille actuelle de la file."""
        return len(self.content)

# Définition de la classe "node"
class node():
    """
    Cette classe représente un nœud qui peut contenir des éléments accessibles via un index.
    Elle simule un système d'itération avec un pointeur (index).
    """

    def __init__(self) -> None:
        """Initialise un nœud avec une liste contenant un élément vide."""
        self.content = [None]
        self.index = 0

    def pick(self):
        """Renvoie l'élément actuellement pointé par l'index."""
        return self.content[self.index]
    
    def insert(self, item) -> None:
        """Insère un élément à l'index courant."""
        self.content.insert(self.index, item)
    
    def next(self) -> None:
        """
        Avance l'index vers l'élément suivant.
        Affiche un message d'erreur si l'index dépasse les limites.
        """
        if len(self.content) - 1 > self.index:
            self.index += 1
        else:
            print("Impossible d'aller plus loin")
    
    def previous(self) -> None:
        """
        Recule l'index vers l'élément précédent.
        Affiche un message d'erreur si l'index est déjà au début.
        """
        if self.index - 1 >= 0:
            self.index -= 1
        else:
            print("Impossible d'aller plus loin")

# Fonction pour trier le contenu d'une liste (insertion)
def tri_insertion(liste):
    """
    Trie une liste en utilisant l'algorithme du tri par insertion.

    Arguments :
    - liste : Liste d'éléments à trier.

    Retourne :
    - La liste triée.
    """
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1

        # Déplace les éléments plus grands que 'key' d'une position vers la droite
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1

        # Place 'key' à sa position correcte
        liste[j + 1] = key

    return liste

# Fonction pour trier le contenu d'une liste (séléction)
def tri_selection(liste):
    """
    Trie une liste en utilisant l'algorithme du tri par sélection.

    Arguments :
    - liste : Liste d'éléments à trier.

    Retourne :
    - La liste triée.
    """
    n = len(liste)
    for i in range(n):
        # Trouve l'indice du plus petit élément non trié
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        
        # Échange l'élément actuel avec le plus petit trouvé
        liste[i], liste[min_index] = liste[min_index], liste[i]

    return liste

# Fonction pour trier le contenu d'une liste (fusion)
def tri_fusion(liste):
    """
    Trie une liste en utilisant l'algorithme du tri par fusion.

    Arguments :
    - liste : Liste d'éléments à trier.

    Retourne :
    - La liste triée.
    """
    if len(liste) > 1:
        # Divise la liste en deux moitiés
        milieu = len(liste) // 2
        gauche = liste[:milieu]
        droite = liste[milieu:]

        # Trie récursivement les deux moitiés
        tri_fusion(gauche)
        tri_fusion(droite)

        # Fusionne les deux moitiés triées
        i = j = k = 0
        while i < len(gauche) and j < len(droite):
            if gauche[i] < droite[j]:
                liste[k] = gauche[i]
                i += 1
            else:
                liste[k] = droite[j]
                j += 1
            k += 1

        # Ajoute les éléments restants de la moitié gauche
        while i < len(gauche):
            liste[k] = gauche[i]
            i += 1
            k += 1

        # Ajoute les éléments restants de la moitié droite
        while j < len(droite):
            liste[k] = droite[j]
            j += 1
            k += 1

    return liste

# Décorateur pour mise en cache des résultats de fonction
def cache(fonction):
    """
    Ce décorateur permet de mémoriser les résultats d'une fonction pour éviter des calculs répétitifs.
    Utilise un dictionnaire pour stocker les résultats des appels précédents.
    """
    dico = {}
    
    def verify(*args):
        if args in dico.keys():
            return dico[args]
        else:
            result = fonction(*args)
            dico[args] = result
            return result
    
    return verify

# Fonction pour calculer la moyenne d'une liste
def moyenne(liste: list):
    """Calcule et renvoie la moyenne des éléments d'une liste."""
    Somme = 0
    for i in liste:
        Somme += i
    return Somme / len(liste)

# Fonction pour calculer la médiane d'une liste
def mediane(liste: list):
    """
    Calcule et renvoie la médiane d'une liste.
    Trie la liste avant de calculer la médiane.
    """
    liste_trie = tri_fusion(liste)
    if len(liste_trie) % 2 == 0:
        return moyenne([liste_trie[(len(liste_trie)//2)-1], liste_trie[len(liste_trie)//2]])
    else:
        return liste_trie[len(liste_trie)//2]

# Vérification des parenthèses équilibrées
def verif_parentheses(Txt: list) -> bool:
    """
    Vérifie si les parenthèses, crochets et accolades sont correctement équilibrés dans une chaîne.
    Retourne True si c'est le cas, False sinon.
    """
    Ouverture = "([{"
    Fermeture = ")]}"
    Pile = [] # Utilisation d'une pile pour le suivi
    for i in range(len(Txt)):
        if Txt[i] in Ouverture:
            Pile.append(Txt[i])
        elif Txt[i] in Fermeture:
            if Pile[-1] == Ouverture[Fermeture.index(Txt[i])]:
                Pile.pop()
            else:
                return False
    return not Pile # Si la pile est vide, tout est équilibré

# Fonction pour calculer la dérivée numérique d'une fonction donnée
def derivation(fonction, h=1e-10):
    """
    Approche numérique pour calculer la dérivée d'une fonction.
    
    Arguments :
    - fonction : Expression mathématique en tant que chaîne de caractères (e.g., "x**2").
    - h : Pas d'incrémentation utilisé pour calculer la dérivée, par défaut très petit pour une meilleure précision.

    Retourne une fonction représentant la dérivée.
    """
    def fonction_math(x):
        """Évalue la fonction mathématique pour une valeur donnée de x."""
        return eval(fonction)
    
    def fonction_prime(x):
        """Calcule la dérivée en utilisant la méthode des différences finies."""
        return (fonction_math(x + h) - fonction_math(x)) / h

    return fonction_prime

# Analyse de fréquence des lettres et des mots dans un texte
def frequence(text: str):
    """
    Analyse la fréquence des lettres et des mots dans un texte donné.
    Affiche :
    - La lettre la plus fréquente et son nombre d'apparitions.
    - Le mot le plus fréquent et son nombre d'apparitions.
    - Le nombre total de caractères et de mots.

    Arguments :
    - text : Chaîne de caractères à analyser.
    """

    dico = {}  # Fréquence des lettres
    Liste = [""]  # Liste pour les mots extraits

    # Comptage des lettres et construction des mots
    for i in text:

        i = i.lower() # Normalisation en minuscules
        if i == " ":
            Liste.append("")
        elif i in "abcdefghijklmnopqrstuvwxyz":
            Liste[-1] += i


        if i not in dico:
            dico[i] = 1
        else:
            dico[i] += 1
    
    dico_2 = {} # Fréquence des mots
    for i in Liste:
        if i not in dico_2:
            dico_2[i] = 1
        else:
            dico_2[i] += 1

    # Recherche des éléments les plus fréquents

    # Lettre la plus fréquente
    maxi = [0, 0]
    for (i, j) in dico.items():
        if j > maxi[1]:
            maxi = [i, j]   

    # Mot le plus fréquent
    maxi_2 = [0, 0]
    for (i, j) in dico_2.items():
        if j > maxi_2[1]:
            maxi_2 = [i, j]

    print(Liste)
    print(f"Lettre préférée : {maxi[0]}, nombre d'utilisation : {maxi[1]}")
    print(f"Mot préféré : {maxi_2[0]}, nombre d'utilisation : {maxi_2[1]}")
    print(f"Nombre total de caractères : {len(text)}")
    print(f"Nombre total de mots : {len(Liste)}")

# Calcul du PGCD (Plus Grand Commun Diviseur)
def pgcd(value_a, value_b) -> int:
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de deux nombres entiers en utilisant l'algorithme d'Euclide.

    Arguments :
    - value_a : Premier entier.
    - value_b : Deuxième entier.

    Retourne le PGCD des deux nombres.
    """
    
    while value_a != 0 and value_b != 0:
        if value_a > value_b:
            value_a = value_a % value_b
        else:
            value_b = value_b % value_a
    
    if value_a > 0:
        return value_a
    return value_b

# Calcul du PPCM (Plus Petit Commun Multiple)
def ppcm(value_a, value_b) -> int:
    """
    Calcule le Plus Petit Commun Multiple (PPCM) de deux nombres entiers.

    Arguments :
    - value_a : Premier entier.
    - value_b : Deuxième entier.

    Retourne le PPCM des deux nombres.
    """
    if value_a > 0 and value_b > 0:
        return (value_a * value_b) / pgcd(value_a, value_b)

# Test de primalité avec l'algorithme de Miller-Rabin
def est_premier(number, random_value=5):
    """
    Vérifie si un nombre est premier en utilisant le test probabiliste de Miller-Rabin.

    Arguments :
    - number : Nombre entier à tester.
    - random_value : Nombre de tests aléatoires effectués pour améliorer la fiabilité (par défaut : 5).

    Retourne True si le nombre est premier, False sinon.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0:
        return False

    # Décomposition de n-1 en 2^r * s avec s impair
    num_s, num_r = number - 1, 0
    while num_s % 2 == 0:
        num_s //= 2
        num_r += 1

    for _ in range(random_value):
        num_a = random.randint(2, number - 1)
        num_x = pow(num_a, num_s, number)
        if num_x == 1 or num_x == number - 1:
            continue
        for _ in range(num_r - 1):
            num_x = pow(num_x, 2, number)
            if num_x == number - 1:
                break
        else:
            return False
    return True

# Générateur de mots de passe aléatoires
def generateur_pwd(length, letters: bool = True, numbers: bool = True, \
                    symbols: bool = True) -> str:
    """
    Génère un mot de passe aléatoire avec des options pour inclure des lettres, chiffres et symboles.

    Arguments :
    - length : Longueur souhaitée du mot de passe.
    - letters : Inclure des lettres (True par défaut).
    - numbers : Inclure des chiffres (True par défaut).
    - symbols : Inclure des symboles spéciaux (True par défaut).

    Retourne le mot de passe généré sous forme de chaîne.
    """
    
    using = ""
    if letters:
        using += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if numbers:
        using += "0123456789"
    if symbols:
        using += "?!()[]@"
    
    pwd = ""
    for i in range(length):
        if i % 4 == 0:
            pwd += "-"
        pwd += random.choice(using)
    
    return pwd[1:] # Suppression du premier tiret superflu

# Fonction pour calculer un terme de la suite de Fibonacci
def fibonacci(level):
    """
    Calcule le n-ième terme de la suite de Fibonacci de manière récursive.

    Arguments :
    - level : Indice du terme à calculer.

    Retourne le n-ième terme de la suite de Fibonacci.
    """

    if level == 0:
        return 0
    elif level == 1:
        return 1
    else:
        return fibonacci(level - 1) + fibonacci(level - 2)