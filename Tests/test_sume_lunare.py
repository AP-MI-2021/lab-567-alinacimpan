from Logic.sume_lunare import sume_lunare_apartament
from Logic.crud import adauga_cheltuiala
def test_sume_lunare_apartament():
    lista = []
    lista = adauga_cheltuiala(1, 13, 150, "12.03.2021", "alte cheltuieli", lista)
    lista = adauga_cheltuiala(2, 45, 200, "23.10.2021", "intretinere", lista)
    lista = adauga_cheltuiala(3, 45, 89.45, "04.10.2021", "canal", lista)
    lista = adauga_cheltuiala(4, 45, 50, "04.03.2021", "canal", lista)

    rezultat = sume_lunare_apartament(lista)
    assert len(rezultat) == 2
    assert rezultat[13] == {"03.2021": 150}
    assert rezultat[45] == {"10.2021": 289.45, "03.2021": 50}