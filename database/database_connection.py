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


def register(email, phoneNumber, password, firstName, lastName, age, gender, personalId, rank='customer'):
    userId = addToUserAuth(email, phoneNumber, password)
    addToUserInfo(userId, firstName, lastName, age, gender, personalId, rank)


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


def signIn(mailOrPhone, password):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM user_auth WHERE (email = %s) OR (phone_number = %s)', (mailOrPhone, mailOrPhone))
    record = cursor.fetchall()  
    userInfo=None
    if password == record[0][3]:
        userInfo = getUserInfo(record[0][0])
    if (connection):
        cursor.close()
        connection.close()
    return(userInfo)


# print(signIn('0165592825', 'ADMSiho2dsa'))
# print(signIn('admin', 'admin'))
# register('admin', '0000000', 'admin',
#          'saher', 'bdsa', 18, 'Male', '999999', 'admin')
