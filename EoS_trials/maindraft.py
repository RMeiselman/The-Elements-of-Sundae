#!/usr/bin/env python

import sys
import pygame
from pygame import *
from resource import load_image
import random
from pygame.locals import K_ESCAPE

class Sprite:
    def __init__ (self, xpos, ypos, filename, colorkey=-1):
        
        if type(image) is str:
            image = load_image(image)

        if colorkey == -1:
            colorkey = image.get_at((0,0))
            
        if colorkey:
            image.set_colorkey(colorkey)

        self.x = xpos
        self.y = ypos
       
    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
        
def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 75) and (s1_x < s2_x + 75) and (s1_y > s2_y - 75) and (s1_y < s2_y + 75):
        return 1
    else:
        return 0

init()
screen = display.set_mode((900, 700))
key.set_repeat(1,1)
display.set_caption('The Elements of Sundae :)')
background = load.image("background.bmp")
FPS = 30

enemies = []

x = 0

for count in range(5):
    enemies.append(Sprite(125 * x + 50, 50, 'enemy.bmp'))
    x += 1

hero = Sprite(500, 680, 'pye.bmp')
ourmissileup = Sprite(0,680, 'bullet_up.bmp')
ourmissiledown = Sprite(0,680, 'bullet_down.bmp')
ourmissileleft = Sprite(0,680, 'bullet_left.bmp')
ourmissileright = Sprite(0,680, 'bullet_right.bmp')
door = 'cookie.bmp'

quit = 0
enemyspeed = 2

while quit == 0:
    screen.blit(backdrop, (0, 0))
    
    for count in range(len(enemies)):
        enemies[count].y += + enemyspeed
        enemies[count].render()

    if enemies[len(enemies)-1].y > 699:
        enemyspeed = -2
        for count in range(len(enemies)):
            enemies[count].x += 5

    if enemies[0].y < 10:
        enemyspeed = 2
        for count in range(len(enemies)):
            enemies[count].x += 5

    if ourmissileleft.x < 699 and ourmissileleft.x > 0:
        ourmissileleft.render()
        ourmissileleft.x -= 5

    if ourmissiledown.y < 699 and ourmissiledown.y > 0:
        ourmissiledown.render()
        ourmissiledown.y += 5

    if ourmissileup.y < 699 and ourmissileup.y > 0:
        ourmissileup.render()
        ourmissileup.y -= 5

    if ourmissileright.x < 699 and ourmissileright.x > 0:
        ourmissileright.render()
        ourmissileright.x += 5

    for count in range(0, len(enemies)):
        if Intersect(ourmissileup.x, ourmissileup.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissiledown.x, ourmissiledown.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissileleft.x, ourmissileleft.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break
        elif Intersect(ourmissileright.x, ourmissileright.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break

    if len(enemies) == 0:
        pygame.quit()
        sys.exit()

    for ourevent in event.get():
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_ESCAPE:
                quit = 1
            if ourevent.key == K_d and hero.x < 890:
                hero.x += 5
            if ourevent.key == K_a and hero.x > 10:
                hero.x -= 5
            if ourevent.key == K_s and hero.y < 690:
                hero.y += 5
            if ourevent.key == K_w and hero.y > 10:
                hero.y -= 5
            if ourevent.key == K_UP:
                ourmissileup.x = hero.x
                ourmissileup.y = hero.y
            if ourevent.key == K_DOWN:
                ourmissiledown.x = hero.x
                ourmissiledown.y = hero.y
            if ourevent.key == K_LEFT:
                ourmissileleft.x = hero.x
                ourmissileleft.y = hero.y
            if ourevent.key == K_RIGHT:
                ourmissileright.x = hero.x
                ourmissileright.y = hero.y


    hero.render()
    display.update()
    time.delay(2)
