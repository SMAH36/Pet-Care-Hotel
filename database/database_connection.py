from tkinter.constants import NONE
from typing import Coroutine
import psycopg2
from psycopg2 import Error


def connectToDb():
    try:
        connection = psycopg2.connect(
            host='ec2-54-195-246-55.eu-west-1.compute.amazonaws.com',
            port=5432,
            database='dfl389q97gd8c6',
            user='pywbvbgjjkfnyv',
            password='50ffacc2606337e3c9d652c87509a725a515a6856fd93c9c77966995c9e05a4b')
        cursor = connection.cursor()
        return connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)


def addToUserAuth(email, phoneNumber, password):
    connection = connectToDb()
    cursor = connection.cursor()
    insert_script = """INSERT INTO user_auth (email, phone_number, password) VALUES(%s, %s, %s) RETURNING id"""
    insert_value = (email, phoneNumber, password)
    cursor.execute(insert_script, insert_value)
    record = cursor.fetchone()
    connection.commit()
    if (connection):
        cursor.close()
        connection.close()
    return(record[0])


def getUserIdByEmail(mailOrPhone):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_auth WHERE (email = %s) OR (phone_number = %s)', (mailOrPhone, mailOrPhone))
    record = cursor.fetchone()
    if (connection):
        cursor.close()
        connection.close()
    return(record[0])


def addToUserInfo(userId, firstName, lastName, age, gender, personalId, rank):
    connection = connectToDb()
    cursor = connection.cursor()
    insert_script = """INSERT INTO user_info (user_id, first_name, last_name, age, gender, personal_id,rank) VALUES(%s, %s, %s,%s,%s,%s,%s) RETURNING ID"""
    insert_value = (userId, firstName, lastName, age, gender, personalId, rank)
    cursor.execute(insert_script, insert_value)
    record = cursor.fetchall()
    connection.commit()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getUserInfo(userId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM user_info WHERE user_id = '{userId}'")
    record = cursor.fetchone()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def checkIfUserExist(mailOrPhone):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_auth WHERE (email = %s) OR (phone_number = %s)', (mailOrPhone, mailOrPhone))
    record = cursor.rowcount
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def signIn(mailOrPhone, password):
    if(checkIfUserExist(mailOrPhone) == 0):
        return False
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_auth WHERE (email = %s) OR (phone_number = %s)', (mailOrPhone, mailOrPhone))
    record = cursor.fetchall()
    userInfo = None
    if password == record[0][3]:
        userInfo = getUserInfo(record[0][0])
    else:
        userInfo = False
    if (connection):
        cursor.close()
        connection.close()
    return(userInfo)


def register(email, phoneNumber, password, firstName, lastName, age, gender, personalId, rank='customer'):
    if checkIfUserExist(email) == 0 or checkIfUserExist(phoneNumber) == 0:
        userId = addToUserAuth(email, phoneNumber, password)
        addToUserInfo(userId, firstName, lastName,
                      age, gender, personalId, rank)
        return True
    return False


def removeUser(mailOrPhone):
    if checkIfUserExist(mailOrPhone) == 1:
        userId = getUserIdByEmail(mailOrPhone)
        connection = connectToDb()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN")
            cursor.execute(f"DELETE FROM user_auth WHERE id = '{userId}'")
            cursor.execute(f"DELETE FROM user_info WHERE user_id = '{userId}'")
            cursor.execute("COMMIT")
            if (connection):
                cursor.close()
                connection.close()
            return True
        except:
            cursor.execute("ROLLBACK")
            if (connection):
                cursor.close()
                connection.close()
            return False
    return False


def userPromotion(mailOrPhone, rank='worker'):
    if checkIfUserExist(mailOrPhone) == 1:
        userId = getUserIdByEmail(mailOrPhone)
        connection = connectToDb()
        cursor = connection.cursor()
        try:
            cursor.execute("BEGIN")
            cursor.execute(
                f"UPDATE user_info SET rank = '{rank}' WHERE user_id = '{userId}'")
            cursor.execute("COMMIT")
            if (connection):
                cursor.close()
                connection.close()
            return True
        except:
            cursor.execute("ROLLBACK")
            if (connection):
                cursor.close()
                connection.close()
            return False
    return False


def addPet(userId, petName, petType, age, gender, petPersonalId):
    connection = connectToDb()
    cursor = connection.cursor()
    insert_script = """INSERT INTO pets_info (user_id, pet_name, pet_type, age, gender ,pet_personal_id) VALUES(%s, %s, %s,%s,%s,%s)"""
    insert_value = (userId, petName, petType, age, gender, petPersonalId)
    try:
        cursor.execute(insert_script, insert_value)
        connection.commit()
        if (connection):
            cursor.close()
            connection.close()
        return(True)
    except:
        if (connection):
            cursor.close()
            connection.close()
        return(False)


def reservedRoomsByDate(startDate, endDate):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""SELECT (room_number) FROM room_reservation WHERE
        (end_date >= '{startDate}' AND start_date <= '{startDate}')
        OR (start_date <= '{endDate}' AND end_date >= '{endDate}')
        OR (start_date >= '{startDate}' AND end_date <= '{endDate}')""")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def reserveRoom(roomNumber, petId, userId, startDate, endDate):
    connection = connectToDb()
    cursor = connection.cursor()
    insert_script = """INSERT INTO room_reservation (room_number, pet_id, user_id, start_date, end_date) VALUES(%s, %s, %s,%s,%s)"""
    insert_value = (roomNumber, petId, userId, startDate, endDate)
    try:
        cursor.execute(insert_script, insert_value)
        connection.commit()
        if (connection):
            cursor.close()
            connection.close()
        return(True)
    except:
        if (connection):
            cursor.close()
            connection.close()
        return(False)


def getPetsByUSERid(userId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (pet_name,pet_type,id,age,gender,pet_personal_id) FROM pets_info WHERE user_id = '{userId}'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getPetInfoByPetId(petId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (pet_name,pet_type,id,age,gender,pet_personal_id) FROM pets_info WHERE id = '{petId}'")
    record = cursor.fetchone()
    if (connection):
        cursor.close()
        connection.close()
    return(record[0])


def getAllWorkers():
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (user_id,first_name,personal_id) FROM user_info WHERE rank = 'worker'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getAllRoomsWorkers(date):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (room_number) FROM rooms_workers WHERE date = '{date}'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def setWorkerToRoom(date, roomNumbers, userId):
    connection = connectToDb()
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN")
        for room in roomNumbers:
            cursor.execute(
                f"""INSERT INTO rooms_workers (date, room_number, user_id) VALUES('{date}','{room}','{userId}')""")
        cursor.execute("COMMIT")
        if (connection):
            cursor.close()
            connection.close()
        return(True)
    except:
        cursor.execute("ROLLBACK")
        if (connection):
            cursor.close()
            connection.close()
        return(False)

# didnt check it yet


def getCustomerResarvations(userId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""SELECT (room_number) FROM room_reservation WHERE user_id = '{userId}'""")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def deleteResarvation(userId, petId, startDate, endDate):
    # delete reseved room if not assiegnd yet to worker
    # didnt start the date yet
    connection = connectToDb()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"DELETE FROM room_reservation WHERE user_id = '{userId}' AND pet_id = '{petId}' AND start_date = '{startDate} AND end_date= '{endDate}' ")
        if (connection):
            cursor.close()
            connection.close()
        return True
    except:
        if (connection):
            cursor.close()
            connection.close()
        return False


