import datetime

from Logic.crud import create
from Tests.test_sterge_cheltuieli import test_delete_all_expenses
from Tests.test_adunarea_unei_valori import test_add_value_if_date
from Tests.test_cea_mai_mare_cheltuiala import test_biggest_sum_by_type
from Userinterface.console import run_ui

def main():
    cheltuieli = []
    cheltuieli = create(cheltuieli,311, 1, 239.42, datetime.date(2019, 11, 28), 'canal')
    cheltuieli = create(cheltuieli,312, 2, 193.2, datetime.date(2015, 1, 21), 'alte cheltuieli')
    cheltuieli = create(cheltuieli,313, 3, 300, datetime.date(2010, 10, 8), 'intretinere')
    run_ui(cheltuieli)

if __name__ == '__main__':
    test_delete_all_expenses
    test_add_value_if_date
    test_biggest_sum_by_type
    main()