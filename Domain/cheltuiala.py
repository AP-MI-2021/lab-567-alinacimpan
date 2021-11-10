

def creeaza_cheltuiala(id_cheltuiala,nr_apartament: int, suma, data, tipul):
    """
    Creeaza un dictionar ce reprezinta o cheltuiala.
    :param id_cheltuiala: Id-ul apartamentului, trebuie sa fie unic.
    :param nr_apartament: Numarul apartamentului, trebuie sa fie unic.
    :param suma: Suma de cheltuit.
    :param data: Data cheltuielii.
    :param tipul: Tipul cheltuielii: intretinere, canal sau alte cheltuieli.
    :return: O cheltuiala.
    """

    return [id_cheltuiala, nr_apartament, suma, data, tipul]


def get_id_cheltuiala(cheltuiala):
    """
    Getter pentru id-ul cheltuielii.
    :param cheltuiala: cheltuiala.
    :return: Id-ul cheltuielii.
    """
    return cheltuiala[0]




def get_nr_apartament(cheltuiala):
    """
    Getter pentru numarul apartamentului.
    :param cheltuiala: cheltuiala.
    :return: Nr de apartament al cheltuielii.
    """
    return cheltuiala[1]



def get_suma(cheltuiala):
    """
    Getter pentru suma.
    :param cheltuiala: cheltuiala
    :return: suma cheltuita
    """
    return cheltuiala[2]

def get_data(cheltuiala):
    """
    Getter pentru data.
    :param cheltuiala: cheltuiala
    :return: Data cheltuielii
    """
    return cheltuiala[3]


def get_tipul(cheltuiala):
    """
    Getter pentru tip.
    :param cheltuiala: cheltuiala
    :return: Tipul cheltuielii: intretinere, canal sau alte cheltuieli
    """
    return cheltuiala[4]


def to_string(cheltuiala):
    """
    Returneaza cheltuiala ca string
    :param cheltuiala: cheltuiala careia vrem sa-i aflam datele
    :return: cheltuiala ca string
    """
    return f"Id: {get_id_cheltuiala(cheltuiala)}; Numar apartament: {get_nr_apartament(cheltuiala)}; " \
           f"Suma: {get_suma(cheltuiala)}; Data: {get_data(cheltuiala)}; Tipul: {get_tipul(cheltuiala)}"