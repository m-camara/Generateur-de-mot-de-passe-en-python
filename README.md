Générateur de Mot de Passe en Python 🔐

Ce projet est un générateur de mot de passe aléatoire en Python. Il crée un mot de passe sécurisé contenant au moins :

1 lettre minuscule

1 lettre majuscule

1 chiffre

1 symbole spécial

Le reste des caractères est choisi aléatoirement parmi toutes les lettres, chiffres et symboles pour atteindre la longueur demandée par l’utilisateur.

Fonctionnalités

Vérifie que la longueur du mot de passe est d’au moins 4 caractères.

Garantit la présence de lettres, chiffres et symboles pour un mot de passe sécurisé.

Mélange tous les caractères pour rendre le mot de passe aléatoire.

Facile à utiliser depuis le terminal.

Code principal : 

import random
import string


def generer_mot_de_passe(longueur):
    if longueur < 4:
        print("La longueur doit être d'au moins 4.")
        return ""
    
    
    minuscule = random.choice(string.ascii_lowercase)
    majuscule = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation)
    
    tous_les_characteres = string.ascii_letters + string.digits + string.punctuation
    reste = [random.choice(tous_les_characteres)for _ in range(longueur-4) ]
    
    mot_de_passe_liste = [minuscule,majuscule,chiffre,symbole] + reste
    random.shuffle(mot_de_passe_liste)
    
    return"".join(mot_de_passe_liste)

if __name__ == '__main__':
    longueur = int(input("Longueur du mot de passe : "))
    mot_de_passe = generer_mot_de_passe(longueur)
    
    print("Mot de passe généré : ",mot_de_passe)

 auteur : m-camara
