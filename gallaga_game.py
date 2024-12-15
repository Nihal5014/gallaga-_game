import pgzrun 
import random 
HEIGHT = 600
WIDTH = 800
TITLE = "Gallaga Game"
score = 0
ship = Actor("ship image")
bullet = Actor("bullet image") 
bug = Actor("bug image")
ship.pos = (300,540)
bug.pos =(random.randint(50,750),0)
bullets = []
def draw():
    screen.fill("dark blue")
    
    if score > 200:
        screen.draw.text("You won"+ str(score), (400,500))
    else:
        ship.draw()
        bug.draw()
        screen.draw.text("score"+ str(score),(15,15))
        for bullet in bullets:
            bullet.draw() 
def update():
    global score
    if keyboard.left:
        ship.x = ship.x-5
    if keyboard.right:
        ship.x = ship.x+5

    bug.y +=5
    if bug.y >600:
        bug.pos = (random.randint(50,750),0)

    if bug.colliderect(ship):
        score = score - 300
        bug.pos = (random.randint(50,750),0)
    for bullet in bullets:
        bullet.y = bullet.y-30

        if bullet.colliderect(bug):
            score = score + 30
            bug.pos = (random.randint(50,750),0)
            bullets.remove(bullet)

        
def on_key_down(key):
    if key  == keys.SPACE:
        bullet = Actor('bullet image')
        bullet.pos = ship.pos
        bullets.append(bullet)
pgzrun.go()