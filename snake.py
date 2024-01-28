import random
import time
import turtle

player_score = 0
highest_score = 0
delay_time = 0.1

# Window screen created
wind = turtle.Screen()
wind.title("Snake Maze🐍")
wind.bgcolor("red")
wind.setup(width=600, height=600)

# Creating the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Creating the food
snake_food = turtle.Turtle()
shapes = random.choice(['triangle', 'circle'])
snake_food.shape(shapes)
snake_food.color("blue")
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your_score: 0 Highest_Score : 0", align="center", font=("Arial", 24, "normal"))


# Assigning directions
def move_left():
    if snake.direction != "right":
        snake.direction = "left"


def move_right():
    if snake.direction != "left":
        snake.direction = "right"


def move_up():
    if snake.direction != "down":
        snake.direction = "up"


def move_down():
    if snake.direction != "up":
        snake.direction = "down"


def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)

    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)

    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)

    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)


# Keyboard bindings
wind.listen()
wind.onkeypress(move_left, 'Left')
wind.onkeypress(move_right, 'Right')
wind.onkeypress(move_up, 'Up')
wind.onkeypress(move_down, 'Down')

segments = []


# Main game loop
def game_loop():
    wind.update()

    if snake.distance(snake_food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snake_food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        global player_score, highest_score, delay_time
        player_score += 5
        if player_score > highest_score:
            highest_score = player_score
        pen.clear()
        pen.write("Player's_score: {} Highest_score: {}".format(player_score, highest_score), align="center",
                  font=("Arial", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the snake is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with walls
    if (abs(snake.xcor()) > 290) or (abs(snake.ycor()) > 290):
        reset_game()

    # Check for collision with itself
    for segment in segments:
        if segment.distance(snake) < 20:
            reset_game()

    wind.ontimer(game_loop, int(delay_time * 1000))


def reset_game():
    time.sleep(1)
    snake.goto(0, 0)
    snake.direction = "stop"
    snake.color('black')
    snake.shape('square')

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    global player_score, delay_time
    player_score = 0
    delay_time = 0.1

    pen.clear()
    pen.write("Player's_score: {} Highest_score: {}".format(player_score, highest_score), align="center",
              font=("Arial", 24, "normal"))


# Start the game loop
game_loop()

turtle.mainloop()
