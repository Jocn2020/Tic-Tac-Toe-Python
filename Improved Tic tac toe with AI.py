#Tic Tac Toe
from tkinter import *
from tictactoe import *
import sys
sys.setrecursionlimit(10000)

def callback(x,y):
    global players
    global turn
    global stop_game
    
    if players == 'X' and placed[x][y] == 0 and stop_game == False:
        buttons[x][y].configure(text='X')
        placed[x][y] = 'X'
        players = 'O'
        title.configure(text='Player {} Turn'.format(turn%2+1))
        check_winner()
        turn+=1

        if(turn<9):
            #AI Turn
            move = minimax(placed)
            buttons[move[0]][move[1]].configure(text='O')
            placed[move[0]][move[1]] = 'O'
            players = 'X'
            title.configure(text='Player {} Turn'.format(turn%2+1))
            check_winner()
            turn+=1
        
def check_winner():
    global stop_game #to change stop_game variable
    for i in range(3):
        if placed[i][0] == placed[i][1] == placed[i][2]!= 0:
            buttons[i][0].configure(bg='grey')
            buttons[i][1].configure(bg='grey')
            buttons[i][2].configure(bg='grey')
            title.configure(text='Player {} Win'.format(turn%2+1))
            stop_game=True

    for i in range (3):
        if placed[0][i] == placed[1][i] == placed[2][i]!= 0:
            buttons[0][i].configure(bg='grey')
            buttons[1][i].configure(bg='grey')
            buttons[2][i].configure(bg='grey')
            title.configure(text='Player {} Win'.format(turn%2+1))
            stop_game=True
            
    if placed[0][0] == placed[1][1] == placed[2][2] != 0:
        buttons[0][0].configure(bg='grey')
        buttons[1][1].configure(bg='grey')
        buttons[2][2].configure(bg='grey')
        title.configure(text='Player {} Win'.format(turn%2+1))
        stop_game=True

    if placed[0][2] == placed[1][1] == placed[2][0] != 0:
        buttons[2][0].configure(bg='grey')
        buttons[1][1].configure(bg='grey')
        buttons[0][2].configure(bg='grey')
        title.configure(text='Player {} Win'.format(turn%2+1))
        stop_game=True

    if turn == 9 and stop_game == False:
        title.configure(text='Player 1 and Player 2 are draw')
        stop_game=True

def start():
    global players
    global turn
    global stop_game
    
    for a in range(3):
        for b in range(3):
            buttons[a][b].configure(text='', bg='yellow')
            placed[a][b] = 0
            
    title.configure(text='Player 1 Turn')        
    players='X'
    turn = 1
    stop_game = False
    
root = Tk()
title= Label(text='Player 1 Turn')
title.grid(row=0, column=0, columnspan=2)
buttons=[[0,0,0],
         [0,0,0],
         [0,0,0]]
placed= initial_state()
    
for i in range(3):
    for j in range(3):
        buttons[i][j]=Button(font=('Verdana',56), width=3, bg='yellow',
                             command = lambda x=i, y=j: callback(x,y))
        buttons[i][j].grid(row=i+1, column=j)

turn = 1
stop_game = False
players = 'X'
restart = Button(text='Restart', command = start)
restart.grid(row=0, column=2)
    
mainloop()
                     
