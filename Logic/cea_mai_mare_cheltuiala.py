from Domain.cheltuiala import get_suma, get_tipul, get_nr_apartament

def cea_mai_mare_cheltuiala_dupa_tip(lista):
    """
    Determina cea mai mare cheltuiala pentru fiecare tip de cheltuială
    :param lista: lista de chetuieli
    :return: cea mai mare chetuiala pentru fiecare tip de cheltuiala
    """
    rezultat = {}
    for cheltuiala in lista:
        tipul = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tipul in rezultat:
            if suma > get_suma(rezultat[tipul]):
                rezultat[tipul] = cheltuiala
        else:
            rezultat[tipul] = cheltuiala
    return rezultat
