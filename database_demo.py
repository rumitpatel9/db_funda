import mysql.connector

# myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin@123")
# print(myconn)

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "admin@123",database="example")
print(myconn)

cur=myconn.cursor()
print(cur)

def fetch_data(cur):
	cur.execute("select * from employee")
	result = cur.fetchall()

	for i in result:
		print(i)

def create_table(cur):
	cur.execute("create table Testing2 (Id int auto_increment,name varchar(255),age int,primary key(Id))")
	cur.execute("show tables")
	for i in cur:
		print(i)

# create_table(cur)

def insert_data(cur):
	sql = "INSERT INTO Testing1 (name,age) VALUES (%s,%s)"
	name=input("Enter name")
	age=int(input("Enter age"))
	val=(name,age)
	cur.execute(sql,val)
	myconn.commit()

insert_data(cur)