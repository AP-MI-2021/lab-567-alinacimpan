from Domain.cheltuieli import creeaza_cheltuiala, get_nr_apartment
from Logic.sterge_cheltuieli import delete_all_expenses

def get_datas():
    return [
        creeaza_cheltuiala(1, 32, 263, datetime.date(2021, 6, 20), 'canal'),
        creeaza_cheltuiala(2, 15, 126, datetime.date(2021, 9, 27), 'intretinere'),
        creeaza_cheltuiala(3, 24, 100, datetime.date(2020, 4, 18), 'alte cheltuieli'),
        creeaza_cheltuiala(4, 56, 54,  datetime.date(2019, 4, 30), 'intretinere')
    ]

def test_delete_all_expenses():
    list = get_data()
    contor = 0
    new_list = delete_all_expenses(list, 2)
    assert len(new_list) == len(list) - 3
    for creeaza_cheltuiala in new_list:
        if get_nr_apartment(expense) == 2:
            contor = contor + 1
    assert contor == 0