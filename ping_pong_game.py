import turtle
from tkinter import font

from docutils.parsers.rst.directives.tables import align

#window===================
window=turtle.Screen()
window.title('ping pong game by mohamed khaled')
window.setup(width=800, height=600)
window.bgcolor(.1,.1,.1)
window.tracer(0)

#ball=====================
ball =turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.penup()
ball.goto(x=0, y=0)
ball_dx,ball_dy=1,1
ball_speed=0.6


#centre line===============
centre_line= turtle.Turtle()
centre_line.speed(0)
centre_line.shape('square')
centre_line.color('white')
centre_line.shapesize(stretch_len=.1, stretch_wid=25)
centre_line.penup()
centre_line.goto(0,0)

#player 1====================
p1=turtle.Turtle()
p1.speed(0)
p1.shape('square')
p1.color('blue')
p1.shapesize(stretch_len=1, stretch_wid=5)
p1.penup()
p1.goto(-350,0)

#player 2 ====================
p2=turtle.Turtle()
p2.speed(0)
p2.shape('square')
p2.color('red')
p2.shapesize(stretch_len=1, stretch_wid=5)
p2.penup()
p2.goto(350,0)

#score================
score=turtle.Turtle()
score.color('white')
score.penup()
score.goto(0,260)
score.write('Player1: 0 Player2: 0 ',align='center', font=('courier', 14,'normal'))
score.hideturtle()
p1_score,p2_score=0,0

#players movment============
p_speed=30
def p1_move_up():
    p1.sety(p1.ycor()+ p_speed)

def p1_move_down():
    p1.sety(p1.ycor()- p_speed)

def p2_move_up():
    p2.sety(p2.ycor()+ p_speed)

def p2_move_down():
    p2.sety(p2.ycor()- p_speed)
#keyboard movement==============
window.listen()
window.onkeypress(p1_move_up,'w')
window.onkeypress(p1_move_down,'s')
window.onkeypress(p2_move_up,'Up')
window.onkeypress(p2_move_down,'Down')


#game loop==================
while True:
    window.update()
    #ball movement===================
    ball.setx(ball.xcor() + (ball_dx * ball_speed))
    ball.sety(ball.ycor() + (ball_dy * ball_speed))

    if (ball.ycor() > 290):
        ball.sety(290)
        ball_dy *= -1

    if (ball.ycor() < -290):
            ball.sety(-290)
            ball_dy *= -1

    #ball collision with player 1 and player 2===================

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (p1.ycor()-60) and ball.ycor() < (p1.ycor()+60):
        ball.setx(-340)
        ball_dx *= -1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (p2.ycor()-60) and ball.ycor() < (p2.ycor()+60):
        ball.setx(340)
        ball_dx *= -1

    #  scoring ==========================

    if(ball.xcor() > 390):
        ball.goto(0,0)
        ball_dx *= -1
        score.clear()
        p1_score += 1
        score.write(f'Player1: {p1_score} Player2: {p2_score} ', align='center', font=('courier', 14, 'normal'))

    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball_dx *= -1
        score.clear()
        p2_score += 1
        score.write(f'Player1: {p1_score} Player2: {p2_score} ', align='center', font=('courier', 14, 'normal'))


















