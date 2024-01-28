import datetime
import unittest
from Domain import Examen
from Repository import FileRepositoryExamen
from Validator import  ValidatorExamen
from Exceptii import *

class TesteDomain(unittest.TestCase):

    def setUp(self):
        self.__ex = Examen("FP", "20.02", "08:00", "normal")

    def test_creeare_examen(self):
        self.assertEqual(self.__ex.get_Ora(), "08:00")
        self.assertEqual(self.__ex.get_data(), "20.02")


class TesteRepository(unittest.TestCase):

    def setUp(self):
        self.__repo = FileRepositoryExamen("test.txt")

    def test_get_all(self):
        self.assertEqual(len(self.__repo.get_all()), 7)

    def test_add_examen(self):
        ex = Examen("FP", "20.02", "08:00", "normal")
        with self.assertRaises(RepoError):
            self.__repo.add_examen(ex)


class TesteValidator(unittest.TestCase):
    def setUp(self):
        self.__validator = ValidatorExamen()
        self.__ex1 = Examen("FP", "20.02", "08:00", "normal")
        self.__ex2 = Examen("FP", "20.02", "08:00", "")

    def test_validare_examen(self):
        self.assertEqual(self.__validator.validare_examen(self.__ex1), 1)
        with self.assertRaises(ValidError):
            self.__validator.validare_examen(self.__ex2)

