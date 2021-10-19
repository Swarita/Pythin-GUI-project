from mysql.connector import Error
import mysql.connector as mysql


# enter your server IP address/domain name
HOST = "database-test.c19dmal1aidz.us-east-2.rds.amazonaws.com" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "test"
# this is the user you create
USER = "admin"
# user password
PASSWORD = "turtle123"
# connect to MySQL server
conn = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
cursor = conn.cursor()
print("Connected to:", conn.get_server_info())
# enter your code here!

sql = """
    select * from Persons;
   """
try:
   # Executing the SQL command
    cursor.execute(sql)

   # Commit your changes in the database
    row = cursor.fetchone()

    while row is not None:
        print(row)
        row = cursor.fetchone()

except Error as e:
    print(e)

finally:
    conn.close()