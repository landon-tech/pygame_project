import pygame
import os
from spritesheet import Sprite_Sheet
from dropped_items import Dropped_Item
from groups import *
#from surfaces import create_surface_png
import json

with open(os.path.join("Data","crafting_recipies.json"), "r") as file:
    crafting_recipes = json.load(file)

def get_craftable_items(inventory: list, recipes: str, available_machines: list):
    craftable_items = []
    for item_name, recipe in recipes.items():
        required_machine = recipe.get("machine_required")
        if required_machine not in available_machines:
            continue # Skips this item if the machine is unavailable
        can_craft = all(
            inventory.get(ingredient, 0) >= amount
            for ingredient, amount in  recipe["ingredients"].items()
        )

        if can_craft:
            craftable_items.append(item_name)
    return craftable_items

def drop_item(player, item):
      item_data = {
          'name': item.name,
          'image_path': os.path.join("Assets", "items", item.category, item.name),
          'color': item.color
      }
      Dropped_Item(player.rect.center, item_data, (all_sprites, dropped_item_sprites))

def load_spritesheets(folder_path):
    spritesheets = {}
    for filename in os.listdir(folder_path):
        try:
            if filename.endswith(".png"):  # Ensure only PNG files are loaded
                category_name = filename.split(".")[0]
                file_path = os.path.join(folder_path, filename)
                image = pygame.image.load(file_path).convert_alpha()  # Load with transparency
                spritesheets[category_name]= image
        except pygame.error as e:
            print(f"Error loading sprite sheet {filename}: {e}" )
    return spritesheets

