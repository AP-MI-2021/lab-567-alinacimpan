from Domain.cheltuiala import get_suma

def ordonare_descrescator_cheltuieli_dupa_suma(lista, undo_list=None, redo_list=None):
    """
    Ordoneaza cheltuielile descrescător după sumă.
    :param redo_list: lista pentru redo care e resetata
    :param undo_list: lista pentru undo care salveaza lista inainte de modicare
    :param lista: lista de cheltuieli
    :return: lista de cheltuieli ordonata descrescator dupa suma
    """
    if undo_list is not None and redo_list is not None:
        undo_list.append(lista)
        redo_list.clear()
    return sorted(lista, key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)


def get_luna_and_anul_from_data(data):
    """
    Determina luna (format MM.YYYY) din data ( format DD.MM.YYYY)
    :param data: data in format DD.MM.YYYY
    :return: luna si anul din data in format MM.YYYY
    """
    return data[3:]
