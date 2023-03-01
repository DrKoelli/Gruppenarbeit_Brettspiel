import sys
import socket
import os
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
        self.w = None
        self.setFixedSize(285, 100)
        layout = QGridLayout(self)
        ip_description = QLabel("Eigene IP: ", self)
        layout.addWidget(ip_description, 0, 0)
        ip = QLabel(socket.gethostbyname(socket.gethostname()), self)
        layout.addWidget(ip, 0, 1)
        ip_other_player_description = QLabel("IP des anderen Spielers: ", self)
        layout.addWidget(ip_other_player_description, 1, 0)
        self.ip_other_player = QLineEdit()
        layout.addWidget(self.ip_other_player, 1, 1)
        button_host = QPushButton("Host", self)
        button_host.clicked.connect(self.host)
        layout.addWidget(button_host, 2, 0)
        button_client = QPushButton("Client", self)
        button_client.clicked.connect(self.client)
        layout.addWidget(button_client, 2, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def host(self):
        if(self.ip_other_player.text().strip(" ") != ""):
            self.w = Game()
            self.w.show()

    def client(self):
        pass

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.field = [[" " for x in range(3)] for y in range(3)]
        self.current_player = "X"
        self.rounds_played = 0
        layout = QGridLayout(self)
        self.setFixedSize(400, 400)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(0, 0, 255, 255))
        self.setPalette(p)
        self.group = QButtonGroup(self) 
        for x in range(3):
            for y in range(3):
                button = QPushButton()
                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                self.group.addButton(button, x*3+y)
                layout.addWidget(button, x, y)
        self.show()
        self.group.buttonClicked.connect(self.button_clicked)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def button_clicked(self, object):
        Image = QPixmap(100, 100)
        if(self.current_player == "X"):
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_x.png")
        else:
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_o.png")
        x = int(self.group.id(object)/3)
        y = self.group.id(object) - 3*x
        self.rounds_played += 1
        winner, self.field, self.current_player = main(self.rounds_played, self.current_player, self.field, x, y)
        object.setEnabled(False)
        object.setIcon(QIcon(Image))
        object.setIconSize(QSize(100, 100))
        if(winner == 0 or winner == 1 or winner == -1):
            for i in range(9):
                self.group.button(i).setEnabled(False)
            box = QMessageBox(self)
            if(winner == 0):
                box.setText("Tie")
            elif(winner == 1):
                box.setText("You have won!!!")
            else:
                box.setText("You lost!!!")
            box.exec()

        self.show()

def main(rounds_played, current_player, spielfeld, x, y):
    #player switch
    if (current_player == 'X'):
        current_player = 'O'
    else:
        current_player = 'X'
    #input from GUI (x,y) - where does the player place?
    place(spielfeld, current_player, x, y)
    L = (checkwin(spielfeld, rounds_played, current_player), spielfeld, current_player)
    return L
    
def place(spielfeld, current_player, x, y):
    spielfeld[x][y] = current_player
    
    
    
def checkwin(spielfeld, rounds_played, current_player):    
    if current_player == 'X':       #decide wether player x or o won
        answ = -1
    else:
        answ = 1
    
    for y in range(0,3):
        if((spielfeld[0][y]==current_player)and(spielfeld[1][y]==current_player)and(spielfeld[2][y]==current_player)):
            print(1)
            return answ

    for x in range (0,3):
        if((spielfeld[x][0]==current_player) and(spielfeld[x][1]==current_player)and(spielfeld[x][2]==current_player)):
            print(2)
            return answ

    # diag. to the right
    if((spielfeld[0][0]==current_player)and(spielfeld[1][1]==current_player)and(spielfeld[2][2]==current_player)):
        print(3)
        return answ

    # diag. to the left
    if(spielfeld[0][2] == current_player and spielfeld[1][1] == current_player and spielfeld[2][0] == current_player):
        return answ
    if (rounds_played > 8):
        answ = 0
        return answ
    #game goes on
    else:
        answ = 99
        return answ

app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()
