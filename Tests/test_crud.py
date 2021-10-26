from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.crud import create, read, update, delete

def get_datas():
    return [
        creeaza_cheltuiala(3, 360, 2020 - 12 - 1, 'canal'),
        creeaza_cheltuiala(12, 200, 2021 - 6 - 20, 'intretinere'),
        creeaza_cheltuiala(18, 180, 2019 - 2 - 28, 'alte cheltuieli'),
        creeaza_cheltuiala(4, 260, 2020 - 9 - 27, 'intretinere')
    ]

def test_create():
    cheltuieli = get_datas()
    params = (10, 120, 2021 - 4 - 30, 'alte cheltuieli')
    c_new = creeaza_cheltuiala(*params)
    new_cheltuieli = create(cheltuieli, *params)
    assert c_new in new_cheltuieli
    assert len(new_cheltuieli) == len(cheltuieli) + 1
    assert c_new in  new_cheltuieli

def test_read():
    cheltuieli = get_datas()
    some_c = cheltuieli[2]
    assert read(cheltuieli, get_nr_apartament(some_c)) == some_c
    assert read(cheltuieli, None) == cheltuieli

def test_update():
    cheltuieli = get_datas()
    c_updated = creeaza_cheltuiala(4, 652.8, 2021 - 4 - 18, 'intretinere')
    updated = update(cheltuieli, 4, 652.8, 2021 - 4 - 18, 'intretinere')
    assert c_updated in updated
    assert c_updated not in cheltuieli
    assert len(cheltuieli) == len(updated)


def test_delete():
    cheltuieli = get_datas()
    to_delete = 3
    c_deleted = read(cheltuieli, to_delete)
    deleted = delete(cheltuieli, to_delete)
    assert c_deleted not in deleted
    assert c_deleted in cheltuieli
    assert len(deleted) == len(cheltuieli) - 1

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()
