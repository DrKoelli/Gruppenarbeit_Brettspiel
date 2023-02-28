'''
Small Programm to connect a host to a Server and send messages with
Luca
28.02.23
'''

import socket

def Hostf():
    PORT = 61111
    HOST = input("Host IP eingeben ->")
    #Wait for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

def Sendmessage(data):
    data = bytes(data, 'utf-8')
    conn.sendall(data)


def Recivemessage():
    data = conn.recv(1024)
    return data
