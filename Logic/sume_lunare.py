from Domain.cheltuiala import get_nr_apartament, get_data, get_suma

def get_luna_and_anul_from_data(data):
    """
    Determina luna (format MM.YYYY) din data ( format DD.MM.YYYY)
    :param data: data in format DD.MM.YYYY
    :return: luna si anul din data in format MM.YYYY
    """
    return data[3:]


def sume_lunare_apartament(lista):
    """
    Determina sumele lunare pentru fiecare apartament
    :param lista: lista de cheltuieli
    :return: un nested dictionary cu sumele lunare pentru fiecare apartament
    """
    apartament = {}
    for cheltuiala in lista:
        numar_apartament = get_nr_apartament(cheltuiala)
        luna = get_luna_and_anul_from_data(get_data(cheltuiala))
        suma = get_suma(cheltuiala)
        if numar_apartament in apartament:
            if luna in apartament[numar_apartament]:
                apartament[numar_apartament][luna] += suma
            else:
                apartament[numar_apartament][luna] = suma
        else:
            apartament[numar_apartament] = {}
            apartament[numar_apartament][luna] = suma
    return apartament