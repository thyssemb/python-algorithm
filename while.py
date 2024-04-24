def boucle():
    nombreTrains = 0
    # on initialise à 0 car on commence
    # à compter à partir de 0

    while nombreTrains < 100:
        print("j'ai vu", nombreTrains, "trains")
        nombreTrains += 1
        # on incrémente pour compter jusqu'à 100
        # donc jusqu'à ce que la condition soit valide
    return nombreTrains
    # on return à la fin de la boucle pour arrêter
    # la fonction et récupérer le résultat

def boucleBis():
    nombreTrains = boucle()
    # on récupère la variable nombreTrains de la fonction boucle
    # qui va nous servir à rajouter et afficher un nouveau message
    print("j'ai vu", nombreTrains, "il me manque encore", 100 - nombreTrains, "à voir")

boucleBis()
