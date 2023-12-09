# Creați o aplicatie în Python pentru gestionarea rezervărilor într-un hotel.
# Sistemul va permite utilizatorului să introducă datele de la tastatură și va oferi funcționalități
# pentru adăugarea, căutarea și anularea rezervărilor.
# Fiecare rezervare va conține informații despre client (nume, prenume), numărul camerei și perioada de ședere (data de început și data de sfârșit).
# Aplcatia trebuie sa ofere posibilitatea de afisare a tutror rezervarilor si cautare a unei rezervari dupa nume.

import datetime

class Rezervare:
    def __init__(self, nume, prenume, numar_camera, data_inceput, data_sfarsit):
        self.nume = nume
        self.prenume = prenume
        self.numar_camera = numar_camera
        self.data_inceput = data_inceput
        self.data_sfarsit = data_sfarsit

def adauga_rezervare():
    nume = input("Introdu numele clientului: ")
    prenume = input("Introdu prenumele clientului: ")
    numar_camera = input("Introdu numarul camerei: ")

    data_inceput_str = input("Introdu data de inceput a rezervarii (AAAA-LL-ZZ): ")
    data_sfarsit_str = input("Introdu data de sfarsit a rezervarii (AAAA-LL-ZZ): ")

    data_inceput = datetime.datetime.strptime(data_inceput_str, "%Y-%m-%d").date()
    data_sfarsit = datetime.datetime.strptime(data_sfarsit_str, "%Y-%m-%d").date()

    rezervare_noua = Rezervare(nume, prenume, numar_camera, data_inceput, data_sfarsit)
    rezervari.append(rezervare_noua)
    print("Rezervare adaugata cu success")

def afiseaza_rezervari():
    if not rezervari:
        print("Nu exista rezervari.")
    else:
        for index, rezervare in enumerate(rezervari, start=1):
            print(f"{index}. {rezervare.nume} {rezervare.prenume} - Camera: {rezervare.numar_camera}, Perioada: {rezervare.data_inceput} - {rezervare.data_sfarsit}")

def cauta_rezervare_dupa_nume():
    nume_cautare = input("Introdu numele cientului pentru cautare: ")
    rezervari_gasite = [rezervare for rezervare in rezervari if rezervare.nume.lower() == nume_cautare.lower()]

    if rezervari_gasite:
        for rezervare in rezervari_gasite:
            print(f"{rezervare.nume} {rezervare.prenume} - Camera {rezervare.numar_camera}, Perioada: {rezervare.data_inceput} - {rezervare.data_sfarsit}")
    else:
        print(f"Nu exista rezervare pentru {nume_cautare}")

def anuleaza_rezervare():
    afiseaza_rezervari()
    if rezervari:
        index_anulare = int(input("Introdu numarul rezervarii pe care doresti sa o anulezi: "))
        if 0 <= index_anulare < len(rezervari):
            rezervari.pop(index_anulare)
            print("Rezervarea a fost anualata cu success!")
        else:
            print("Numarul rezervarii alese nu este valid!")
    else:
        print("Nu exista nici o rezervare")

rezervari = []

while True:
    print("\n===== HOTEL Hilton - Meniu =====")
    print("1. Adauga rezervare")
    print("2. Afiseaza rezervarile")
    print("3. Cauta rezervare dupa nume")
    print("4. Anuleaza rezervare")
    print("0. Inchidere Program")

    optiune = int(input("Selecteaza optiunea dorita: "))

    match optiune:
        case 1:
            adauga_rezervare()
        case 2:
            afiseaza_rezervari()
        case 3:
            cauta_rezervare_dupa_nume()
        case 4:
            anuleaza_rezervare()1
        case 0:
            print("Programul se va inchide")
            break
        case _:
            print("Optiunea nu este valida.\nInceercati din nou!")

