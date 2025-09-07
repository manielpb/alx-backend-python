import mysql.connector

def stream_user_ages():
    """Yield user ages lazily from user_data table"""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT age FROM user_data;")
    for (age,) in cursor:   # loop 1
        yield int(age)

    cursor.close()
    conn.close()

def compute_average_age():
    total_age = 0
    count = 0
    for age in stream_user_ages():   # loop 2
        total_age += age
        count += 1
    return total_age / count if count > 0 else 0
