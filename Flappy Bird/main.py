import sys
import pygame
from pygame.locals import *
import random

pygame.init()

# ASSETS
background = pygame.image.load('./assets/background.png')
bird = pygame.image.load('./assets/bird.png')

# PILLARS
gap = 200
px = 800
pw = 80
ph1 = random.randint(50,375)
ph2 = 600-ph1+gap
py1 = 0
py2 = ph1+gap

def set_value_pillars():
    global px,ph2,pw,ph1,py1,py2,score,gap
    score += 1
    px = 980
    pw = 80
    ph1 = random.randint(50, 375)
    ph2 = 600 - ph1 + gap
    py1 = 0
    py2 = ph1 + gap


def check():
    scores = myfont.render('Score : '+str(score), False, (0, 0, 0))
    win.blit(scores, (0, 0))
    pygame.display.update()
    if bird_x+60 >= px and bird_x <= px+pw:
        if bird_y <= ph1:
            welcome()
        elif bird_y+60 >= py2:
            welcome()
    elif bird_y+60 >=600:
        welcome()
    elif bird_y <= 0:
        welcome()


def pillars():
    if px <= -80:
        set_value_pillars()
    pygame.draw.rect(win,green,(px,py1,pw,ph1))
    pygame.draw.rect(win,green,(px-10,ph1,100,30), border_radius=2)
    pygame.draw.rect(win,green,(px,py2,pw,ph2))
    pygame.draw.rect(win,green,(px-10,py2,100,30), border_radius=2)

def update():
    global score
    win.fill(white)
    win.blit(background,(0,0))
    win.blit(bird,(bird_x,bird_y))
    pillars()
    check()
    pygame.display.update()

# COLORS
green = [34, 163, 49]
white = [255,255,255]
black = [0,0,0]

# GLOBALS
score = 0
run = True
bird_x = 100
bird_y = 280
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Press SpaceBar to Play', False, (0, 0, 0))

win = pygame.display.set_mode((900,600))
pygame.display.set_caption('Flappy Bird')

update()

def welcome():
    global run, bird_y, px, bird_x,score
    score = -1
    bird_x = 100
    bird_y = 280
    win.blit(textsurface, (284, 280))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gameloop()

def gameloop():
    global run, bird_y, px
    set_value_pillars()
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    bird_y -= 60
                    update()
        bird_y += .6
        px -= 1
        update()
        global score

welcome()
pygame.quit()
sys.exit()