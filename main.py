from Tests.toate_testele import test_all
from Userinterface.console import run_menu
from Userinterface.command_line_console import run_new_menu


def main():
    test_all()
    lista = []
    while True:
        print("1. Consola normala.")
        print("2. Console line command.")
        print("x. Iesire.")
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            run_menu(lista)
        elif optiune == "2":
            run_new_menu(lista)
        elif optiune.lower() == "x":
            break
        else:
            print("Optiune gresita ! Reincercati ")


if __name__ == "__main__":
    main()