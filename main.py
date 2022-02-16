# from tkinter.messagebox import NO
import psycopg2

my_hostname = "localhost"
my_database = "postgres"
my_username = "postgres"
my_password = 'zyZiek1999XD!'
my_port = 5432

conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host = my_hostname,
        dbname = my_database,
        user = my_username,
        password = my_password, 
        port = my_port)

    cursor = conn.cursor()
    cursor.execute("INSERT INTO albums (id, band, album, genre, description) VALUES (5, 'The Beatles', 'Abbey Road', 'Pop Rock', 'calm')")
    cursor.execute("SELECT * FROM albums") #test

    print(cursor.fetchall()) #test

    conn.commit()
    
except Exception as error:
    print(error)
finally:
    if conn is not None and cursor is not None:
        conn.close()
        cursor.close()

