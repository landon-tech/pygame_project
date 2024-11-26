import pygame
import math

class Enemy(pygame.sprite.Sprite):
  def __init__(self, pos, player,groups) -> None:
    super().__init__(groups)
    self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
    self.image = self.original_image
    self.image.fill((150, 255, 150))
    self.image.set_colorkey((0,0,0))
    self.rect = self.image.get_frect(center=pos)
    self.mask = pygame.mask.from_surface(self.image)
    self.direction = pygame.math.Vector2((0, 0))
    self.speed = 200
    self.following = player
    self.distance = ((player.rect.x - self.rect.x)**2 + (player.rect.y - self.rect.y)**2)**.5
    self.rotation = 0
  
  def update(self, dt) -> None:
    x_dist = (self.following.rect.x-self.rect.x)
    y_dist = (self.following.rect.y-self.rect.y)
    self.rotation= math.degrees(math.atan2(y_dist, x_dist))
    self.image= pygame.transform.rotozoom(self.original_image, -self.rotation, 1)
    self.rect = self.image.get_frect(center = self.rect.center)

    self.distance = ((self.following.rect.x - self.rect.x)**2 + (self.following.rect.y - self.rect.y)**2)**.5
    self.direction.x = (self.following.rect.x -self.rect.x)
    self.direction.y = (self.following.rect.y -self.rect.y)
    self.direction = self.direction.normalize() if self.direction else self.direction
    self.rect.center += self.direction * self.speed * dt