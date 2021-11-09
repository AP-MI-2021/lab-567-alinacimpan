from Domain.cheltuiala import get_nr_apartament

def sterge_toate_cheltuielile_apartament(nr_aparatament, lista, undo_list=None, redo_list=None):
    """
    Ștergerea tuturor cheltuielilor pentru un apartament dat.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modificare
    :param numar_aparatament: numarul de apartament pentru care dorim sa stergem toate cheltuielile
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli fara cele pentru numarul de apartament specificat
    """
    if nr_aparatament < 0:
        raise ValueError("Numarul apartamentului nu poate fi negativ !")
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    rezultat = []
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) != nr_aparatament:
            rezultat.append(cheltuiala)
    return rezultat
