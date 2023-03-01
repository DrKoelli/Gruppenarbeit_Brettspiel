"""
Client-Teil des Gruppenprojekts (TicTacToe)
Johannes Sieß
23.02.2023
4AHEL
"""

#import-Statements
import socket

def Client_connect():
    #Port über welchen die Verbindung läuft
    PORT=61111
    #IP-Adresse des Host
    HOST = input()
    #Adress Familie und Socket-Typ bestimmen
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to Host
    s.connect((HOST, PORT))

def Client_send(data):
    s.sendall(data.encode())

def Client_recive():
    data = s.recv(1024)
    #data zurückgeben
    return data
