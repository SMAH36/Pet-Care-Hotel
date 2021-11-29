import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(
        host='ec2-54-195-246-55.eu-west-1.compute.amazonaws.com',
        port=5432,
        database='dfl389q97gd8c6',
        user='pywbvbgjjkfnyv',
        password='50ffacc2606337e3c9d652c87509a725a515a6856fd93c9c77966995c9e05a4b')

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
