"""
Koell's Branch
TTT - Game
->Main Loop (Checkwin, Playerswitch, etc....:)
"""

#sepp
def show():
    for x in range(3):
        print(" {}".format(x),end="")
    print()
    for y in range(3):
            for x in range(3):
                print("|{}".format(spielfeld[x][y]),end="")
            print("|",y)



def main(rounds_played, current_player, spielfeld, x, y):
    #player switch
    if (current_player == 'X'):
        current_player = 'O'
    else:
        current_player = 'X'
    #input from GUI (x,y) - where does the player place?
    place(spielfeld, current_player, x, y)
    L = (checkwin(spielfeld, rounds_played, current_player), spielfeld)
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
    if((spielfeld[2][0]==current_player)and(spielfeld[1][1]==current_player)and(spielfeld[0][2])):
        return answ
    if (rounds_played > 8):
        answ = 0
        return answ
    #game goes on
    else:
        answ = 99
        return answ
