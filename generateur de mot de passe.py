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