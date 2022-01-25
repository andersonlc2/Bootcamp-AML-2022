import mysql.connector

class Connection:

    data_connection = mysql.connector.connect(
        host="localhost",
        database="mydb",
        user="root",
        password="admin123"
    )
    cursor = data_connection.cursor()

    def connect(data_connection=data_connection, cursor=cursor):
        if data_connection.is_connected():
            db_info = data_connection.get_server_info()
            print("Connection Sussessful: MySQL "+db_info+" version")
            return cursor

    def close(data_connection=data_connection, cursor=cursor):
        if data_connection.is_connected():
            cursor.close()
            data_connection.close()
            #print("Connection finish")