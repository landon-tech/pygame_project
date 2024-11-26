import pygame
from os.path import join
from dropped_items import DroppedItem
from groups import *
from surfaces import create_surface_png
import json

with open(join("Data","crafting_recipies.json"), "r") as file:
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
          'image_path': join("Assets", "items", item.category, item.name),
          'color': item.color
      }
      DroppedItem(player.rect.center, item_data, (all_sprites, dropped_item_sprites))

def load_sprites(folder, png):
    sprite_sheet_image = create_surface_png(folder, png)