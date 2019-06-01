import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='learnPy')
    fname = 'M'
    lname = 'nemati'
    account = 'm.nemati'
    password = '1397'

    cursor = cnx.cursor()
    cursor.execute('INSERT INTO users VALUES (\'%s\', \'%s\', \'%s\', \'%s\')'
                                               %(fname, lname, account, password))
    cnx.commit()
except mysql.connector.Error as err:
    print ('Error in Connect to DataBase %s: ' %err)
else:
    cnx.close()
