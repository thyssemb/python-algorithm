def liste():
    liste = [1, 20, 67, 89, 3]
    print("voici les numéros :", liste)
    return liste

def bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

    print("voici la liste triée :", liste)

bulle(liste())
