#!/usr/bin/env python

background_image_filename = "background.bmp"
sprite_image_filename = 'sprite.jpeg'
import pygame
from pygame.locals import *
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
# The x coordinate of our sprite
x = 0.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 10))
    x += 1.
    # If the image goes off the end of the screen, move it back
    if x > 640.:
        x -= 640.
    pygame.display.update()
