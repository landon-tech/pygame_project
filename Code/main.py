import pygame
from os.path import join
from player import Player
from enemy import Enemy
from item import Item
from projectile import Projectile
from collision import collisions
from text import display
from random import randint, choice
from settings import *
from groups import *
import json

# Load the item data once at the start
with open(join('Data','items.json'), 'r') as file: 
    item_data = json.load(file)

# Game Set up
pygame.init()

pygame.display.set_caption("Test")
clock = pygame.time.Clock()
running = True

player = Player( (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),all_sprites)

# Custom Events
enemy_event = pygame.event.custom_type()
item_event = pygame.event.custom_type()
# Timers
pygame.time.set_timer(enemy_event, 2500)
pygame.time.set_timer(item_event, 5000)

while running:
  dt = clock.tick()/1000
  if player.health < 0:
    running = False

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == enemy_event:
      pos = choice([(randint(0, WINDOW_WIDTH), choice([0, WINDOW_HEIGHT])),(choice([0, WINDOW_WIDTH]), randint(0, WINDOW_HEIGHT))])
      #Enemy(pos, player ,(all_sprites, enemy_sprites)) 
    if event.type == item_event and len(item_sprites)== 0:
      pos = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
      category = choice(list(item_data.keys()))
      item_name = choice(list(item_data[category]))
      item_info = item_data[category][item_name]
      print(category, item_name)
      Item(pos,category, item_name, item_info, (all_sprites,item_sprites))
    
  # Updated
  all_sprites.update(dt)
  collisions(player)
  
  # Draw
  screen.fill((100,100,100))
  all_sprites.draw(screen)
  display(player)

  pygame.display.update()

pygame.quit()
print(player.inventory)