import db

cursor = cnx.cursor()
cursor.execute('INSERT INTO users VALUES (\'ali\', \'nemati\', \'a.nemati\', \'1397\')')
cnx.commit()