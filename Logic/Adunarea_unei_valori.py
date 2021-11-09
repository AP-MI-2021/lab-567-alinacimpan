from Domain.cheltuiala import get_data, get_suma, get_tipul, get_nr_apartament, get_id_cheltuiala, creeaza_cheltuiala



def adauga_valoare_data(data_string, valoare, lista, undo_list=None, redo_list=None):
    """
    Adunarea unei valori la toate cheltuielile dintr-o dată citită.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modificare
    :param valoare: valoarea care se adauga sumei
    :param data_string: data pentru care se va adauga o valoare
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile cu data introdusa au valoarea adaugata sumei
    """
    if valoare < 0:
        raise ValueError("Nu se poate adauga o valoare negativa !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    rezultat = []
    for cheltuiala in lista:
        if get_data(cheltuiala) == data_string:
            cheltuiala_noua = creeaza_cheltuiala(get_id_cheltuiala(cheltuiala), get_nr_apartament(cheltuiala),
                                                 float(get_suma(cheltuiala)) + valoare, get_data(cheltuiala),
                                                 get_tipul(cheltuiala))
            rezultat.append(cheltuiala_noua)
        else:
            rezultat.append(cheltuiala)
    return rezultat