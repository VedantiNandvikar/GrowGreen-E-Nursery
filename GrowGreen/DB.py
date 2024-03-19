import sqlite3

# Create the connection object
myconn = mysql.connector.connect(host="localhost", user="root", passwd="google")

# creating the cursor object
cur = myconn.cursor()

try:
    # creating a new database
    cur.execute("plant nursary")

    # getting the list of all the databases which will now include the new database PythonDB
    dbs = cur.execute("show databases")

except:
    myconn.rollback()

for x in cur:
    print(x)

myconn.close()