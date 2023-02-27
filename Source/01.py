"""
Client-Teil des Gruppenprojekts (TicTacToe)
Johannes Sieß
4AHEL
"""

#import-Statements
import socket

def Client_con():
    PORT=61111
    HOST = input("Host IP eingeben ->")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
