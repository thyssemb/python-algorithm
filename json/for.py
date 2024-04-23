import json

def recherche_prenoms():
    with open("for_json.json", "r") as fichier:
        data = json.load(fichier)

        for objet in data:  # parcours de chaque objet dans le fichier JSON
            if "prenoms" in objet:  # vérification si l'objet contient la clé "prenoms"
                prenom = objet["prenoms"]  # récupération du prénom
                print("prenom trouvé :", prenom)

        if not any("prenoms" in objet for objet in data):  # si aucun prénom n'a été trouvé
            print("aucun prénom trouvé dans le document")

# appel de la fonction pour rechercher les prénoms
recherche_prenoms()
