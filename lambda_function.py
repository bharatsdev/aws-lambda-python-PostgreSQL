import os
import sys

import psycopg2

# We need to access them from AWS SSM parameter store
DB_HOST = 'POSTGRES_HOST'
DB_USER = 'POSTGRES_USER_NAME'
DB_PASSWORD = 'POSTGRES_PASSWORD'
DB_NAME = 'POSTGRES_DB'
DB_PORT = 5432
SSL_MODE = 'verify-full'
SSL_ROOT_CERT = 'cert/xxxx.pem'  # Certificate need to be downloaded from AWS for Lambda Region
SSL_ROOT_CERT = os.path.join(os.path.dirname(os.path.realpath(__file__)), SSL_ROOT_CERT)

print("SSL File Location : {}".format(SSL_ROOT_CERT))


def get_connection():
    try:
        print('[INFO] : AWS Lambda is trying to connect db......!')
        return psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_NAME, password=DB_PASSWORD,
                                sslmode=SSL_MODE,  # Pass SSL Mode
                                sslrootcert=SSL_ROOT_CERT,  # Pass Root certificate
                                database=DB_NAME)
    except BaseException as err:
        print('[ERROR]::   AWS Lambda could not connect to postgres db...! {}'.format(err))
        sys.exit()


db_conn = get_connection()
print('[INFO]:: AWS Lambda connected successfully with postgreSQL DB..!')

select_query = "SELECT * FROM FLIGHTS"


def lambda_handler(event, context):
    print('[INFO]:: AWS Lambda Handler invoked...!')
    cursor = db_conn.cursor()

    print("[INFO]:: Execute Select Query cursor.fetchall")
    cursor.execute(select_query)

    flight_data = cursor.fetchall()

    print("[INFO] :: Iterate Row of Flight data..")
    for row in flight_data:
        print("Id = ", row[0], )
        print("Airline Name = ", row[1])
        print("Destination  = ", row[2], "\n")
