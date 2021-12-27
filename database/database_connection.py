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


def reserveRoom(roomNumber, petId, startDate, endDate):
    connection = connectToDb()
    cursor = connection.cursor()
    insert_script = """INSERT INTO room_reservation (room_number, pet_id, start_date, end_date) VALUES(%s, %s, %s,%s)"""
    insert_value = (roomNumber, petId, startDate, endDate)
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


# print(getPetsByUSERid('1309daf1-70c7-4e60-8a52-3866203824a5'))
# 1309daf1-70c7-4e60-8a52-3866203824a5
# print(register('a', 'a', '1293', 'eyal', 'bta', 18, 'Male', '3271312'))
# print(reserveRoom('2', 'e63a2dd6-719c-4366-a103-0f162f16776e', '10/10/21', '10/12/21'))
# print(reservedRoomsByDate('10/9/21', '10/13/21'))
# print(signIn('0165592825', 'ADMSiho2dsa'))
# print(signIn('admin', 'admin'))
# register('admin', '0000000', 'admin',
#          'saher', 'bdsa', 18, 'Male', '999999', 'admin')
# print(removeUser('aaaaaaaa@.'))
# print(userPromotion('dddddddd@.'))
# print('addingPet:', addPet('a3cc2fa0-8392-44ca-bdd4-525e2d54975f',
#       'sami', 'Dog', '6', 'Male', '165018488'))
