import pygame
from math import *
from random import randint
from groups import *
from utilility import crafting_recipes, get_craftable_items


class Player(pygame.sprite.Sprite):
  def __init__(self, pos, groups) -> None:
    super().__init__(groups)
    self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.polygon(self.original_image, "red", [(25, 0), (0, 50), (50, 50)])
    self.image = self.original_image
    self.rect = self.image.get_frect(center = pos)
    self.mask = pygame.mask.from_surface(self.image)
    self.direction = pygame.math.Vector2(0,0)
    self.speed = 300
    self.health = 1000
    self.firing = False
    self.ammo = 0
    self.rotation= 0
    self.inventory = {}
    self.crafted_items = []
    self.available_machines = []
      
  def craft_item(self, item_name):
        recipe = crafting_recipes[item_name]
        required_machine = recipe.get("machine_required")
        # Check if the required machine is available
        if required_machine and required_machine not in self.available_machines:
           print(f"You need a {required_machine} to craft {item_name}")
           return False
        
        # Check if the player can craft the item
        for ingredient, required_amount in recipe["ingredients"].items():
            if self.inventory.get(ingredient, 0) < required_amount:
                print("Not enough materials!")
                return False

        # Deduct materials
        for ingredient, required_amount in recipe["ingredients"].items():
            self.inventory[ingredient] -= required_amount

        # Add the crafted item to the player's inventory or crafted list
        crafted_item = recipe["output"]["item"]
        self.crafted_items.append(crafted_item)
        if required_machine:
          print(f"Crafted {crafted_item} using {required_machine}!")
        else:
           print(f"Crafted {crafted_item}!") #prints when you did not use a machine
        return True

  def update(self, dt) -> None:
    # Crafting
    craftable_items = get_craftable_items(self.inventory, crafting_recipes, self.available_machines)

    # Rotation might remove later
    mouse_pos = pygame.mouse.get_pos()
    x_dist = (mouse_pos[0]-self.rect.centerx)
    y_dist = (mouse_pos[1]-self.rect.centery)
    self.rotation= degrees(atan2(y_dist, x_dist)) + 90
    self.image= pygame.transform.rotozoom(self.original_image, -self.rotation, 1)
    self.rect = self.image.get_frect(center = self.rect.center)
    
    #Movement
    keys = pygame.key.get_pressed()
    recent_keys = pygame.key.get_just_pressed()
    self.direction.x = int(keys[pygame.K_d]- keys[pygame.K_a])
    self.direction.y = int(keys[pygame.K_s]- keys[pygame.K_w])
    if self.direction.length() > 0:
      self.direction = self.direction.normalize() 
    self.rect.center += self.direction * self.speed * dt
    
    