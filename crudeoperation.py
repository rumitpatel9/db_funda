import mysql.connector
from mysql.connector import cursor

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Darshita@11")

mycursor = mydb.cursor()

def create_database(mycursor):
    database_name=input("Database name is")
    mycursor.execute(f"Create database {database_name}")
    return database_name


def show_database(mycursor):
    mycursor.execute("show databases")

    for i in mycursor:
        print(i)

show_database(mycursor)

def create_table(mycursor):
    db=create_database(mycursor)
    mycursor.execute(f"use {db}")
    table_name=input("table name is")
    mycursor.execute(f"create table {table_name} (id int auto_increment,Name varchar(255),primary key(id))")
    return table_name
 
# create_table(mycursor)

def insert_data(mycursor):
    db=create_table(mycursor)
    sql=f"insert into {db} (id,Name) values(%s)"
    val = ("Blue Village",)
    mycursor.execute(sql,val)
    mydb.commit()
    cursor.close()
insert_data(mycursor)
