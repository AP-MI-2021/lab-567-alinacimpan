from Logic.cea_mai_mare_cheltuiala import biggest_sum_by_type

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

def test_biggest_sum_by_type():
    cheltuieli = get_datas()
    result = biggest_sum_by_type(cheltuieli)
    assert len(result) == 3
    assert result['canal'] == 123
    assert result['intretinere'] == 200
    assert result['alte cheltuieli'] == 390