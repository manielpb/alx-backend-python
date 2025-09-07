def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS user_data(
                   user_id CHAR(36) PRIMARY KEY,
                   name VARCHAR(255) NOT NULL,
                   email VARCHAR(255) NOT NULL UNIQUE,
                   age DECIMAL(3, 0) NOT NULL,
                   INDEX (user_id)
                   ); 
                   """)
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM user_data WHERE email = %s", (data["email"],))
    result = cursor.fetchone()
    if result:
        print(f"Skipping duplicate email: {data['email']}")
    else:
        cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
        """, (str(uuid.uuid4()), data["name"], data["email"], data["age"]))
        connection.commit()
    cursor.close()

