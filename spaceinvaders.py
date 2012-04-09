#!/usr/bin/env python

import pygame
from pygame import *

class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("space.png", -1)
        self.dx = -5
        self.reset()
        
    def update(self):
        self.rect.left += self.dx
        if self.rect.right <= 800:
            self.reset() 
    
    def reset(self):
        self.rect.right = 1600

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('ship.gif', -1)
        self.x_dist = 5
        self.y_dist = 5
        self.lasertimer = 0
        self.lasermax = 5
        self.rect.centery = 400
        self.rect.centerx = 50
        
    def update(self):
        key = pygame.key.get_pressed()
        
        # Movement
        if key[K_UP]:
            self.rect.centery += -3
        if key[K_DOWN]:
            self.rect.centery += 3
        if key[K_RIGHT]:
            self.rect.centerx += 3
        if key[K_LEFT]:
            self.rect.centerx += -3
        
        # Lasers
        if key[K_SPACE]:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))
                self.lasertimer = 0
       
        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 600)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, 800)
        self.rect.left = max(self.rect.left, 0)
                                                     
class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("laser.png", -1)
        self.rect.center = pos
    
    def update(self):
        if self.rect.right > 800:
            self.kill()
        else:
            self.rect.move_ip(15, 0)
            

class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("alien.png", -1)
        self.rect = self.image.get_rect()
        self.dy = 8
        self.reset()
        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > 600:
            self.reset()
        
        # Laser Collisions    
        if pygame.sprite.groupcollide(enemySprites, laserSprites, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           
        # Ship Collisions
        if pygame.sprite.groupcollide(enemySprites, playerSprite, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explosionSprites.add(PlayerExplosion(self.rect.center))
           
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, 600)
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)
                                                           
class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("enemyexplosion.png", -1)
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10
        
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            
class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("enemyexplosion.png", -1)
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10
        
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            exit()
                                                                                                              
def main():    
# Initialize Everything

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('Space Quest')

    pygame.mouse.set_visible(0)



# Create The Backgound

    background = pygame.Surface(screen.get_size())

    background = background.convert()

    background.fill((000, 000, 000))



# Display The Background

    screen.blit(background, (0, 0))

    pygame.display.flip()
        
# Start Music   
    music = pygame.mixer.music.load ("data/spacequest.mp3")
    pygame.mixer.music.play(-1)



# Initialize Game Objects
    global clock

    clock = pygame.time.Clock()
    space = Space()
    global player

    player = Player()


# Render Objects
    # Space
    space = pygame.sprite.RenderPlain((space))
    
    # Player
    global playerSprite   
    playerSprite = pygame.sprite.RenderPlain((player))
    
    # Enemy
    global enemySprites
    enemySprites = pygame.sprite.RenderPlain(())
    enemySprites.add(Enemy(200))
    enemySprites.add(Enemy(300))
    enemySprites.add(Enemy(400))    

    # Projectiles    
    global laserSprites
    laserSprites = pygame.sprite.RenderPlain(())   
    
    # Collisions   
    global enemyExplosion
    enemyExplosion = pygame.sprite.RenderPlain(())
    global playerExplosion
    playerExplosion = pygame.sprite.RenderPlain(())
    global explosionSprites
    explosionSprites = pygame.sprite.RenderPlain(())
            

# Main Loop

    going = True

    while going:

        clock.tick(60)



        # Input Events

        for event in pygame.event.get():

            if event.type == QUIT:

                going = False

            elif event.type == KEYDOWN and event.key == K_ESCAPE:

                going = False

        # Update
        space.update()
        player.update()
        enemySprites.update()
        laserSprites.update()
        enemyExplosion.update()
        playerExplosion.update()
        explosionSprites.update()



        screen.blit(background, (0, 0))


        # Draw
        space.draw(screen)   
        playerSprite.draw(screen)
        enemySprites.draw(screen)
        laserSprites.draw(screen)
        enemyExplosion.draw(screen)
        playerExplosion.draw(screen)
        explosionSprites.draw(screen)
        

        pygame.display.flip()



    pygame.quit()



if __name__ == '__main__':

    main()
