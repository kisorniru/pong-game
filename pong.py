# Simple Pong game in Python 3 for beginners
# By @kisorniru
# Part 1: Getting Started

import turtle
import os

# import winsound # for windows

wn = turtle.Screen()
wn.title("Pong by @kisorniru")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_left = 0
score_right = 0

# Paddle Left
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Paddle Right
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350, 0)

# Paddle Ball
paddle_ball = turtle.Turtle()
paddle_ball.speed(0)
paddle_ball.shape("square")
paddle_ball.color("white")
paddle_ball.penup()
paddle_ball.goto(0, 0)
# When we say delta (d) x, for example, we mean the change in x or how much x changes.
# Here, everything our ball moves, it moves 2px.
paddle_ball.dx = .05
# When we say delta (d) y, for example, we mean the change in y or how much y changes.
# Here, everything our ball moves, it moves 2px.
paddle_ball.dy = -.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_left_up, "Up")
wn.onkeypress(paddle_left_down, "Down")
wn.onkeypress(paddle_right_up, "Left")
wn.onkeypress(paddle_right_down, "Right")

# Main game loop
while True:
    wn.update()

    # Move the ball
    paddle_ball.setx(paddle_ball.xcor() + paddle_ball.dx)
    paddle_ball.sety(paddle_ball.ycor() + paddle_ball.dy)

    # Paddle Border checking
    if paddle_left.ycor() > 250:
        new_y = -250
        paddle_left.sety(new_y)

    if paddle_left.ycor() < -250:
        new_y = 250
        paddle_left.sety(new_y)

    if paddle_right.ycor() > 250:
        new_y = -250
        paddle_right.sety(new_y)

    if paddle_right.ycor() < -250:
        new_y = 250
        paddle_right.sety(new_y)

    # Ball Border checking
    if paddle_ball.ycor() > 290:
        paddle_ball.sety(290)
        paddle_ball.dy *= -1
        # afplay for mac
        os.system("aplay sound/bounce.wav&")
        # for windows
        # winsound.PlaySound("bounce.wav", winound.SND_ASYNC)

    if paddle_ball.ycor() < -290:
        paddle_ball.sety(-290)
        paddle_ball.dy *= -1
        os.system("aplay sound/bounce.wav&")

    if paddle_ball.xcor() > 390:
        # paddle_ball.setx(390)
        paddle_ball.goto(0, 0)
        paddle_ball.dx *= -1
        score_right += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_left, score_right), align="center",
                  font=("Courier", 24, "normal"))

    if paddle_ball.xcor() < -390:
        # paddle_ball.setx(-390)
        paddle_ball.goto(0, 0)
        paddle_ball.dx *= -1
        score_left += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_left, score_right), align="center",
                  font=("Courier", 24, "normal"))

    #  Paddle and ball collisions
    if (340 < paddle_ball.xcor() < 350) and (
            paddle_right.ycor() + 40 > paddle_ball.ycor() > paddle_right.ycor() - 40):
        paddle_ball.setx(340)
        paddle_ball.dx *= -1
        os.system("aplay sound/bounce.wav&")

    if (paddle_ball.xcor() < -340 and paddle_ball.xcor() > -350) and (
            paddle_ball.ycor() < paddle_left.ycor() + 40 and paddle_ball.ycor() > paddle_left.ycor() - 40):
        paddle_ball.setx(-340)
        paddle_ball.dx *= -1
        os.system("aplay sound/bounce.wav&")
