#pip install mysql-connector-python
import mysql.connector

from mysql1 import parameters
#connection establishments
conn=mysql.connector.connect(host=parameters.host_is,user=parameters.user_is,password=parameters.password_is)

my_cursor=conn.cursor()
def savetoDB(text):
    que="insert into srproject.table1(srtext,length) values(%s,%s)"
    val=(text,len(text))
    my_cursor.execute(que,val)
    conn.commit()
    print("Recognised speech saved to database Sucessfully")
  
def retrive():
    my_cursor.execute("select * from srproject.table1 ")
    rows=my_cursor.fetchall()
    conn.commit()
    j=1
    for i in rows:
        print( j,")",i[0],"-->Length is :  ",i[1])
        j+=1
        
def retrivecount():
    my_cursor.execute("select * from srproject.table1 ")
    rows=my_cursor.fetchall()
    conn.commit()
    print("number of Records available is ",len(rows))
    
    

   