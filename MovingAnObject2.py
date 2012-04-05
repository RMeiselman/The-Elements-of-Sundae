#!/usr/bin/env python
import pygame
import sys

class Squirtle(pygame.sprite.Sprite):
   def __init__(self, position):
      pygame.sprite.Sprite.__init__(self)
      # Save a copy of the screen's rectangle
      self.screen = pygame.display.get_surface().get_rect()
      # Create a variable to store the previous position of the sprite
      self.old = (0, 0, 0, 0)
      self.image = pygame.image.load('squirtle.jpeg').convert()
      self.rect = self.image.get_rect()
      self.rect.x = position[0]
      self.rect.y = position[1]

   def update(self, amount):
      # Make a copy of the current rectangle for use in erasing
      self.old = self.rect
      # Move the rectangle by the specified amount
      self.rect = self.rect.move(amount)
      # Check to see if we are off the screen
      if self.rect.x < 0:
         self.rect.x = 0
      elif self.rect.x > (self.screen.width - self.rect.width):
         self.rect.x = self.screen.width - self.rect.width
      if self.rect.y < 0:
         self.rect.y = 0
      elif self.rect.y > (self.screen.height - self.rect.height):
         self.rect.y = self.screen.height - self.rect.height

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("Bulbasaur.jpeg", -1)
        screen = pygame.display.get_surface
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9

    def update(self):
        self._walk()

    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or \
		self.rect.right > self.area.right:
                    self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos
        
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Elements of Sundae Vertical Slice #1')
screen.fill((159, 182, 205))

character = Squirtle((screen.get_rect().x, screen.get_rect().y))
screen.blit(character.image, character.rect)

# Create a Surface the size of our character
blank = pygame.Surface((character.rect.width, character.rect.height))
blank.fill((159, 182, 205))

pygame.display.update()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()

      # Check for movement
      elif event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
            character.update([-30, 0])
         elif event.key == pygame.K_UP:
            character.update([0, -30])
         elif event.key == pygame.K_RIGHT:
            character.update([30, 0])
         elif event.key == pygame.K_DOWN:
            character.update([0, 30])

      # Erase the old position by putting our blank Surface on it
      screen.blit(blank, character.old)

      # Draw the new position
      screen.blit(character.image, character.rect)

      # Update ONLY the modified areas of the screen
      pygame.display.update([character.old, character.rect])
