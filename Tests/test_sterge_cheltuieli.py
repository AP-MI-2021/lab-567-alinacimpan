from Logic.crud import adauga_cheltuiala, get_by_numar_apartament
from Logic.sterge_cheltuieli import sterge_toate_cheltuielile_apartament

def test_sterge_toate_cheltuielile_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "06.10.2021", "canal", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "12.03.2021", "canal", lista)

    lista = sterge_toate_cheltuielile_apartament(45, lista)
    assert len(lista) == 1
    assert get_by_numar_apartament(45, lista) == []
    assert get_by_numar_apartament(13, lista) == [[("id", 1), ("numar_apartament", 13), ("suma", 150),
                                                   ("data", "06.10.2021"), ("tipul", "canal")]]