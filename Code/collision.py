import pygame
from groups import *

def collisions(player):
  # Test item collsion with player to tell it to add it to sprite
  for item in dropped_item_sprites:
    if pygame.sprite.collide_mask(item, player):
      item_name = item.item["name"]
      if item_name in player.inventory:
         player.inventory[item_name] += 1
      else:
         player.inventory[item_name] = 1
      print(player.inventory)
      item.kill()

  for projectile in projectile_sprites:
    enemy_collided_sprites_with_projectile = pygame.sprite.spritecollide(projectile, enemy_sprites, True)
    if enemy_collided_sprites_with_projectile:
      player.ammo += 5
      projectile.kill()
  
  # Test Enemy collision with Player
  for enemy in enemy_sprites:
    if pygame.sprite.collide_mask(enemy, player):
      enemy.speed = -200  
      player.health -= 1 
    else:
      enemy.speed = 200  