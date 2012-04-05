#!/usr/bin/env python

try:
    import sys, math, os, random
    import pygame
    from pygame.locals import *

except ImportError, err:
    print "%s Failed to load module: %s" % (__file__, err)
    sys.exit(1)

class Squirtle(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("squirtle.jpeg")
        self.rect = self.image.get_rect()
        
        self.rect.centerx, self.rect.centery = xy
        
        self.movementspeed = 5
        
        self.velocity = 0

    def up(self):
        self.velocity -= self.movementspeed

    def down(self):
        self.velocity += self.movementspeed

    def move(self, dy):
        if self.rect.bottom + dy > 400:
            self.rect.bottom = 400
        elif self.rect.top + dy < 0:
            self.rect.top = 0
        else:
            self.rect.y += dy

    def update(self):
        self.move(self.velocity)

class Game(object):

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((800, 400))

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Elements of Sundae - Vertical Slice #1")

        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        self.background = pygame.Surface((800,400))
        self.background.fill((255,255,255))

        self.sprites = pygame.sprite.RenderUpdates()

        # creats squirtle, and adds to sprite group
        self.squirtle = Squirtle((50,200))
        self.sprites.add(self.squirtle)

    def run(self):
        print 'Starting Event Loop'

        running = True

        while running:

            self.clock.tick(60)

            running = self.handleEvents()

            for sprite in self.sprites:
                sprite.update

            self.sprites.clear(self.window, self.background)
            dirty = self.sprites.draw(self.window)

            pygame.display.update(dirty)

        print 'Quitting. Thanks for playing!'

    def handleEvents(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    done = True

                if event.key == K_UP:
                    self.squirtle.up(0, 6)

                if event.key == K_DOWN:                ##### add in left and right if this works
                    self.squirtle.down()
        return True

if __name__ == '__main__':
    game = Game()
    game.run()

