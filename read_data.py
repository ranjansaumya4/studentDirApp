import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
    'host': 'mydbtest777.mysql.database.azure.com',
    'user': 'saumya@mydbtest777',
    'password': 'Sran@1708',
    'database': 'mydatbase7'
}


def getData(roll):
    # conn = connect()
    # cursor = connect().cursor()
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(err)
        else:
            print(err)
    else:
        cursor = conn.cursor()
        query = "SELECT * FROM Students WHERE RollNo = "+str(roll)+";"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("Read", cursor.rowcount, "row(s) of data.")

        # Print all rows
        result = ""
        for row in rows:
            print((str(row)))
            result = row

        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
        print("Done.")
        return result


def createRow(params):
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(err)
        else:
            print(err)
    else:
        cursor = conn.cursor()
        query = query = "INSERT INTO Students (RollNo, Name,Email,Address) VALUES (" + str(
            params[0])+",'"+params[1]+"','"+params[2]+"','"+params[3]+"');"
        print(query)
        cursor.execute(query)
        print("Inserted", cursor.rowcount, "row(s) of data.")
        conn.commit()
        cursor.close()
        conn.close()
        print("Done.")
