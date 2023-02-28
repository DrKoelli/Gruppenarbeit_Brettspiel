"""
Client-Teil des Gruppenprojekts (TicTacToe)
Johannes Sieß
23.02.2023
4AHEL
"""

#import-Statements
import socket

def Client_connect():
    PORT=61111
    HOST = input()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

def Client_send(data):
    s.sendall(data.encode())

def Client_recive():
    data = s.recv(1024)
    return data
