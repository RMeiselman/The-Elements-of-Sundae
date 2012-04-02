#!/usr/bin/env python

#import everything
import os, pygame
from pygame.locals import *

#game object class
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0


#quick function to load an image
def load_image(name):
    path = os.path.join('data', name)
    return pygame.image.load(path).convert()


#here's the full code
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    player = load_image('player.bpm')
    background = load_image('background.bmp')
    screen.blit(background, (0, 0))

    objects = []
    for x in range(1):
        o = GameObject(player, x*40, x)
        objects.append(o)

    while 1:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                return

        for o in objects:
            screen.blit(background, o.pos, o.pos)
        for o in objects:
            o.move()
            screen.blit(o.image, o.pos)

        pygame.display.update()



if __name__ == '__main__': main()
