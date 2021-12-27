import unittest
from functions import *
from database.database_connection import *


class Test_functions(unittest.TestCase):
    def test_idVaildetor(self):
        self.assertEqual(idVaildetor(314893587), True,
                         "valid id test should return true")
        self.assertEqual(idVaildetor(2046541),  False,
                         "not valid id test should return false")
        self.assertEqual(idVaildetor(314893585), False,
                         "not valid id test should return false")

    def test_Emailvaildetor(self):
        self.assertEqual(Emailvaildetor('whatever@ac.sce.ac.il'), True,
                         "valid email test should return true")
        self.assertEqual(Emailvaildetor('2046541@sda'),  False,
                         "not valid email test should return false")
        self.assertEqual(Emailvaildetor(';dsa02'), False,
                         "not valid email test should return false")

    def test_Passwordvaildetor(self):
        self.assertEqual(Passwordvaildetor('DSish83he@'), True,
                         "valid password test should return true")
        self.assertEqual(Passwordvaildetor('dsadas'),  False,
                         "not valid password test should return false")
        self.assertEqual(Passwordvaildetor('222222222222'), False,
                         "not valid password test should return false")

    def test_agevaildetor(self):
        self.assertEqual(agevaildetor('25'), True,
                         "valid age test should return true")
        self.assertEqual(agevaildetor('10'),  False,
                         "not valid age test should return false")
        self.assertEqual(agevaildetor('150'), False,
                         "not valid age test should return false")

    def test_phoneCheck(self):
        self.assertEqual(phoneCheck('0536214575'), True,
                         "valid phone number test should return true")
        self.assertEqual(phoneCheck('3721111'), False,
                         "not valid phone number test should return false")
        self.assertEqual(phoneCheck(''), False,
                         "not valid phone number test should return false")

    def test_checkIfUserExist(self):
        self.assertEqual(checkIfUserExist('admin'), 1,
                         "valid database test should return true")
        self.assertEqual(checkIfUserExist('3721111'), 0,
                         "not valid database test should return false")
        self.assertEqual(checkIfUserExist('dsahi82ds'), 0,
                         "not valid database test should return false")

    def test_register(self):
        self.assertEqual(register('dddddddd@.', '3213121', 'pass2dsa', 'what', 'ever', 25, 'Male', '3212111'), False,
                         "not valid database test should return false")


if __name__ == '__main__':
    unittest.main()
