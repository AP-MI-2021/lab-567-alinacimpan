from Domain.cheltuiala import get_suma, get_tipul, get_data
from Logic.crud import adauga_cheltuiala, get_by_id
from Logic.Adunarea_unei_valori import adauga_valoare_data

def test_adauga_valoare_data():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "12.03.2021", "canal", lista)

    lista = adauga_valoare_data("12.03.2021", 45.50, lista)
    assert len(lista) == 3
    cheltuiala_modificata_1 = get_by_id(1, lista)
    assert get_suma(cheltuiala_modificata_1) == 195.50
    assert get_data(cheltuiala_modificata_1) == "12.03.2021"
    assert get_tipul(cheltuiala_modificata_1) == "alte cheltuieli"
    cheltuiala_modificata_2 = get_by_id(3, lista)
    assert get_suma(cheltuiala_modificata_2) == 134.95
    assert get_data(cheltuiala_modificata_2) == "12.03.2021"
    cheltuiala_nemodificata = get_by_id(2, lista)
    assert get_suma(cheltuiala_nemodificata) == 200
    assert get_data(cheltuiala_nemodificata) == "23.10.2021"
