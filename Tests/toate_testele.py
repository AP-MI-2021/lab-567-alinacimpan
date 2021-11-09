from Tests.test_crud import test_adauga_cheltuiala, test_sterge_cheltuiala, test_modifica_cheltuiala, test_get_by_id, \
    test_get_by_numar_apartament
from Tests.test_sterge_cheltuieli import test_sterge_toate_cheltuielile_apartament
from Tests.test_adunarea_unei_valori import test_adauga_valoare_data
from Tests.test_cea_mai_mare_cheltuiala import test_cea_mai_mare_cheltuiala_dupa_tip
from Tests.test_ordonare_descrescator import  test_ordonare_descrescator_cheltuieli_dupa_suma, test_get_luna_and_anul_from_data
from Tests.test_sume_lunare import test_sume_lunare_apartament
from Tests.test_undo_and_redo import test_undo_and_redo

def test_all():
    test_adauga_cheltuiala()
    test_sterge_cheltuiala()
    test_modifica_cheltuiala()
    test_get_by_id()
    test_get_by_numar_apartament()
    test_sterge_toate_cheltuielile_apartament()
    test_adauga_valoare_data()
    test_cea_mai_mare_cheltuiala_dupa_tip()
    test_ordonare_descrescator_cheltuieli_dupa_suma()
    test_get_luna_and_anul_from_data()
    test_sume_lunare_apartament()
    test_undo_and_redo()