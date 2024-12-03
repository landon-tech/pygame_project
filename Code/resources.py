import pygame
from dropped_items import Dropped_Item
from spritesheet import Sprite_Sheet
from surfaces import create_default_surface
from random import randint
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

class Resource(pygame.sprite.Sprite):
  def __init__(self, pos, resource_data, spritesheets,  item_json ,groups):
        super().__init__(groups)
        self.resource = resource_data
        self.name = self.resource["name"]
        self.health = self.resource["health"]
        self.drops = self.resource["drops"]  # This is now a list of multiple items
        self.required_tool = self.resource["required_tool"]
        self.frame_index = self.resource["frame_index"]
        self.item_json = item_json
        
        
        # Load sprite image based on the index
        self.original_image = self.create_resource(spritesheets)
        if self.original_image is None:
          self.original_image = create_default_surface(64, 64)  
        self.image = self.original_image
        self.rect = self.image.get_frect(topleft=pos)
    
  def take_damage(self, tool):
      if self.required_tool == "any" or self.required_tool == tool:
          self.health -= 1
          if self.health <= 0:
              self.destroy()
  
  def destroy(self):
      for drop in self.drops:  # Loop through each item in the drops list
          self.spawn_drop(drop)
      self.kill()

  def spawn_drop(self, drop):
      item_name, quantity = drop["item"], drop["quantity"]
      for category, items in self.item_json.items():
        if item_name in items:
          item_data = items[item_name]
          for _ in range(randint(0,quantity)):
            Dropped_Item(self.rect.center, item_data)
          return  
  def create_resource(self, spritesheets):
    sheet = spritesheets.get("resources")
    if sheet:
      # Create a Sprite_Sheet object to handle frame extraction
      sprite_sheet = Sprite_Sheet(sheet, 64, 96)
      # Get the image for the item using the frame index (e.g., random or predefined)
      return sprite_sheet.get_image(self.resource["frame_index"])      
    else:
    # Return default image if the frame is empty or out of range
      return create_default_surface(64, 96)