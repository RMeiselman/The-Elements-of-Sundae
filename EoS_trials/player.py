#!/usr/bin/env python

import math
import pygame

from pygame.locals import *
from pygame import Surface
from pygame.sprite import Sprite
from spritesheet import SpriteSheet
from anim import Animation


class PlayerAnimation(Animation):
    _rows = {(0,1): 0,
             (0, -1): 1,
             (-1, 0): 2,
             (1, 0): 3}
    def __init__(self, player, image, duration):
        self.player = player
        self.y = self._rows[(0,1)]
        spritesheet = SpriteSheet(image, (3,4))
        frames = [ (duration, 0),
                   (duration, 1),
                   (duration, 2),
                   (duration, 1) ]
        Animation.__init__(self, spritesheet, frames)

    def update(self, dt):
        vx, vy = self.player.vx, self.player.vy
        try: vx /= abs(vx)
        except: vx = 0

        try: vy /= abs(vy)
        except: vy = 0

        if vx == 0 and vy == 0:
            self.time = 0
            self.x = 1

        else:
            self.time += dt
            self.x = self.get_frame_data(self.time)
            self.y = self._rows[(vx, vy)]

class Player(Sprite):
    speed = 400

    def __init__(self):
        Sprite.__init__(self)
        self.vx = 0
        self.vy = 0

        self.anim = PlayerAnimation(self, "pye", 40)
        self.image = self.anim.get_current_frame()
        self.rect = self.image.get_rect()

    def update(self, dt):
        self.anim.update(dt)
        self.image = self.anim.get_current_frame()
        self.vx, self.vy = 0,0
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.vy = -self.speed
        if keys[K_DOWN]:
            self.vy = self.speed
        if keys[K_LEFT]:
            self.vx = -self.speed
        if keys[K_RIGHT]:
            self.vx = self.speed

        dt = dt / 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt



                  

    
