#!/usr/bin/env python

import sys
import pygame
from pygame import *
import math, random
from livewires import games, color
from pygame.locals import K_ESCAPE


games.init(screen_width = 900, screen_height = 700, fps = 50)

          

## Trial Wrapper##
class Wrapper(games.Sprite):
    def update(self):
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height
            
        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        self.destroy()

class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprtie.die()
            self.die()

    def die(self):
        #Destroy self and leave explosion behind#
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Enemy(Wrapper):
    
    SPEED = 2
    SPAWN = 2
    POINTS = 30

    images = games.load_image("enemy_straight_on.bmp")

    total = 0

    def __init__(self, game, x, y, size):
        Enemy.total +=1

        super(Enemy, self).__init__(
            image = Asteroid.images[size],
            x =x, y = y,
            dx = random.choice([1, -1]) * Enemy.SPEED * random.random()/size,
            
            dy = random.choice([1, -1]) * Enemy.SPEED * random.random()/size)

        self.game = game
        self.size = size

    def die(self):
        Enemy.total -= 1

        self.game.score.value += int(Enemy.POINTS)
        self.game.score.right = games.screen.width - 10

        if Enemy.total == 0:
            self.game.advance()

        super(Enemy, self).die()

class Hero(Collider):

    image = games.load_image("pye_straight_on.bmp")
    SPEED = 3
    MISSILE_DELAY = 25

    def __init__(self, game, x,y):
        super(Hero, self).__init__(image = Hero.image, x = x, y = y)
        self.game = game
        self.missile_wait = 0 
   

    def set_position(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
  
        
    def Intersect(s1_x, s1_y, s2_x, s2_y):
        if (s1_x > s2_x - 75) and (s1_x < s2_x + 75) and (s1_y > s2_y - 75) and (s1_y < s2_y + 75):
            return 1
        else:
            return 0

    def die(self):
        self.game.end()
        super(Hero, self).die()

class Missile(Collider):
    image = games.load_image("bullet_up.bmp")
    BUFFER = 40
    LIFETIME = 40
    
    def __init__(self, hero_x, hero_y):

        super(Missile, self).__init(image = Missile.image,
                                    x = x, y = y,
                                    dx = dx, dy = dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        super(Missile, self).update()

        self.lifetime -+ 1
        if self.lifeitme == 0:
            self.destroy()


## Game class Trial ##

class Game(object):
    def __init__(self):
        self.level = 0

        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)

        self.hero = Hero(game = self,
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.hero)

    def play(self):
        
        EoS_background = games.load_image("EoS_Background.bmp")
        games.screen.background = E0S_background

        self_advance()
        
        games.screen.mainloop()

    def advance(self):
        self.level += 1

        BUFFER = 150

        #create new enemies
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, gmaes.screen.height - y_min)

            x = self.hero.x + x_distance
            y = self.hero.y + y_distance
            
            #create the enemy (work on it)
            new_enemy = Enemy(game = self,
                              x = x, y = y)
            games.screen.add(new_enemy)

        #Display level number
        level_message = games.Message(value = "Level " + str(self.level),
                                      size = 40,
                                      color = color.white,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

    def end(self):
        end_message = games.Message(value = "Game Over",
                                    size = 100,
                                    color = color.black,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)

def main():
    Elements_of_Sundae = Game()
    Elements_of_Sundae.play()

main()
                       

