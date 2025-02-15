from turtle import *
import turtle as tur

sc = tur.Screen()
sc.setup(800,800)
sc.title("Pythontpoint")
sc.setworldcoordinates(-5,-5,5,5)
sc.bgcolor('black')
sc.tracer(0,0)
tur.hideturtle()

def draw_board():
    tur.pencolor('blue')
    tur.pensize(10)
    tur.up()
    tur.goto(-3,-1)
    tur.seth(0)
    tur.down()
    tur.fd(6)
    tur.up()
    tur.goto(-3,1)
    tur.seth(0)
    tur.down()
    tur.fd(6)
    tur.up()
    tur.goto(-1,-3)
    tur.seth(90)
    tur.down()
    tur.fd(6)
    tur.up()
    tur.goto(1,-3)
    tur.seth(90)
    tur.down()
    tur.fd(6)

def draw_circle(x,y):
    tur.up()
    tur.goto(x,y-0.75)
    tur.seth(0)
    tur.color('red')
    tur.down()
    tur.circle(0.75, steps=100)

def draw_x(x,y):
    tur.color('blue')
    tur.up()
    tur.goto(x-0.75,y-0.75)
    tur.down()
    tur.goto(x+0.75,y+0.75)
    tur.up()
    tur.goto(x-0.75,y+0.75)
    tur.down()
    tur.goto(x+0.75,y-0.75)
    
def draw_piece(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==1:
        draw_x(x,y)
    else:
        draw_circle(x,y)
    
def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,b[i][j])
    sc.update()

# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
    if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
    
def play(x,y):
    global turn
    i = 3-int(y+5)//2
    j = int(x+5)//2 - 1
    if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    draw(b)
    r = gameover(b)
    if r==1:
        sc.textinput("Game over!","X's won!")
    elif r==2:
        sc.textinput("Game over!","O's won!")
    elif r==3:
        sc.textinput("Game over!", "Tie!")
    
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
draw(b)
turn = 'x'
sc.onclick(play)
tur.mainloop()
