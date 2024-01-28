from Domain import *
from Exceptii import *

class FileRepositoryExamen:

    def __read_from_file(self):
        """
        functie ce citeste dintr-un fisier toate examenele
        :return:
        """
        with open(self.__filename, "r") as file:
            self.__examene.clear()
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                parti = line.split("/")
                materie = parti[0]
                data = parti[1]
                ora = parti[2]
                tip_examen = parti[3]
                ex = Examen(materie, data, ora, tip_examen)
                self.__examene.append(ex)

    def __init__(self, filename):
        self.__examene = []
        self.__filename = filename
        self.__read_from_file()

    def __load_to_file(self):
        """
        functie ce citeste intr-un fisier examenele
        :return:
        """
        with open(self.__filename, "w") as file:
            for examen in self.__examene:
                file.write(str(examen) + '\n')

    def get_all(self):
        """
        functie ce returneaza toate examenele
        :return:
        """
        return self.__examene

    def add_examen(self, ex):
        """
        functie ce adauga un examen in lista de examene
        :param ex:
        :return:
        """
        self.__read_from_file()
        for examen in self.__examene:
            if examen == ex:
                raise RepoError("Exista deja acest examen!")

        self.__examene.append(ex)
        self.__load_to_file()

