import mysql.connector

def connect_db(user, password):
    try:
        return mysql.connector.connect(
            host="localhost",
            user=user,
            password=password,
            database="prod"
        )
    except:
        print("DB failed")
        return None
