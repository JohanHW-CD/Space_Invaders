import turtle
import os
import math
import random
import winsound
import shelve

#screen setup

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Attack")
wn.bgpic("burning-city1.gif")

#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
#Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set score = 0
score = 0


#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Player Turtle
player = turtle.Turtle()
player.color("green")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


#Choose number of enemies
number_of_enemies = 7

#List of enemies
enemies = []

for i in range(number_of_enemies):
    #Create Enemy
    enemies.append(turtle.Turtle())
#Enemy Turtle

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemyspeed = 4

#Player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.setheading(90)
bullet.speed(0)
bullet.shapesize(0.5, 0.5)

bulletspeed = 20

#Definer Bullet State
#Ready - ready to fire
#Fire - bullet is firing
bulletstate = "ready"


#player movement
playerspeed = 15
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    if x > 280:
        x = 280
    x += playerspeed
    player.setx(x)

def fire_bullet():
    #Decleare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        #move bullet to just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 17:
        return True
    else:
        return False


#Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")
turtle.onkey(quit, "q")


#Main Game Loop
while True:
    for enemy in enemies:
            
        #move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
#Speed levels

        if score == 100:
            enemyspeed = 5
            score += 1

        if score == 211:
            enemyspeed = 6
            score += 1

        if score == 322:
            enemyspeed = 8
            score += 1

        if score == 333:
            enemyspeed = 5
            score +=1

        if score == 604:
            enemyspeed = 6
            score +=1

            
        #Boundary Check Enemy
        if enemy.xcor() > 280:
            #Moves all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *=-1
            
        if enemy.xcor() < -280:
            #Move all enemies down
            for e in enemies: 
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *=-1

      #Check for collision
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(1000, -400)
            #reset enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x,y)
            #Update Score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


    #Adding enemies
            
    if len(enemies) == 7 and score >= 100 and score <= 1000:
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)
    
    if len(enemies) == 8 and score >= 200 and score <= 1000:
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)

    if len(enemies) == 9 and score >= 300 and score <= 1000:
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)

    if len(enemies) == 10 and score >= 400 and score <= 1000:
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)


 #Final Boss

    if len(enemies) == 11 and score >= 500 and score <= 1000:
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)
        enemies.append(turtle.Turtle())
        enemies[-1].penup()
        enemies[-1].color("red")
        enemies[-1].shape("invader.gif")
        enemies[-1].speed(0)
    
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("gameover")
        print("Score: %s") %score
        break 
            
    #move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if bullet has reached the top
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate = "ready"

  




