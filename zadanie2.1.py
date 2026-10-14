def pomnoz_przez_2(liczby):
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

liczby = [2, 4, 6, 8, 10]
print(pomnoz_przez_2(liczby))