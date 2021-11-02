from Domain.cheltuiala import creeaza_cheltuiala, get_suma
from Logic.Adunarea_unei_valori import add_value_if_date


def get_data():
    """
    Functie suport pentru functiile de test
    """
    return \
        [
            creeaza_cheltuiala(23, 5, 123, datetime.date(2021, 6, 20), 'canal'),
            creeaza_cheltuiala(56, 6, 200, datetime.date(2021, 6, 20), 'intretinere'),
            creeaza_cheltuiala(19, 3, 390, datetime.date(2020, 12, 12), 'alte cheltuieli'),
            creeaza_cheltuiala(34, 7, 100, datetime.date(2018,  5, 20), 'canal')

        ]



def test_add_value_if_date():
    list = get_data()
    list2 = get_data()
    list2 = add_value_if_date(list2, '2020 12 12', 400)
    assert len(list2) == len(list)
    assert get_suma(list[2]) + 400 == get_suma(list2[2])