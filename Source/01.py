'''
Small Programm to connect a host to a Server and send messages with
Luca
28.02.23
'''

import socket

def Host_connect():
    #Port and Host IP
    PORT = 61111
    HOST = input("Host IP eingeben ->")
    #Wait for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    conn, addr = s.accept()
    return conn

def Host_send(data, conn):
    #sends input
    data = bytes(data, 'utf-8')
    conn.sendall(data)

def Host_recive(conn):
    #recives input
    data = conn.recv(1024)
    return data
