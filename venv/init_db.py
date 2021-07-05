import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor();
cur.execute('drop table Employee')
cur.execute('create table Employee(Name varchar(50),Designation varchar(100),Address varchar(50),Phone int(10))')

cur.execute("insert into Employee values('Steve Jobs','CEO','Bangalore',99999999)")
cur.execute("insert into Employee values('Tom Cook','CTO','Bangalore',88888880)")
cur.execute("insert into Employee values('Elon Musk','Innovator','Bangalore',7777777)")

conn.commit()
conn.close()