import json

def recherche_hobbies():
    with open("for2_json.json", "r") as fichier:
        data = json.load(fichier)

        if "hobbies" in data:
            hobbies = data["hobbies"]
            print("voici les hobbies trouvés :", hobbies)
        else:
            print("aucun hobby trouvé")

recherche_hobbies()
