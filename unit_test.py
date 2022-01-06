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
        self.assertEqual(checkIfUserExist('a'), 1,
                         "valid database test should return true")
        self.assertEqual(checkIfUserExist('3721111'), 0,
                         "not valid database test should return false")
        self.assertEqual(checkIfUserExist('dsahi82ds'), 0,
                         "not valid database test should return false")

    def test_register(self):
        self.assertEqual(register('dddddddd@.', '3213121', 'pass2dsa', 'what', 'ever', 25, 'Male', '3212111'), False,
                         "not valid database test should return false")

    def test_getPetHistory(self):
        self.assertEqual(getPetHistory('30a4a169-5cca-4cb7-9fc1-3ed359675f73'), [],
                         'not vaild id should return empty list')

    def test_getCustomerHistory(self):
        self.assertEqual(getCustomerHistory('e8c6d15d-b029-4ff2-90cb-b0de8a2ec383'), [],
                         'not vaild id should return empty list')

    def test_getRoomHistory(self):
        self.assertEqual(getRoomHistory('1')[0]['room_number'], '1',
                         'room history 1 contains 1 should return true')

    def test_getAllReservations(self):
        self.assertEqual(getAllReservations('1/5/20'), [],
                         'no reservations in this date should return empty list')

    def test_getAllWorkers1(self):
        self.assertEqual('31511122128' in str(getAllWorkers1()), True,
                         'id of worker exist should return True')

    def test_getAllCustomers(self):
        self.assertEqual('3151112128' in str(getAllCustomers()), True,
                         'id of customer exist should return True')

    def test_getUncompletedTasks(self):
        self.assertEqual(getUncompletedTasks('1/5/22', 'e8c6d15d-b029-4ff2-90cb-b0de8a2ec382'), [],
                         'not vaild id should return empty list')

    def test_getUnapprovedCompletedTasks(self):
        self.assertEqual(getUnapprovedCompletedTasks('1/5/20'), [],
                         'not vaild date should return empty list')

    def test_approveTask(self):
        self.assertEqual(approveTask('1/5/20', -1, 'e8c6d15d-b029-4ff2-90cb-b0de8a2ec382'), False,
                         'not vaild data should return False')

    def test_completeTask(self):
        self.assertEqual(completeTask('1/5/20', -1, 'e8c6d15d-b029-4ff2-90cb-b0de8a2ec382'), False,
                         'not vaild data should return False')

    def test_getPetInfoByRoomNumber(self):
        self.assertEqual('Fish' in str(getPetInfoByRoomNumber('1/5/22', '1')), True,
                         'Fish is contained should return True')

    def test_getWorkerRoomsByDate(self):
        self.assertEqual(getWorkerRoomsByDate('1/5/22', 'e8c6d15d-b029-4ff2-90cb-b0de8a2ec382'), [],
                         'not vaild data should return empty list')

    def test_getCustomerResarvations(self):
        self.assertEqual("('2',)" in str(getCustomerResarvations('e8c6d15d-b029-4ff2-90cb-b0de8a2ec38c')), True,
                         '2 is contained should return True')


if __name__ == '__main__':
    unittest.main()
