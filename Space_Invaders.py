import turtle
import os
import math
import random
import winsound
import shelve

# Global Parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BORDER_SIZE = 300
SCORE_POSITION = (-290, 280)
PLAYER_START_POSITION = (0, -250)
PLAYER_START_HEADING = 90
NUMBER_OF_ENEMIES = 7
FONT = ("Arial", 14, "normal")

# --- Screen Setup ---
wn = turtle.Screen()
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor("black")
wn.title("Space Attack")
wn.bgpic("burning-city1.gif")
wn.tracer(0)  # Disable automatic screen updates for efficiency

# --- Import Shapes ---
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


# --- Helper Functions ---
def create_turtle(shape=None, color=None, position=(0, 0), heading=0, pen_up=True):
    """Creates and returns a turtle with specified attributes."""
    t = turtle.Turtle()
    if shape:
        t.shape(shape)
    if color:
        t.color(color)
    t.speed(0)
    t.setposition(position)
    t.setheading(heading)
    if pen_up:
        t.penup()
    return t

# --- Draw Border ---
border_pen = create_turtle(color="white", pen_up=False)
border_pen.pensize(3)
border_pen.setposition(-BORDER_SIZE, -BORDER_SIZE)
for _ in range(4):
    border_pen.forward(SCREEN_WIDTH)
    border_pen.left(90)
border_pen.hideturtle()

# --- Score Setup ---
score = 0
score_pen = create_turtle(color="white", position=SCORE_POSITION)
score_pen.write(f"Score: {score}", align="left", font=FONT)
score_pen.hideturtle()

# --- Player Setup ---
player = create_turtle(shape="player.gif", color="green", position=PLAYER_START_POSITION, heading=PLAYER_START_HEADING)

# Create and set up enemies
enemies = [
    create_turtle(shape="invader.gif", color="red", position=(random.randint(-200, 200), random.randint(100, 250)))
    for _ in range(NUMBER_OF_ENEMIES)
]

# Enemy speed
enemyspeed = 4

# Player bullet setup
bullet = create_turtle(shape="triangle", color="yellow", heading=90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

# Bullet properties
bulletspeed = 20
bulletstate = "ready"

# Player movement speed
playerspeed = 15

# --- Player Movement Functions ---
def move_left():
    x = player.xcor()
    player.setx(max(x - playerspeed, -280))

def move_right():
    x = player.xcor()
    player.setx(min(x + playerspeed, 280))

# --- Fire Bullet Function ---
def fire_bullet():
    if bulletstate == "ready":
        # Change bullet state and fire
        global bulletstate
        bulletstate = "fire"
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        # Move bullet to player's position and show it
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# --- Collision Detection ---
def isCollision(t1, t2):
    return t1.distance(t2) < 17

# --- Keyboard Bindings ---
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")
wn.onkey(quit, "q")


# --- Main Game Loop ---
while True:
    for enemy in enemies:
        # Move enemy
        enemy.setx(enemy.xcor() + enemyspeed)

        # Speed levels update (using a dictionary for conditions)
        speed_levels = {100: 5, 211: 6, 322: 8, 333: 5, 604: 6}
        if score in speed_levels:
            enemyspeed = speed_levels[score]

        # Boundary check for enemies
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            enemyspeed *= -1  # Change direction
            for e in enemies:
                e.sety(e.ycor() - 40)  # Move all enemies down

        # Check for collision with bullet
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            # Reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1000, -400)
            # Reset enemy
            enemy.setposition(random.randint(-200, 200), random.randint(100, 250))
            # Update score
            score += 10
            score_pen.clear()
            score_pen.write(f"Score: {score}", align="left", font=("Arial", 14, "normal"))

    # Add enemies based on score thresholds
    enemy_thresholds = {7: 100, 8: 200, 9: 300, 10: 400}
    for enemy_count, threshold in enemy_thresholds.items():
        if len(enemies) == enemy_count and threshold <= score <= 1000:
            enemies.append(create_turtle(shape="invader.gif", color="red"))

    # Add final boss enemies at score >= 500
    if len(enemies) == 11 and 500 <= score <= 1000:
        while len(enemies) < 15:  # Add four more enemies
            enemies.append(create_turtle(shape="invader.gif", color="red"))

    # Check for collision between player and enemy
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game over")
        print(f"Score: {score}")
        break

    # Move the bullet
    if bulletstate == "fire":
        bullet.sety(bullet.ycor() + bulletspeed)

        # Check if bullet reached the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"

    # Update the screen
    wn.update()
  