def getWorkerRoomsByDate(date, userId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (room_number) FROM rooms_workers WHERE date = '{date}' AND user_id= '{userId}'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getPetInfoByRoomNumber(date, roomNumber):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT (pet_id) FROM room_reservation WHERE room_number = '{roomNumber}' AND
        (end_date >= '{date}' AND start_date <= '{date}')
        """)
    record = cursor.fetchone()
    if (connection):
        cursor.close()
        connection.close()
    return(getPetInfoByPetId(record[0]))


def changeWorkerRoom(date, roomNumber, newUserId):
    connection = connectToDb()
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN")
        cursor.execute(
            f"UPDATE rooms_workers SET user_id = '{newUserId}' WHERE date = '{date}' AND room_number= '{roomNumber}'")
        cursor.execute("COMMIT")
        if (connection):
            cursor.close()
            connection.close()
        return True
    except:
        cursor.execute("ROLLBACK")
        if (connection):
            cursor.close()
            connection.close()
        return False


def completeTask(date, roomNumbers, userId):
    connection = connectToDb()
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN")
        for room in roomNumbers:
            cursor.execute(
                f"UPDATE rooms_workers SET task_completed = TRUE WHERE date = '{date}' AND room_number= '{room}' AND user_id = '{userId}'")
        cursor.execute("COMMIT")
        if (connection):
            cursor.close()
            connection.close()
        return True
    except:
        cursor.execute("ROLLBACK")
        if (connection):
            cursor.close()
            connection.close()
        return False


def approveTask(date, roomNumbers, userId):
    connection = connectToDb()
    cursor = connection.cursor()
    try:
        cursor.execute("BEGIN")
        for room in roomNumbers:
            cursor.execute(
                f"UPDATE rooms_workers SET approved = TRUE WHERE date = '{date}' AND room_number= '{room}' AND user_id = '{userId}'")
        cursor.execute("COMMIT")
        if (connection):
            cursor.close()
            connection.close()
        return True
    except:
        cursor.execute("ROLLBACK")
        if (connection):
            cursor.close()
            connection.close()
        return False


def getUnapprovedCompletedTasks(date):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (room_number) FROM rooms_workers WHERE date = '{date}' AND approved = 'FALSE' AND task_completed = 'TRUE'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getUncompletedTasks(date, userId):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (room_number) FROM rooms_workers WHERE date = '{date}' AND user_id= '{userId}' AND approved = 'FALSE' AND task_completed = 'FALSE'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getAllCustomers():
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (first_name,last_name,age,gender,personal_id) FROM user_info WHERE rank = 'customer'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)

def getAllWorkers1():
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT (first_name,last_name,age,gender,personal_id) FROM user_info WHERE rank = 'worker'")
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return(record)


def getReservationInfoByRoomNumber(date, roomNumber):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT (pet_id,user_id,start_date,end_date) FROM room_reservation WHERE room_number = '{roomNumber}' AND
        (end_date >= '{date}' AND start_date <= '{date}')
        """)
    record = cursor.fetchone()
    res = False
    if (connection):
        cursor.close()
        connection.close()
    if record != None:
        petInfo = getPetInfoByPetId(record[0].replace(
            '(', '').replace(')', '').split(',')[0])
        userInfo = getUserInfo(record[0].replace(
            '(', '').replace(')', '').split(',')[1])
        res = petInfo, userInfo, record[0].replace('(', '').replace(')', '').split(
            ',')[2], record[0].replace('(', '').replace(')', '').split(',')[3]
    return res


