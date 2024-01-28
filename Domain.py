
class Examen:
    """
    clasa ce devineste un obiect de tip examen
    """

    def __init__(self, materie, data, ora, tip_examen):
        self.__materie = materie
        self.__data = data
        self.__zi = int(data[:2])
        self.__luna = int(data[3:])
        self.__Ora = ora
        self.__ora = int(ora[:2])
        self.__minute = int(ora[3:])
        self.__tip_examen = tip_examen

    def get_materie(self):
        return self.__materie

    def get_data(self):
        return self.__data

    def get_zi(self):
        return self.__zi

    def get_luna(self):
        return self.__luna

    def get_ora(self):
        return self.__ora

    def get_minute(self):
        return self.__minute

    def get_Ora(self):
        return self.__Ora

    def get_tip_examen(self):
        return self.__tip_examen

    def __str__(self):
        return f"{self.__materie}/{self.__data}/{self.__Ora}/{self.__tip_examen}"

    def __eq__(self, other):
        return self.__materie == other.get_materie() and self.__tip_examen == other.get_tip_examen()


