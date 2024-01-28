from Exceptii import *
from Domain import *

class ValidatorExamen:

    def validare_examen(self, ex):
        """
        functie ce valideaza un examen
        :param ex: Examen
        :return:
        :raises: ValidError: format data, ora nu este corect, materie vida, tip examen vid
        """

        erori = ""
        data = ex.get_data()
        if len(data) != 5:
            erori += "Formatul datei nu este corect"
        if data[2] != ".":
            erori += "Formatul datei nu este corect"
        try:
            int(data[0:2])
            int(data[3:5])
        except ValueError:
            erori += "Formatul datei nu este corect"

        ora = ex.get_Ora()
        if len(ora) != 5:
                erori += "Formatul orei nu este corect"
        if ora[2] != ":":
                erori += "Formatul orei nu este corect"
        try:
            int(ora[0:2])
            int(ora[3:5])
        except ValueError:
            erori += "Formatul orei nu este corect"

        if ex.get_materie() == "":
             erori += "Materia nu poate fi vida!"

        if ex.get_tip_examen() == "":
            erori += "Materia nu poate fi vida!"

        if erori != "":
            raise ValidError(erori)

        return 1