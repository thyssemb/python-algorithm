import json

def recherche_city():
    with open("for2_json.json", "r") as fichier:
        data = json.load(fichier)

        if "city" in data:
            city = data["city"]
            print("voici les villes trouvées :", city)
        else:
            print("aucune ville trouvée")

recherche_city()
