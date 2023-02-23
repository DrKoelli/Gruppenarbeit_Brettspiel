"""
Koell's Branch
TTT - Game
->Main Loop
"""
x_dim = 3
y_dim = 3

def show():
    for x in range(x_dim):
        print(" {}".format(x),end="")
    print()
    for y in range(y_dim):
            for x in range(x_dim):
                print("|{}".format(spielfeld[x][y]),end="")
            print("|",y)

def main()
    while(True):
        spielfeld = [[" "]*y_dim for i in range(x_dim)]
        show()
        current_player = 'X'
        #input from GUI - where does the player place?
        #place()
        if checkwin==-1:
            print("player x won")
        if checkwin==0:
            print("TIE!!!")
        if checkwin==1:
            print("player O won")
        else:
            print("game goes on")
            current_player = 'O'
        
def place(rounds_played, current_player, x, y):
    spielfeld[x][y] = current_player
    show()
    
    
def checkwin(spielfeld, rounds_played, current_player):    
    answ = 0
    if (rounds_played > 8):
        return answ
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
    if((spielfeld[2][0]==current_player)and(spielfeld[1][1]==current_player)and(spielfeld[0][2])):
        return answ
    #game goes on
    answ = 99
    return answ

