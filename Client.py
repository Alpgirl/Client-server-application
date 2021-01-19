from socket import *

HOST = 'localhost'  # локальный адрес localhost или 127.0.0.1
PORT = 21111  # порт на котором работает сервер
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)  # установка связи с сервером

while True:
    #data = input('>')  # ввод данных для отправки
    #if not data:
    #    break
    ID = input('Enter ID: ')
    name = input('Enter name: ')
    city = input('Enter city: ')
    post_code = input('Enter post code: ')
    space = ' '
    #msg = 'Hello, server!'
    tcpCliSock.send(ID.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(space.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(name.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(space.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(city.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(space.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(post_code.encode('utf-8'))  # отправка данных в bytes
    tcpCliSock.send(space.encode('utf-8'))  # отправка данных в bytes

    data = tcpCliSock.recv(BUFSIZ)  # ожидание (получение) ответа
    print('Message from server: ', data.decode('utf-8')) #'length', len(data), 'byte')
    if not data:
        break
    #print(data.decode('utf8'))
    break

tcpCliSock.close()
