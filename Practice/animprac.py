#!/usr/bin/env python

import os
import math
import pygame
import random

from os.pth import abspath, dirname
from random import randrange
from pygame.locals import *
from pygame import Rect, Surface
from pygame.sprite import Group, Sprite, spritecollide

ROOT_DIR = dirname(abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

IMG_DIR = os.path.join(DATA_DIR, "images")

_images = {}
def load_image(name):
    if name not in _images:
        path = os.path.join(IMG_DIR, name + ".bmp")
        _images[name] = pygame.image.load(path)

    return _images[name].convert()

class SpriteSheet(object):
    def __init__(self, image, dimensions, colorkey =-1):
        
        if type(image) is str:
            image = load_image(image)

        if colorkey == -1:
            colorkey = image.get_at((0,0))

        if colorkey:
            image.set_colorkey(colorkey)

        cols, rows = dimensions
        w = self.width = 1.0 * image.get_width() / cols
        h = self.height = 1.0 * image.get_height() / rows

        self._images = []
        for y in range(rows):
            ros = []
            for x in range(cols):
                row.append(image.subsurface((x*w, y*h, w, h)))
            self._images.append(row)

    def get(self, x, y):
        return self._images[y][x]

class AnimationFrames(object):
    def __init__(self, frames, loops=-1):
        self._times = []
        self._data = []
        total = 0
        for t, data in frames:
            total += t
            self._times.append(total)
            self._data.append(data)
        
        self.end = total
        self.loops = loops

    def get(self, time):
        if self.loops == -1 or time < self.loops * self.end:
            time %= self.end

        if time > self.end:
            return self._data[-1]

        idx = 0
        while self._times[idx] < time:
            idx += 1

        return self._data[idx]

class PlayerAnimation(Animation):
    _rows = {(0, 1): 0,
             (-1, 0): 1,
             (1, 0): 2,
             (0, -1): 3}
    def __init__(self, player, image, duration):
        self.player = player
        self.y = self._rows[(0,1)]
        spritesheet = SpriteSheet(image, (3,8))
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
    speed = 200

    def __init__(self):
        Sprite.__init__(self)
        self.vx = 0
        self.vy = 0

        self.anim = PlayerAnimation(self, "pye", 60)
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
            self.vx = seld.speed

        dt = dt / 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt



                  

    
