"""
Koell's Branch
TTT - Game
->Main Loop
"""

def checkwin(playfield, rounds_played, current_player):
    
    
    for y in range(0,3):
        if((playfield[0][y]==current_player)and(playfield[1][y]==current_player)and(playfield[2][y]==current_player)):
            return True

    for x in range (0,3):
        if((playfield[x][0]==current_player) and(playfield[x][1]==current_player)and(playfield[x][2]==current_player)):
            return True

    # diag. nach rechts
    if((playfield[0][0]==current_player)and(playfield[1][1]==current_player)and(playfield[2][2]==current_player)):
        return True
   
    # diag. nach links
    if((playfield[2][0]==current_player)and(playfield[1][1]==current_player)and(playfield[0][2])):
        return True
   
    return False

