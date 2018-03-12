import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()

cursor.execute("""
UPDATE PHONEBOOK SET PHONE=?, EMAIL=? WHERE NAME=?
""", ('070-1234-4567', 'psh@shinhye.com', 'aaa'))

conn.commit()

cursor.execute("""
SELECT NAME, PHONE, EMAIL FROM PHONEBOOK
WHERE NAME=?
""", ('aaa',))

rows=cursor.fetchall()
for row in rows:
	print("NAME: {0}, PHONE: {1}, EMAIL: {2}".format(row[0], row[1], row[2]))

cursor.close()
conn.close()
