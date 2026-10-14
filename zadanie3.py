def wyswietl_parzyste(liczby):
    for liczba in liczby:
        if liczba % 2 == 0:
            print(liczba)

liczby = list(range(1, 11))
wyswietl_parzyste(liczby)