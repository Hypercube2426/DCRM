import mysql.connector
from mysql.connector import Error

try:
    # Establishing connection to MySQL
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='adminroot'
    )

    # Create a cursor object
    cursorObject = database.cursor()

    # Attempt to create the database
    cursorObject.execute('CREATE DATABASE elderco')
    print("Database 'elderco' created successfully!")

except Error as e:
    # Check if the error is about the database already existing
    if "1007" in str(e):
        print("Database 'elderco' already exists.")
    else:
        print(f"Error occurred: {e}")
# finally:
#     # Closing the connection
#     if database.is_connected():
#         cursorObject.close()
#         database.close()
