#!/usr/bin/env python

import pygame
from pygame import *
import random

class Sprite:
    def __init__ (self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 32) and (s1_x < s2_x + 32) and (s1_y > s2_y - 32) and (s1_y < s2_y + 32):
        return 1
    else:
        return 0

init()
screen = display.set_mode((640, 480))
key.set_repeat(1,1)
display.set_caption('Elements of Sundae :)')
backdrop = image.load('backdrop.bmp')
FPS = 30

enemies = []

x = 0

for count in range(1):
    enemies.append(Sprite(50 * x + 50, 50, 'Bulbasaur.jpeg'))
    x += 1
    
hero = Sprite(580,430, 'squirtle.bmp')
ourmissile = Sprite(0,480, 'icecreamsprite.gif')

quit = 0
enemyspeed = 3

while quit == 0:
    screen.blit(backdrop, (0, 0))
    
    for count in range(len(enemies)):
        enemies[count].y += + enemyspeed
        enemies[count].render()

    if enemies[len(enemies)-1].y > 479:
        enemyspeed = -3
        for count in range(len(enemies)):
            enemies[count].x += 5

    if enemies[0].y < 10:
        enemyspeed = 3
        for count in range(len(enemies)):
            enemies[count].x += 5

    if ourmissile.y < 430 and ourmissile.y > 0:
        ourmissile.render()
        ourmissile.y -= 5

    for count in range(0, len(enemies)):
        if Intersect(ourmissile.x, ourmissile.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break

    if len(enemies) == 0:
        quit = 1

    
    for ourevent in event.get():
        if ourevent.type == QUIT:
            quit = 1
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_RIGHT and hero.x < 590:
                hero.x += 5
            if ourevent.key == K_LEFT and hero.x > 10:
                hero.x -= 5
            if ourevent.key == K_UP and hero.y < 430:
                hero.y += 5
            if ourevent.key == K_DOWN and hero.y > 10:
                hero.y -= 5
            if ourevent.key == K_SPACE:
                ourmissile.x = hero.x
                ourmissile.y = hero.y


    hero.render()
    display.update()
    time.delay(5)
