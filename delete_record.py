import sqlite3
conn=sqlite3.connect('test.db')
cursor=conn.cursor()

cursor.execute("""
DELETE FROM PHONEBOOK WHERE EMAIL=?
""", ('visal@bskim.com',))
conn.commit()

cursor.execute("SELECT NAME, PHONE, EMAIL FROM PHONEBOOK")

rows=cursor.fetchall()
for row in rows:
	print("NAME: {0}, PHONE: {1}, EMAIL: {2}".format(row[0], row[1], row[2]))

cursor.close()
conn.close()
