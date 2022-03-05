"""
We Returned to Our Places, These Kingdoms
No Longer at Ease, in The Old Dispensation,
With an Alien People Clutching Their Gods
I Should Be Glad of Another Death
"""
import random
import os
import turtle

lista_colori = ["#ff99ff", "#ff9999","#99ff66","#00ccff","#9900cc","#ff9900"]

colore_sfondo = random.randint(0, 5)

sfondo = turtle.Screen()
sfondo.title("Fight!")
sfondo.bgcolor(lista_colori[int(colore_sfondo)])
sfondo.setup(width = 800, height = 600)
sfondo.tracer(0)

punteggioS = 0
punteggioD = 0

racchettaS = turtle.Turtle()
racchettaS.speed(0)
racchettaS.shape("square")
racchettaS.shapesize(stretch_wid=5,stretch_len=1)
racchettaS.color("black")
racchettaS.penup()
racchettaS.goto(-350, 0)

racchettaD = turtle.Turtle()
racchettaD.speed(0)
racchettaD.shape("square")
racchettaD.shapesize(stretch_wid=5, stretch_len=1)
racchettaD.color("black")
racchettaD.penup()
racchettaD.goto(350, 0)

palla = turtle.Turtle()
palla.speed(1)
palla.shape("square")
palla.color("black")
palla.penup()
palla.goto(0,0)
palla.dx = 2
palla.dy = 2

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Giocatore Uno: 0  Giocatore Due: 0", align="center", font=("Courier", 24, "normal"))


def racchettaS_Up():
    y = int(racchettaS.ycor())
    y += 20
    racchettaS.sety(y)

def racchettaS_Down():
    y = int(racchettaS.ycor())
    y -= 20
    racchettaS.sety(y)
    
def racchettaD_Down():
    y = int(racchettaD.ycor())
    y -= 20
    racchettaD.sety(y)
    
def racchettaD_Up():
    y = int(racchettaD.ycor())
    y += 20
    racchettaD.sety(y)

sfondo.listen()
sfondo.onkeypress(racchettaS_Up(), "w")
sfondo.onkeypress(racchettaS_Down(), "s")
sfondo.onkeypress(racchettaD_Up(), "Up")
sfondo.onkeypress(racchettaD_Down(), "Down")

while True:
    sfondo.update()
    palla.setx(palla.xcor() + palla.dx)
    palla.sety(palla.ycor() + palla.dy)
    if palla.ycor() > 290:
        palla.sety(290)
        palla.dy *= -1
        os.system("afplay bounce.wav&")
    elif palla.ycor() < -290:
        palla.sety(-290)
        palla.dy *= -1
        os.system("afplay bounce.wav&")

    if palla.xcor() > 350:
        punteggioS += 1
        pen.clear()
        pen.write("Giocatore Uno: {}  Giocatore Due: {}".format(punteggioS, punteggioD), align="center", font=("Courier", 24, "normal"))
        palla.goto(0, 0)
        palla.dx *= -1
    elif palla.xcor() < -350:
        punteggioD += 1
        palla.clear()
        pen.write("Giocatore Uno: {}  Giocatore Due: {}".format(punteggioS, punteggioD), align="center", font=("Courier", 24, "normal"))
        palla.goto(0, 0)
        palla.dx *= -1

    if palla.xcor() < -340 and palla.ycor() < racchettaS.ycor() + 50 and palla.ycor() > racchettaS.ycor() - 50:
        palla.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif palla.xcor() > 340 and palla.ycor() < racchettaD.ycor() + 50 and palla.ycor() > racchettaD.ycor() - 50:
        palla.dx *= -1
        os.system("afplay bounce.wav&")
        
