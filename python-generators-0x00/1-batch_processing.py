import mysql.connector

def stream_users_in_batches(batch_size):
    """Yield rows from user_data table in batches"""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data;")
  while True:
          batch = cursor.fetchmany(batch_size)  
          if not batch: 
              break
          yield batch  
  cursor.close()
  conn.close()

def batch_processing(batch_size):
    """Yield users over age 25 from streamed batches"""
    for batch in stream_users_in_batches(batch_size):  # loop 1
        for user in batch:  # loop 2
            if int(user["age"]) > 25:
                yield user
