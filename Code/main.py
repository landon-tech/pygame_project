import pygame
from os.path import join
from player import Player
from enemy import Enemy
from projectile import Projectile
from resources import Resource
from collision import collisions
from text import display
from utilility import load_spritesheets
from random import randint, choice
from settings import *
from groups import *
import json

data_path = 'Data'
# Load the item data once at the start
with open(join(data_path,'items.json'), 'r') as file: 
    item_json = json.load(file)
with open(join(data_path, 'resources.json'), 'r') as file:
  resource_json = json.load(file)
# Game Set up
pygame.init()

item_sprite_sheets = load_spritesheets(ITEM_SPRITE_SHEET_FOLDER)
resource_sprite_sheet=load_spritesheets(RESOURCE_SPRITE_SHEET_FOLDER)
item_sprite_sheets.update(resource_sprite_sheet)
sprite_sheets = item_sprite_sheets
print("Sprite Sheet",sprite_sheets)
pygame.display.set_caption("Test")
clock = pygame.time.Clock()
running = True

player = Player( (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)),(all_sprites, player_sprites))

# Custom Events
enemy_event = pygame.event.custom_type()
resource_event = pygame.event.custom_type()
# Timers
pygame.time.set_timer(enemy_event, 2500)
pygame.time.set_timer(resource_event, 5000)

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
    if event.type == resource_event and len(resources_sprites)<= 10:
      pos = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
      resource_name = choice(list(resource_json.keys()))
      resource_data = resource_json[resource_name]
      print(resource_name)
      Resource(pos, resource_data, sprite_sheets, item_json,(all_sprites, resources_sprites))
    
  # Updated
  all_sprites.update(dt)
  collisions(player)
  
  # Draw
  screen.fill((100,100,100))
  all_sprites.draw(screen)
  # Text Display
  display(player)

  pygame.display.update()

pygame.quit()
print(player.inventory)