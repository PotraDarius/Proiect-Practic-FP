import copy
import datetime

from Exceptii import *
from datetime import *
from Domain import Examen
class ServiceExamen:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def examene_maine(self, date):
        """
        functie ce afiseaza toate examenele de maine
        :param date: date-datetime
        :return:
        """
        astazi = date
        print(astazi)
        examene_maine = []
        examene = self.__repo.get_all()
        for examen in examene:
            if examen.get_zi() == astazi.day+1:
                examene_maine.append(examen)

        examene_maine.sort(key= lambda x:x.get_Ora())

        return examene_maine

    def adauga_examen(self, materie, data, ora, tip_examen):
        """
        functie ce adauga in fisier un examen nou
        :param materie: string
        :param data: string
        :param ora: string
        :param tip_examen:string
        :return:
        """
        ex = Examen(materie, data, ora, tip_examen)
        if self.__validator.validare_examen(ex) == 1:
            self.__repo.add_examen(ex)

    def examene_programate(self, data):
        """
        functie ce afiseaza toate examene programate in urmatoarele 3 zile de la data
        :param data: datetime
        :return:
        """
        examene_total = []
        examene = self.__repo.get_all()
        for i in range(0, 3):
            examene_azi = []
            for examen in examene:
                if examen.get_zi() == data.day + i:
                    examene_azi.append(examen)

            examene_azi.sort(key=lambda x: x.get_Ora())

            for examen in examene_azi:
                examene_total.append(examen)
        return examene_total

    def __sort_dupa_ora_data(self, examene):
        if not examene:
            return
        examene.sort(key=lambda x: x.get_data())
        data = examene[0].get_data()
        rezultat = []
        examene_aux = []
        for examen in examene:
            if examen.get_data() == data:
                examene_aux.append(examen)
            else:
                examene_aux.sort(key=lambda x: x.get_Ora())
                for exam in examene_aux:
                    rezultat.append(exam)
                examene_aux.clear()
                data = examen.get_data()
                examene_aux.append(examen)
        examene_aux.sort(key=lambda x: x.get_Ora())
        for exam in examene_aux:
            rezultat.append(exam)
        return rezultat

    def export(self, filename, string):
        """
        functie ce exporta intr-un fisier dat toate examenele ce contin string in materie, ordonate dupa data si ora
        :param filename: string
        :param string: string
        :return:
        """
        try:
            with open(filename, "w") as file:
                examene = self.__repo.get_all()
                examene_export = []
                for examen in examene:
                    if string in examen.get_materie():
                        examene_export.append(examen)

                rezultat = self.__sort_dupa_ora_data(examene_export)

                for examen in rezultat:
                    file.write(str(examen) + '\n')
        except IOError:
            raise ServiceError("Probleme la export!")
