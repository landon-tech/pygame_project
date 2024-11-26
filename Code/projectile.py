import pygame
from math import *
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


class Projectile(pygame.sprite.Sprite):
  def __init__(self, pos, angle ,groups) -> None:
    super().__init__(groups)
    self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  
    pygame.draw.circle(self.image, (240, 240, 240), (5, 5), 5)
    self.rect = self.image.get_frect(center= pos)
    pygame.draw.circle(self.image,(240, 240, 240),self.rect.center, self.rect.width/2)
    self.direction = pygame.math.Vector2(cos(radians(angle)), sin(radians(angle)))
    self.speed = 1000

  def update(self, dt, key, keys) -> None:
    self.rect.center += self.direction * self.speed * dt
    if self.rect.left >= WINDOW_WIDTH or self.rect.right <= 0 or self.rect.top >= WINDOW_HEIGHT or self.rect.bottom <= 0:
      self.kill()
   