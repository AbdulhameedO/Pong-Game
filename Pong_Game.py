import turtle 
player1=turtle.Turtle()
player2=turtle.Turtle()
points = turtle.Turtle()
ballz=turtle.Turtle()
mo=turtle.Screen()

mo.title("PREPARE TO LOSE")
mo.bgcolor("black")
mo.setup(width=1000, height= 600)
mo.tracer(0)


score1=0
score2=0

def up1():
    y=player1.ycor()
    if(y<240):
        y+=25
    else:
        y=240
    player1.sety(y)
def down1():
    y=player1.ycor()
    if(y>-240):
        y-=25
    else:
        y=-240   
    player1.sety(y)
def up2():
    y=player2.ycor()
    if(y<240):
        y+=25
    else:
        y=240
    player2.sety(y)
def down2():
    y=player2.ycor()
    if(y>-240):
        y-=25
    else:
        y=-240
    player2.sety(y)
#def exit():
#    ballz.home()
#    mo.update()
#   mo.exitonclick()

mo.listen()
mo.onkeypress(up1,"w")
mo.onkeypress(down1,"s")
mo.onkeypress(up2,"Up")
mo.onkeypress(down2,"Down")
#mo.onkeypress(exit,"Escape")

#Paddle size is 120X20
player1.speed(0)
player1.shape("square")
player1.color("green")
player1.shapesize(stretch_wid=6, stretch_len=1)
player1.penup()
player1.goto(-470,0)

player2.speed(0)
player2.shape("square")
player2.color("blue")
player2.shapesize(stretch_wid=6, stretch_len=1)
player2.penup()
player2.goto(470,0)

points.speed(0)
points.penup()
points.hideturtle()
points.color("pink")
points.goto(0,250)
points.write("Player 1: 0  Best of three  Player 2: 0 ",align="center",font=("Courier", 20, "normal")) 

ballz.speed(0)
ballz.shape("circle")
ballz.color("yellow")
ballz.penup()
ballz.goto(0,0)


dx=0.5
dy=0.5
x=ballz.xcor()
y=ballz.ycor()
z=True

while z:
    mo.update()
    if(x>=480):
        dx*=-1
    else: 
        if(x<=-480):
            dx*=-1

    if(y>=280):
        dy*=-1
    else:
        if(y<=-280):
            dy*=-1
    
    x+=dx
    y+=dy

    if(x>=player2.xcor()-20 and y<=player2.ycor()+60 and y>=player2.ycor()-60):
        x=player2.xcor()-20
        dx*=-1
    
    if(x<=player1.xcor()+20 and y<=player1.ycor()+60 and y>=player1.ycor()-60):
        x=player1.xcor()+20
        dx*=-1
    
    ballz.setposition(x,y)

    if(x==480 or x==-480):
        ballz.home()
        dx*=-1
        if(x==480):
            score1+=1            #increase speed as points increase
            points.clear()
            points.write("Player 1: {}  Best of three  Player 2: {}".format(score1,score2),align="center",font=("Courier", 20, "normal"))   
        else:
            score2+=1
            points.clear()
            points.write("Player 1: {}  Best of three  Player 2: {}".format(score1,score2),align="center",font=("Courier", 20, "normal"))

        x=0
        y=0
        
    if(score1==3 or score2==3):
        z=0
if score1==3:
    points.clear()
    points.write("Player 1: 3  HA HA  Player 2: LOSER",align="center",font=("Courier", 20, "normal"))
else:
    points.clear()
    points.write("Player 1: LOSER  HA HA  Player 2: 3",align="center",font=("Courier", 20, "normal"))
    
    
mo.update()
mo.exitonclick()

mo.mainloop()