def getAllReservations(date):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT (room_number,start_date,end_date) FROM room_reservation WHERE end_date >= '{date}' AND start_date <= '{date}'
        """)
    record = cursor.fetchall()
    if (connection):
        cursor.close()
        connection.close()
    return record

# room history


def getRoomHistory(roomNumber):
    # w8
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT (room_number,user_id,start_date,end_date) FROM room_reservation WHERE room_number = '{roomNumber}'
        """)
    records = cursor.fetchall()
    result = []
    for record in records:
        record = record[0].replace('(', '').replace(')', '').split(',')
        cursor = connection.cursor()
        cursor.execute(
            f"""
        SELECT (first_name,last_name,personal_id) FROM user_info WHERE user_id = '{record[1]}'
        """)
        userInfo = cursor.fetchone()[0].replace(
            '(', '').replace(')', '').split(',')
        dec = {'room_number': record[0], 'start_date': record[2],
               'end_date': record[3], 'user': [userInfo[0], userInfo[1], userInfo[2]]}
        result.append(dec)

    if (connection):
        cursor.close()
        connection.close()
    return result


print(getRoomHistory(1))
# print(getReservationInfoByRoomNumber('1/5/22', 1))
# print(getAllReservations('1/5/22'))

# print(getAllCustomers())

# print(getWorkerRoomsByDate("1/4/22", '8d6ad7c9-7a1a-42fb-bfee-2ad508749225'))
# print(getPetInfoByRoomNumber("1/4/22", 2))
# print(setWorkerToRoom('12/28/21', 1, '7859f3b9-e14e-47da-b1f5-7caa5f260b04'))
# print(getAllRoomsWorkers('12/28/21'))
# print(getAllWorkers())
# print(getPetsByUSERid('1309daf1-70c7-4e60-8a52-3866203824a5'))
# 1309daf1-70c7-4e60-8a52-3866203824a5
# print(register('w2', '12311123', 'w2', 'ayal','bta', 18, 'Male', '222222222', 'worker'))
# print(register('c1', '1151111', 'c', 'heba',
#                'bta', 18, 'Male', '511122128', 'customer'))
# print(reserveRoom('3', 'ba8beb62-5eb4-4f93-a2a0-657ba7d2a419',
#       'e8c6d15d-b029-4ff2-90cb-b0de8a2ec38c', '10/10/21', '10/12/21'))
# print(reservedRoomsByDate('10/9/21', '10/13/21'))
# print(signIn('0165592825', 'ADMSiho2dsa'))
# print(signIn('admin', 'admin'))
# register('admin', '0000000', 'admin',
#          'saher', 'bdsa', 18, 'Male', '999999', 'admin')
# print(removeUser('aaaaaaaa@.'))
# print(userPromotion('dddddddd@.'))
# print('addingPet:', addPet('a3cc2fa0-8392-44ca-bdd4-525e2d54975f',
#       'sami', 'Dog', '6', 'Male', '165018488'))
