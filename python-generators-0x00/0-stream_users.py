import mysql.connector

def stream_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM user_data;")

    for row in cursor:   
        yield row

    cursor.close()
    conn.close()
