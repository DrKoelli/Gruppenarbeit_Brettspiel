"""
Elias Köll, Johannes Sieß, Loca Bombardelli, Jonas Waldner
TicTacToe mit GUI und Netzwerkfunktion
02.03.2023
"""

#imports
import sys
import socket
import os
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


def Host_connect(HOST):
    #Port and Host IP
    PORT = 61111
    #Wait for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    return s

def Makeconnection(s):
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

def Client_connect(HOST):
    #Port über welchen die Verbindung läuft
    PORT=61111
    #Adress Familie und Socket-Typ bestimmen
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect to Host
    s.connect((HOST, PORT))
    return s

def Client_send(data, s):
    s.sendall(data.encode())

def Client_recive(s):
    data = s.recv(1024)
    #data zurückgeben
    return data

#Hauptmenü
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        #layout definieren
        layout = QVBoxLayout(self)

        #buttons erstellen
        button_game = QPushButton("Play", self)
        button_game.clicked.connect(self.game)
        button_game.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button_scoreboard = QPushButton("Scoreboard", self)
        button_scoreboard.clicked.connect(self.scoreboard)
        button_scoreboard.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        
        #Buttons zu layout hinzufügen
        layout.addWidget(button_game)
        layout.addWidget(button_scoreboard)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    #Das Fenster zum Auswählen des Benutzernamen des Spielers und der IP des Gegners anzeigen
    def game(self):
        self.w = Host_or_client()
        self.w.show()
    

    #Das Scoreboard anzeigen
    def scoreboard(self):
        self.w = Scoreboard()
        self.w.show()



