import turtle
import random

# Screen setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle setup
def create_paddle(x, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, 0)
    return paddle


paddle_a = create_paddle(-350, "white")
paddle_b = create_paddle(350, "white")

# Ball setup
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([-0.2, 0.2])
ball.dy = random.choice([-0.2, 0.2])

# Pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Scores
score_a, score_b = 0, 0


# Functions
def paddle_up(paddle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)


def paddle_down(paddle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(lambda: paddle_up(paddle_a), "w")
wn.onkeypress(lambda: paddle_down(paddle_a), "s")
wn.onkeypress(lambda: paddle_up(paddle_b), "Up")
wn.onkeypress(lambda: paddle_down(paddle_b), "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collisions
    if abs(ball.ycor()) > 290:
        ball.dy *= -1

    # Scoring and ball reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1

    # Update the score display
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    for paddle in [paddle_a, paddle_b]:
        if (paddle.xcor() - 20 < ball.xcor() < paddle.xcor() + 20) and (
                paddle.ycor() + 50 > ball.ycor() > paddle.ycor() - 50):
            ball.setx(paddle.xcor() - 20) if ball.dx > 0 else ball.setx(paddle.xcor() + 20)
            ball.dx *= -1
