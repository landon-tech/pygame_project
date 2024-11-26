import pygame
from projectile import Projectile
from groups import *
from settings import *
from random import randint


class weapon(pygame.sprite.Sprite):
  def __init__(self, type: str, name: str, capacity: int ,fire_rate: int, damage: int, description: str, ammo: int, groups ) -> None:
    super().__init__(groups)
    self.original_image = pygame.Surface((15, 50), pygame.SRCALPHA)
    self.image = self.original_image
    self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
    self.name = name
    self.description= description
    self.ammo = ammo
    self.capacity = capacity
    self.max_capacity = capacity
    self.fire_rate = fire_rate
    self.damage = damage
    self.direction = pygame.math.Vector2(0,0)
    self.rotation = 0

     # fire Cooldown
    self.can_shoot =True
    self.projectile_fire_time = 0
    self.cooldown_durration = 40
  def firing_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.projectile_fire_time >= self.cooldown_durration:
        self.can_shoot = True

  def reload(self):
    self.capacity = self. max_capacity


  def update(self, dt):
    mouse_buttons=pygame.mouse.get_pressed()
    if mouse_buttons[0] and self.can_shoot and self.capacity > 0:
      offset = pygame.math.Vector2(0, -30).rotate(self.rotation)
      spawn_pos = self.rect.center + offset
      Projectile(spawn_pos, self.rotation -90 , (all_sprites, projectile_sprites))
      self.capacity -= 1
      self.can_shoot = False
      self.projectile_fire_time = pygame.time.get_ticks()
    self.firing_timer()

