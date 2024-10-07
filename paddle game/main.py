# Pong
import turtle
#import winsound
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
count_o = 0
count_t = 0

# Paddle left
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=3, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# Paddle right
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=3, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.90000
ball.dy = -0.90000

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_One: 0  Player_Two: 0", align="center", font=("Courier", 24, "normal"))


# paddle function
def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)


# KeyBind
wn.listen()
wn.onkeypress(paddle_l_up, "a")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "j")
wn.onkeypress(paddle_r_down, "k")

# Game loop
while True:
    wn.update()

    # ball movement
    ball.setx(ball.xcor() + ball.dx * 2)
    ball.sety(ball.ycor() + ball.dy * 2)

    # border hitscan
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        count_o += 1
        pen.clear()
        pen.write("Player one: {}  Player two: {}".format(count_o, count_t), align="center",
                  font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        count_t += 1
        pen.clear()
        pen.write("Player One: {}  Player Two: {}".format(count_o, count_t), align="center",
                  font=("Courier", 24, "normal"))

    # paddle-ball hitscan
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_r.ycor() + 40 and ball.ycor() > paddle_r.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_l.ycor() + 40 and ball.ycor() > paddle_r.ycor()   - 50):
        ball.setx(-340)
        ball.dx *= -1
