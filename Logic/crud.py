from Domain.cheltuiala import creeaza_cheltuiala, get_nr_apartament

def create(lst_cheltuieli,
           nr_apartament, suma, data, tipul):
    """
    Adauga o cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli.
    :param nr_apartament: numar partament.
    :param suma: suma.
    :param data: data
    :param tipul: tipul
    :return: o noua lista formata din lst_cheltuieli si noua cheltuiala adaugata.
    """
    cheltuiala = creeaza_cheltuiala(nr_apartament, suma, data, tipul)
    return lst_cheltuieli + [cheltuiala]


def read(lst_cheltuieli, nr_apartament: int = None):
    """
    Citeste o cheltuiala din "baza de date".
    :param lst_cheltuieli: lista de cheltuieli.
    :param nr_apartament: nr apartament.
    :return: cheltuiala cu nr-ul nr_apartament sau lista cu toate cheltuielile, daca nr_apartament=None.
    """
    cheltuiala_cu_nr = None
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_nr = cheltuiala
    if cheltuiala_cu_nr:
        return cheltuiala_cu_nr
    return lst_cheltuieli


def update(lst_cheltuieli, nr_apartament, suma, data, tipul):
    """
    Actualizeaza o cheltuiala.
    :param lst_cheltuieli: lista de cheltuieli.
    :param nr_apartament: numar partament.
    :param suma: suma.
    :param data: data
    :param tipul: tipul
    :return: o lista de cheltuieli actualizata.
    """
    new_cheltuieli = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) == nr_apartament:
            cheltuiala_noua = creeaza_cheltuiala(nr_apartament, suma, data, tipul)
            new_cheltuieli.append(cheltuiala_noua)
        else:
            new_cheltuiala.append(cheltuiala)
    return new_cheltuiala


def delete(lst_cheltuieli, nr_apartament):
    """
    Sterge o cheltuiala din "baza de date".
    :param lst_cheltuieli: o lista de cheltuieli.
    :param nr_apartament: nr apartament.
    :return: o lista fara cheltuiala cu nr-ul nr_apartament.
    """
    new_list = []
    for cheltuiala in lst_cheltuieli:
        if get_nr_apartament(cheltuiala) != nr_apartament:
            new_list.append(cheltuiala)
    return new_list