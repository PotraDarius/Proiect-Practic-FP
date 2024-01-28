import datetime

from Exceptii import *


class UIConsole:

    def __init__(self, service):
        self.__service = service
        self.__comenzi = {"adaugare": self.__ui_adaugare, "examene": self.__ui_examene_programare, "export": self.__ui_export}

    def __ui_examene_maine(self):
        """
        functie ce afiseaza toate examenele de maine
        :return:
        """
        data = datetime.date.today()
        examene_maine = self.__service.examene_maine(data)
        for examen in examene_maine:
            print(str(examen))

    def __ui_adaugare(self, parametrii):
        """
        functie din ui pentru adauarea si creearea unui examen
        parametrii = [materie, data, ora, tip_examen]
        :param parametrii:
        :return:
        """
        if len(parametrii) < 4:
            raise UIError("Parametrii insuficienti!")

        self.__service.adauga_examen(parametrii[0],parametrii[1],parametrii[2],parametrii[3])

    def __ui_examene_programare(self, parametrii):
        """
        functie pentru afisarea examenelor in urmatoarele 3 zile de la data
        parametrii[luna, zi]
        :param parametrii:
        :return:
        """
        if len(parametrii) < 2:
            raise UIError("Parametrii insuficienti!")
        try:
            luna = int(parametrii[0])
            zi = int(parametrii[1])
            data = datetime.date(2024, luna, zi)
            examene = self.__service.examene_programate(data)
            if examene == "":
                print("Nu s-a gasit niciun examen!")
            else:
                for examen in examene:
                    print(str(examen))
        except ValueError:
            raise UIError("Parametrii invalizi")

    def __ui_export(self, parametrii):
        """
        functie pentru a da export
        parametrii = [nume_fisier, string]
        :param parametrii:
        :return:
        """
        if len(parametrii) < 2:
            raise UIError("Parametrii insuficienti!")

        if parametrii[0] == "" or parametrii[1] == "":
            raise UIError("Parametrii invalizi!")

        self.__service.export(parametrii[0], parametrii[1])

    def run(self):
        """
        functie pentru rularea consolei
        indicatii: comenzile se dau in felul urmator : comanda/parametru1,parametru2,...
        comenzi: adaugare/p1,p2,p3,p4
                 examene/p1,p2
                 export/p1,p2
        :return:
        """
        self.__ui_examene_maine()
        while True:
            comanda = input("Comanda: ")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return

            parti = comanda.split("/")
            nume_comanda = parti[0]
            try:
                if nume_comanda in self.__comenzi:
                    try:
                        parametrii = parti[1]
                        parametrii = parametrii.split(",")
                    except IndexError:
                        raise UIError("Nu s-a dat niciun parametru!")
                    self.__comenzi[nume_comanda](parametrii)
                else:
                    raise UIError("Comanda invalida")

            except UIError as ui:
                print(f"Eroare la ui: {ui}")
            except RepoError as rep:
                print(f"Eroare la repository: {rep}")
            except ValidError as val:
                print(f"Eroare la validare: {val}")
            except ServiceError as sv:
                print(f"Eroare la service: {sv}")


