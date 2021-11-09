from Logic.crud import adauga_cheltuiala
from Logic.ordonare_descrescator import  ordonare_descrescator_cheltuieli_dupa_suma,  get_luna_and_anul_from_data


def test_ordonare_descrescator_cheltuieli_dupa_suma():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 90, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)

    lista = ordonare_descrescator_cheltuieli_dupa_suma(lista)
    assert lista[0] == [("id", 2), ("numar_apartament", 90), ("suma", 200),
                        ("data", "23.10.2021"), ("tipul", "intretinere")]
    assert lista[1] == [("id", 1), ("numar_apartament", 13), ("suma", 150),
                        ("data", "12.03.2021"), ("tipul", "alte cheltuieli")]
    assert lista[2] == [("id", 3), ("numar_apartament", 45), ("suma", 89.45),
                        ("data", "04.10.2021"), ("tipul", "canal")]


def test_get_luna_and_anul_from_data():
    assert get_luna_and_anul_from_data("12.03.2021") == "03.2021"
    assert get_luna_and_anul_from_data("04.10.2021") == "10.2021"
