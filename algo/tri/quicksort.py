import json

def file():
    with open("insertion.json", "r") as fichier:
        data = json.load(fichier)
    print("voici la liste non triée", data)
    return data

def partition(array, low, high):
    pivot = array[high]["habitants"]
    i = low - 1
    for j in range(low, high):
        if array[j]["habitants"] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

data = file()


quicksort(data, 0, len(data) - 1)

print("voici la liste triée :", data)
