import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",passwd="admin@123",database="example")

cur = db.cursor()

# cur.execute("DELETE from employee where ID=4")
cur.execute("UPDATE employee set salary=25000 where ID=2")

db.commit()

# result=cur.fetchall()

# for x in result:
# 	print(x)