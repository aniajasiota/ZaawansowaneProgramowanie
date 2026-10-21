def wyswietl_co_drugi(liczby):
    for i in range(0, len(liczby), 2):
        print(liczby[i])


liczby = list(range(1, 11))
wyswietl_co_drugi(liczby)