class Host_or_client(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(285, 118)

        #Layout erstellen
        layout = QGridLayout(self)

        #Labels und Texteingaben erstellen und zu Layout hinzufügen
        ip_description = QLabel("Eigene IP: ", self)
        layout.addWidget(ip_description, 0, 0)
        ip = QLabel(socket.gethostbyname(socket.gethostname()), self)
        layout.addWidget(ip, 0, 1)
        ip_other_player_description = QLabel("IP des anderen Spielers: ", self)
        layout.addWidget(ip_other_player_description, 1, 0)
        self.ip_other_player = QLineEdit()
        layout.addWidget(self.ip_other_player, 1, 1)
        username_description = QLabel("Username: ", self)
        layout.addWidget(username_description, 2, 0)
        self.username = QLineEdit()
        layout.addWidget(self.username, 2, 1)
        button_host = QPushButton("Host", self)
        button_host.clicked.connect(self.host)
        layout.addWidget(button_host, 3, 0)
        button_client = QPushButton("Client", self)
        button_client.clicked.connect(self.client)
        layout.addWidget(button_client, 3, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
    

    def host(self):
        #Das Spiel starten
        if(self.ip_other_player.text().strip(" ") != "" and self.username.text().strip(" ") != ""):
            IP = self.ip_other_player.text()
            server = Host_connect(IP)
            conn = Makeconnection(server)
            self.w = Game(self.username.text(), True, conn)
            self.w.show()


    def client(self):
        #das Spiel starten
        if(self.ip_other_player.text().strip(" ") != "" and self.username.text().strip(" ") != ""):
            IP = self.ip_other_player.text()
            Cserver = Client_connect(IP)
            self.w = Game(self.username.text(), False, Cserver)
            self.w.show()



class Scoreboard(QMainWindow):
    def __init__(self):
        super().__init__()
        #Den Score einlesen
        score = read()

        #Layout erstellen
        layout = QVBoxLayout()

        #Überschrift erstellen
        label = QLabel("Scoreboard", self)
        label.setFont(QFont("Times", 20))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        #Label erstellen, mit welchen die scores angezeigt werden
        for i in range(len(score)):
            label = QLabel(f"{i+1}. {score[i][0]}: {score[i][1]}", self)
            layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
        self.setFixedSize(self.size())



class Game(QMainWindow):
    def __init__(self, username, Ishost, conn):
        super().__init__()
        self.setFixedSize(400, 400)

        #Spielfeld erstellen
        self.field = [[" " for x in range(3)] for y in range(3)]

        #Variablen definieren
        self.current_player = "X"
        self.rounds_played = 0
        self.username = username
        self.conn = conn
        self.isHost = Ishost

        #layout erstellen
        layout = QGridLayout(self)

        #Dem Fenster eine blaue Hintergrundfarbe geben
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(0, 0, 255, 255))
        self.setPalette(p)

        #eine Buttongroup erstellen
        self.group = QButtonGroup(self) 

        for x in range(3):
            for y in range(3):
                #Button erstellen
                button = QPushButton()
                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                
                #Butten zu Buttongroup hinzufügen
                self.group.addButton(button, x*3+y)
                
                #Button zu layout hinzufügen
                layout.addWidget(button, x, y)

        self.group.buttonClicked.connect(self.button_clicked)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()
        if(Ishost == True):
            self.got_Cords()


    def button_clicked(self, object):
        #Den Button mit einem Bild versehen
        Image = QPixmap(100, 100)
        if(self.current_player == "X"):
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_x.png")
        else:
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_o.png")
        object.setIcon(QIcon(Image))
        object.setIconSize(QSize(100, 100))

        #Die Position des Buttons herausfinden
        x = int(self.group.id(object)/3)
        y = self.group.id(object) - 3*x

        #Die Anzahl der gespielten Runden um eins erhöhen
        self.rounds_played += 1

        #Herausfinden, ob jemand gewonnen hat und den Spieler tauschen
        winner, self.field, self.current_player = main(self.rounds_played, self.current_player, self.field, x, y)
        
        #Den Button deaktivieren
        object.setEnabled(False)

        self.show()
        self.update()

        Host_send(f"{x},{y}", self.conn)

        #Anzeigen, ob jemand gewonnen hat
        if(winner == 0 or winner == 1 or winner == -1):
            for i in range(9):
                self.group.button(i).setEnabled(False)
            box = QMessageBox(self)
            if(winner == 0):
                box.setText("Tie")
            elif(winner == 1 and self.isHost == False):
                box.setText(f"{self.username}, you have won!!!")
                save(self.username, 1)
            else:
                box.setText(f"{self.username}, you lost!!!")
            box.exec()
            return

        self.show()
        self.update()

        self.got_Cords()

    def got_Cords(self):
        #Die Koordinaten empfangen
        cords = Host_recive(self.conn)
        [x, y] = str(cords, "utf-8").split(",")
        x = int(x)
        y = int(y)

        #Dem Button ein Bild anfügen
        Image = QPixmap(100, 100)
        if(self.current_player == "X"):
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_x.png")
        else:
            Image.load(os.path.dirname(os.path.abspath(__file__))+"/TicTacToe_o.png")
        self.group.button(3*x+y).setIcon(QIcon(Image))
        self.group.button(3*x+y).setIconSize(QSize(100, 100))
        self.group.button(3*x+y).setEnabled(False)

        #Spieler wechseln und herausfinden, wer der Gewinner ist
        winner, self.field, self.current_player = main(self.rounds_played, self.current_player, self.field, x, y)
        if(winner == 0 or winner == 1 or winner == -1):
            for i in range(9):
                self.group.button(i).setEnabled(False)
            box = QMessageBox(self)
            if(winner == 0):
                box.setText("Tie")
            elif(winner == 1 and self.isHost == False):
                box.setText(f"{self.username}, you have won!!!")
                save(self.username, 1)
            else:
                box.setText(f"{self.username}, you lost!!!")
            box.exec()
            return
        self.update()
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
            return answ

    for x in range (0,3):
        if((spielfeld[x][0]==current_player) and(spielfeld[x][1]==current_player)and(spielfeld[x][2]==current_player)):
            return answ

    # diag. to the right
    if((spielfeld[0][0]==current_player)and(spielfeld[1][1]==current_player)and(spielfeld[2][2]==current_player)):
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

def save(name,win):
    #opening the save file to read and write
    fobj=open("scores.txt", "a")
    fobj.close()
    fobj=open("scores.txt", "r+")
    #saving the content of the file into a list of strings
    lines = fobj.readlines()

    # check if the given name already exists
    #enumerate keeps track of the index of each line -> enumerate(['a', 'b', 'c'])-->(0, 'a'), (1, 'b'), (2, 'c')
    for i, line in enumerate(lines):
        if line.startswith(name + ","):
                #splitting the line into two parts, the second entry->[1] should be the number of already existing wins
            parts = line.strip().split(", ")
            #saving the number of wins into a variable
            existing_win = int(parts[1])

                # Updating the score
            updated_win = existing_win + win
            #writing the file  into the line the name was found in the list named files
            lines[i] = f"{name}, {updated_win}\n"
            #navigating to the beginning of the file
            fobj.seek(0)
            #deleting the contents of the file
            fobj.truncate()
            #rewriting the file with the updated list
            fobj.writelines(lines)
            print("USER FOUND!")
            return
    #if the name does not exist we create a new entry       
    fobj.write("{}, {}\n".format(name, win))
    fobj.close()

def read():
    try:
        #creating a list that will later be filled two dimensionally->[[name1,wins1],[name2,wins2],...]
        scoreboard=[]
        #opening file
        fobj=open("scores.txt","r")
        #saving the contents of the file into a list of strings
        lines=fobj.readlines()
        for line in lines:
            #splitting the each entry into two separate strings
            name, wins = line.strip().split(", ")
            #appending the strings into the scoreboard and also converting wins into an integer
            scoreboard.append([name, int(wins)])
        #sorting the list in decending order based on the wins variable
        #"key=lambda x: x[1]" is needed to be able to refer into the inner lists as the criteria for the "sort" function
        scoreboard.sort(key=lambda x: x[1], reverse=True)
        return scoreboard
    except:
        return []

app = QApplication(sys.argv)
window = MainMenu()
window.show()
app.exec()