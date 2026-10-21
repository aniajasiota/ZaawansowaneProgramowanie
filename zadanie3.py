def wyswietl_parzyste(liczby):
    for i in range(len(liczby)):
        if liczby[i] % 2 == 0:
            print(liczby[i])


liczby = list(range(1, 11))
wyswietl_parzyste(liczby)
