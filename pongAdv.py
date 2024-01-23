import turtle
import random


class Paddle(turtle.Turtle):
    def __init__(self, x, color):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x, 0)


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = random.choice([-0.2, 0.2])
        self.dy = random.choice([-0.2, 0.2])


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)


class PongGame:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong Game")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        self.paddle_a = Paddle(-350, "white")
        self.paddle_b = Paddle(350, "white")
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.score_a = 0
        self.score_b = 0

        self.configure_keyboard_bindings()

    def configure_keyboard_bindings(self):
        self.wn.listen()
        self.wn.onkeypress(lambda: self.paddle_up(self.paddle_a), "w")
        self.wn.onkeypress(lambda: self.paddle_down(self.paddle_a), "s")
        self.wn.onkeypress(lambda: self.paddle_up(self.paddle_b), "Up")
        self.wn.onkeypress(lambda: self.paddle_down(self.paddle_b), "Down")

    def paddle_up(self, paddle):
        y = paddle.ycor()
        y += 20
        paddle.sety(y)

    def paddle_down(self, paddle):
        y = paddle.ycor()
        y -= 20
        paddle.sety(y)

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Player A: {self.score_a}  Player B: {self.score_b}", align="center",
                              font=("Courier", 24, "normal"))

    def border_collisions(self):
        if abs(self.ball.ycor()) > 290:
            self.ball.dy *= -1

    def scoring_and_ball_reset(self):
        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score_a += 1
        elif self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            self.score_b += 1

    def paddle_and_ball_collisions(self):
        for paddle in [self.paddle_a, self.paddle_b]:
            if (paddle.xcor() - 20 < self.ball.xcor() < paddle.xcor() + 20) and (
                    paddle.ycor() + 50 > self.ball.ycor() > paddle.ycor() - 50):
                self.ball.setx(paddle.xcor() - 20) if self.ball.dx > 0 else self.ball.setx(paddle.xcor() + 20)
                self.ball.dx *= -1

    def run_game(self):
        while True:
            self.wn.update()

            # Move the ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Check for collisions
            self.border_collisions()
            self.scoring_and_ball_reset()
            self.update_scoreboard()
            self.paddle_and_ball_collisions()


if __name__ == "__main__":
    game = PongGame()
    game.run_game()
