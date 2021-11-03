import datetime
from Domain.cheltuiala import creeaza_cheltuiala, get_str, get_nr_apartament, get_suma, get_data, get_tipul
from Logic.crud import create, update, delete, read
from Logic.Adunarea_unei_valori import add_value_if_date
from Logic.cea_mai_mare_cheltuiala import biggest_sum_by_type
from Logic.Sterge_cheltuieli import delete_all_expenses
from Userinterface.command_line_console import run_cli

def show_menu():
    print('1. CRUD ')
    print('2. Ștergerea tuturor cheltuielilor pentru un apartament dat. ')
    print('3. Adunarea unei valori la toate cheltuielile dintr-o dată citită. ')
    print('4. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială. ')
    print('x. EXIT ')


def read_date():
    date_str = input('Dati data cu elementele separate printr-o liniuta: ')
    date = date_str.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    return datetime.date(year, month, day)


def handle_add(cheltuieli):
    id_cheltuiala = int(input('Dati id-ul cheltuielii: '))
    nr_apartament = int(input('Dati numarul apartamentului: '))
    suma = float(input('Dati suma ce trebuie cheltuita: '))
    date = read_date()
    tip = input('Dati tipul: ')
    return create(cheltuieli, nr_apartament, suma, date, tip)


def handle_modify(cheltuieli):
    id_cheltuiala = int(input('Dati id-ul cheltuielii ce trebuie modificata: '))
    nr_apartament = int(input('Dati numarul apartamentului ce ii trebuie modificata cheltuiala: '))
    suma = float(input('Dati noua suma: '))
    data = read_date()
    tip = input('Dati noul tip: ')
    return update(cheltuieli, nr_apartament, suma, data, tip)


def handle_delete(cheltuieli):
    id_cheltuiala = int(input('Dati id-ul cheltuielii ce se a sterge: '))
    nr_apartament = int(input('Dati numarul apartamentului ce se a sterge: '))
    cheltuieli = delete(cheltuieli, nr_apartament)
    print('Stergerea a fost efectuata cu succes!')
    return cheltuieli


def handle_show_all(cheltuieli):
    for chelt in cheltuieli:
        print(get_str(chelt))


def handle_show_details(cheltuieli):
    d_cheltuiala = int(input('Dati id-ul cheltuielii pentru care doriti detalii: '))
    nr_apartament = int(input('Dati numarul apartamentului pentru care doriti detalii: '))
    chelt = read(cheltuieli, nr_apartament)
    print(f'Numarul apartamentului este: {get_nr_apartament(chelt)}')
    print(f'Suma ce trebuie cheltuita este: {get_suma(chelt)}')
    print(f'Data la care s-au generat costurile: {get_data(chelt)}')
    print(f'Tipul cheltuielii este: {get_tipul(chelt)}')


def handel_crud(cheltuieli):
    while True:
        print('1. Adaugare cheltuiala')
        print('2. Modificare cheltuiala')
        print('3. Stergere cheltuiala')
        print('a. Afisare')
        print('d. Detalii cheltuiala')
        print('r. Revenire')

        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            cheltuieli = handle_add(cheltuieli)
        elif optiune == '2':
            cheltuieli = handle_modify(cheltuieli)
        elif optiune == '3':
            cheltuieli = handle_delete(cheltuieli)
        elif optiune == 'a':
            handle_show_all(cheltuieli)
        elif optiune == 'd':
            handle_show_details(cheltuieli)
        elif optiune == 'r':
            break
        else:
            print('Optiune invalida, incercati din nou! ')
    return cheltuieli

def delete_all_expenses_for_apartement(cheltuieli):
    try:
        nr_ap = int(input('Dati numarul apartamentului caruia i se vor sterge cheltuielile: '))
        cheltuieli = delete_all_expenses(cheltuieli, nr_ap)
        print(f'Cheltuieleile apartamentului cu numarul {nr_ap} au fost sterse! ')
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def add_sum_to_date(cheltuieli):
    try:
        data = read_date()
        if data is None:
            raise ValueError("Data nu a fost introdusa corespunzator")
        valoare = float(input('Dati valoarea ce trebuie adunata: '))
        cheltuieli = add_value_if_date(cheltuieli, data, valoare)
        return cheltuieli
    except ValueError as ve:
        print('Eroare:  {ve}')
    return cheltuieli


def get_biggest_chelt(cheltuieli):
    result = biggest_sum_by_type(cheltuieli)
    for tipul in result:
        print(f'Tipul {tipul} are suma maxima {result[tipul]}. ')


def run_ui(cheltuieli):
    while True:
        show_menu()
        optiune = input('Alegeti o optiune: ')
        print()
        if optiune == '1':
            cheltuieli = handel_crud(cheltuieli)
        elif optiune == '2':
            nr_apartament = int(input('Dati numarul apartamentului caruia i se vor sterge cheltuielile: '))
            cheltuieli = delete_all_costs_for_apartement(cheltuieli, nr_ap)
            print(f'Apartamentul cu numarul {nr_apartament} a fost sters, neavand nicio cheltuiala! ')
        elif optiune == '3':
            cheltuieli = add_sum_to_date(cheltuieli)
        elif optiune == '4':
            cheltuieli = get_biggest_chelt(cheltuieli)
        elif optiune == '5':
            pass
        elif optiune == '6':
            pass
        elif optiune == 'x':
            break
        else:
            print('Optiune incorecta, incercati din nou! ')
    return cheltuieli