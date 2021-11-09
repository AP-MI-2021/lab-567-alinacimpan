from Domain.cheltuiala import get_id
from Logic.crud import adauga_cheltuiala
from Logic.cea_mai_mare_cheltuiala import cea_mai_mare_cheltuiala_dupa_tip

def test_cea_mai_mare_cheltuiala_dupa_tip():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 90, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 87, 78.90, "07.12.2021", "canal", lista)
    lista = adauga_cheltuiala(5, 56, 567.78, "14.01.2020", "intretinere", lista)
    lista = adauga_cheltuiala(6, 17, 70, "31.12.2020", "alte cheltuieli", lista)

    rezultat = cea_mai_mare_cheltuiala_dupa_tip(lista)

    assert len(rezultat) == 3
    assert get_id(rezultat["canal"]) == 3
    assert get_id(rezultat["intretinere"]) == 5
    assert get_id(rezultat["alte cheltuieli"]) == 1