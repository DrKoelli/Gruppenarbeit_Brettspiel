"""
A school project
Designing a popular game
Object oriented TIC-TAC-TOE with GUI
"""

import sys
import os
from random import gauss
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        layout = QVBoxLayout(self)
        button_game = QPushButton("Play", self)
        button_game.clicked.connect(self.game)
        button_game.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_scoreboard = QPushButton("Scoreboard", self)
        button_scoreboard.clicked.connect(self.scoreboard)
        button_scoreboard.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(button_game)
        layout.addWidget(button_scoreboard)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def game(self):
        self.w = Host_or_client()
        self.w.show()
    
    def scoreboard(self):
        print("b")

class Host_or_client(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        ip_description = QLabel("Eigene IP: ", self)
        ip = QLabel("")
        ip_other_player_description = QLabel("IP des anderen Spielers: ", self)
        layout.addWidget(ip_other_player_description, 0, 0)
        ip_other_player = QLineEdit()
        layout.addWidget(ip_other_player, 0, 1)
        button_host = QPushButton("Host", self)
        layout.addWidget(button_host, 1, 0)
        button_client = QPushButton("Client", self)
        layout.addWidget(button_client, 1, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()
