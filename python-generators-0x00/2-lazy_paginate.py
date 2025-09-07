import mysql.connector

def paginate_users(page_size, offset):
    """Fetch one page of users given a page_size and offset"""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s;", (page_size, offset))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows
  
def lazy_paginate(page_size):
    """Lazily yield pages of users"""
    offset = 0
    while True:   # 🔹 only one loop
        page = paginate_users(page_size, offset)
        if not page:   # stop when no more rows
            break
        yield page
        offset += page_size
