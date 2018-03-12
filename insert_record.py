# -*- coding: utf-8 -*-

import sqlite3

conn=sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
INSERT INTO PHONEBOOK(NAME,PHONE,EMAIL)
VALUES(?,?,?)
""", ('aaa', '021-322-1542', 'shinhye@park.com'))

id=cursor.lastrowid
print(id)

cursor.execute("""
INSERT INTO PHONEBOOK(NAME,PHONE,EMAIL)
VALUES(?,?,?)
""", ('bbb', '021-445-2424', 'visal@bskim.com'))


id=cursor.lastrowid
print(id)

conn.commit()

cursor.close()
conn.close()

