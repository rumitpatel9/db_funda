import mysql.connector

db =mysql.connector.connect(host ='localhost',user ='root',password ='tridhya@123')
# print(db)

mycursor =db.cursor()
try:
    mycursor.execute("create database collage")
except:
    pass    
mycursor.execute("use collage")
def show_databases(mycursor):
    mycursor.execute("SHOW DATABASES")
    for database in mycursor:
        print(database)

# show_databases(mycursor)

def create_table(mycursor):
    table_name =input("enter table name: ")
    mycursor.execute(f"create table {table_name} (stu_id int auto_increment,name varchar(255),password varchar(255), primary key(stu_id))")
    print("table created...")

create_table(mycursor)

def delect_tables(mycursor):
    table_name =input("enter table name: ")
    mycursor.execute(f"delete from  {table_name}")
    print(f"{table_name} is deleted.")
    db.commit()

# delect_tables(mycursor)   

def show_tables(mycursor):
    mycursor.execute("show tables")
    for table in mycursor:
        print(table)

show_tables(mycursor)        

def drop_tables(mycursor):
    table_name =input("enter table name: ")
    mycursor.execute(f"drop table  {table_name}")
    print(f"{table_name} is drop.")

# drop_tables(mycursor) 


def add_data(mycursor):
    # stu_nu =int(input("how many stu you have????: "))
    query ="insert into  stu_info (name,password) values(%s,%s)"
    val = [
  ('qqq', '@Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
]
    mycursor.executemany(query,val)
    db.commit()
    mycursor.lastrowid
    print(f"recode inserted id is: {mycursor.lastrowid}")

add_data(mycursor)    

def show_recode_into_table(mycursor):
    mycursor.execute("select * from stu_info")
    # result =mycursor.fetchone()
    # print(result)
    for data in mycursor:
        print(data)
 



def update_data(mycursor):
    query ="update stu_info set name =%s where name =%s"
    data =('abc','rumit')
    mycursor.execute(query,data)
    db.commit()

# update_data(mycursor)  


def limit_and_offset_funda(mycursor):
    mycursor.execute("select * from stu_info limit 7 offset 19")
    for data in mycursor:
        print(data)
# limit_and_offset_funda(mycursor)
# show_recode_into_table(mycursor) 
