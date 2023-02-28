'''
Small Programm to connect a host to a Server and send messages with
Luca
28.02.23
'''

#Maybe unfinished / Need to test in main branch :/

import socket

def Hostf():
    #Port and Host IP
    PORT = 61111
    HOST = input("Host IP eingeben ->")
    #Wait for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

def Connectionasteblish():
    #need this before you can send anything
    conn, addr = s.accept()

def Sendmessage(data):
    #sends input
    data = bytes(data, 'utf-8')
    conn.sendall(data)


def Recivemessage():
    #recives input
    data = conn.recv(1024)
    return data
