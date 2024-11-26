import pygame
from random import randint, choice
from os.path import join
from surfaces import create_surface_png

# Item for data
class Item:
  def __init__(self, item_data, amount=1) -> None:
    # Data
    self.name = item_data["name"]
    self.category =  item_data["category"]
    self.color = self.data["color"]
    self.effect = self.data['effect']
    self.usage = self.data['usage']
    self.max_stack = self.data.get("max_stack", 99) # Defaults to 99 if not specidied
    self.type = self.data.get("type", "resource") # Could be 'weapon', 'tool', etc.
    self.amount = amount
    self.durability = item_data.get("durability", None)
    self.is_craftable = self.data.get("craftable", False) # Defaults to non-craftable
  
  #Shows the name of the item in the Players inventory
  def __repr__(self):
      return f"{self.name.capitalize()} (Ammount: {self.ammount})"