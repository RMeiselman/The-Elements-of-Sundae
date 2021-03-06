import os 

import pygame
from pygame import Rect, Surface
from pygame.sprite import Group, spritecollide

from resource import load_image

from player import Player


class Level(object):

    def __init__(self, size):
        self.bounds = Rect((0,0), size)
        self.bg = image.load("background.bmp")

    def background(self, surf):
        tw, th = self.bg.get_size()
        sw, sh = surf.get_size()

    def restart(self):
        self.player = Player()
        self.player.rect.center = self.bounds.center


        # start the background music
      
    def update(self, dt):
        self.player.update(dt)
     
        # lock player in bounds
        self.player.rect.clamp_ip(self.bounds)

        # collide player with coins
       # if spritecollide(self.player, self.cookies, True):
           # self.coin_sfx.stop()#
           # self.coin_sfx.play()#
        
    def draw(self, surf):
        surf.blit(self.player.image, self.player.rect)
