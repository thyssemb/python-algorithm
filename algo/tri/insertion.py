import json

def tri_city():
    with open("insertion.json", "r") as fichier:
        data = json.load(fichier)
        liste = [(ville["habitants"], ville["ville"]) for ville in data]

        n = len(liste)
        for i in range(1, n):
            cle = liste[i]
            j = i - 1
            while j >= 0 and liste[j] > cle:
                liste[j + 1] = liste[j]
                j = j - 1
            liste[j + 1] = cle

    print("voici la liste triée par nb d'habitants :", liste)

tri_city()
