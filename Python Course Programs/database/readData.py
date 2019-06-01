import mysql.connector

try:
    cnx = mysql.connector.connect(user = 'root', password = '',
                                  host = 'localhost', database = 'learnPy')
    cursor = cnx.cursor()
    query = ('SELECT * FROM users')
    cursor.execute(query)

    for (fname, lname, account, password) in cursor:
        print ('%10s %10s %10s %10s' %(fname, lname, account, password))
except mysql.connector.Error as err:
    print ('Errore in Connect to Database : %s' %err)
else:
    cnx.close()