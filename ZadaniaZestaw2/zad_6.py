def polacz_listy(lista1, lista2):
    lista = list(set(lista1 + lista2))
    wynik = []

    for liczba in lista:
        wynik.append(liczba ** 3)

    return wynik


wynik = polacz_listy([1, 2, 3], [3, 4, 5])
print(wynik)
