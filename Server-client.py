from socket import *
import sqlite3
from sqlite3 import Error
import string
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

HOST = 'localhost'  # адрес хоста (сервера) пустой означает использование любого доступного адреса
PORT = 21111  # номер порта на котором работает сервер (от 0 до 65525, порты до 1024 зарезервированы для системы, порты TCP и UDP не пересекаются)
BUFSIZ = 1024  # размер буфера 1Кбайт
ADDR = (HOST, PORT)  # адрес сервера
tcpSerSock = socket(AF_INET, SOCK_STREAM)  #создаем сокет сервера
#result = tcpSerSock.connect_ex(('irc.myserver.net', 21111))
#if result == 0:
#    print ("Port is open")
#else:
#    print ("Port is not open")


tcpSerSock.bind(ADDR)  # связываем сокет с адресом
tcpSerSock.listen(5)  # устанавливаем максимальное число клиентов одновременно обслуживаемых

msg = list()
#def create_connection(db_file):
#    conn = None
#    try:
#        conn = sqlite3.connect(db_file)
#        print(sqlite3.version)
#    except Error as e:
#        print(e)
#    finally:
#        if conn:
#            conn.close()
#if __name__ == 'main':
#    create_connection(r"C:/home/inna/data.db")
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
print('Succesfully Connected to SQLite')
#connection = mysql.connector.connect(host='127.0.0.1',
#                             port ='21111',
#                             database ='main',
#                             user='inna',
#                             password='larina2001')
#cursor.execute("CREATE TABLE data (ID integer primary key, name text, city text, post_code integer)")

while True:  # бесконечный цикл сервера
    print('Waiting for client...')
    tcpCliSock, addr = tcpSerSock.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет tcpCliSock)
    print('Connected from: {}'.format(addr))

    #while True:  # цикл связи
#        try:
#            mySql_insert_query = """INSERT INTO data (ID, NAME, CITY, POSTAL_CODE)
#                                    VALUES
#                           (1, 'Maria Anders', 'Berlin', 12209) """
#            cursor = connection.cursor()
#            cursor.execute(mySql_insert_query)
#            connection.commit()
#            print(cursor.rowcount, "Record inserted successfully into data table")
#            cursor.close()
#        except mysql.connector.Error as error:
#            print("Failed to insert record into data table {}".format(error))
#        cursor.executescript("""
        #curs = conn.execute('select * from data')
        #names = [description[0] for description in curs.description]
        #print (names)
    while True:
        data = tcpCliSock.recv(BUFSIZ)  # принимает данные от клиента
        if not data:
            break
        if data.decode('utf-8').isdigit():
            msg = data.decode('utf-8')
            print(msg)
            msg = int(msg)
            cursor.execute("SELECT * FROM data where ID = ?", (msg,))
            row = cursor.fetchall()
            print(row)
            #str = ''
            def convertTuple(tup):
                der = " ".join(str(x) for x in tup)
                return der
            inf = convertTuple(row)
            print(inf)
            #tcpCliSock.send(x.encode('utf-8') for x in row)
            #inf = [x.encode('utf-8') for x in row]
            tcpCliSock.send(inf.encode('utf-8'))
            break
        else:
            msg = data.decode('utf-8').split()
            print(msg)
            cursor.execute("INSERT OR REPLACE INTO data (ID, name, city, post_code) VALUES (?, ?, ?, ?)", (msg[0], msg[1], msg[2], msg[3]))
            cursor.execute("SELECT * FROM data")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            msg = "Record inserted successfully into data table"
        #print ('Message:', data.decode('utf-8'), ' come from: ', addr)
        #msg = "Play volleyball today"
            tcpCliSock.send(msg.encode('utf-8'))
        #count = cursor.execute(sqlite_insert_query)

        #cursor.execute("INSERT INTO data VALUES (1, 'Maria Anders', 'Berlin', 12209)")
        #cursor.execute("INSERT INTO data VALUES ('NAME', 'Maria Anders')")
        #cursor.execute("SELECT * FROM data")
        #print(cursor.fetchall())
         # insert into data values (Null, '1');
          #insert into data values (Null, 'Artem');
          #""")
         #(input("Введите ID"), input("Введите имя"))
         # insert into CITY value (input("Введите город"))";
         # insert into POSTAL_CODE value (input("Введите почтовый код"));
         # """")
        #cursor.execute("SELECT Name FROM ID ORDER BY Name NAME")
        #results = cursor.fetchall()
        #print(results)
        #data = tcpCliSock.recv(BUFSIZ)  # принимает данные от клиента
        #    if not data:
        #        break  # разрываем связь если данных нет
        #tcpCliSock.send(bytes('You sent me "{}"'.format(data.decode('utf8')), 'utf8'))  # отвечаем клиенту его же данными
        #tcpCliSock.send(msg.encode('utf-8'))
            break
    tcpCliSock.close()  # закрываем сеанс (сокет) с клиентом
    break
conn.commit()
#print("Record inserted successfully into data table")# cursor.rowcount)
cursor.close()
#curs.close()
conn.close()
#if (connection.is_connected()):
#    connection.close()
#    print("MySQL connection is closed")
tcpSerSock.close()  # закрытие сокета сервера
