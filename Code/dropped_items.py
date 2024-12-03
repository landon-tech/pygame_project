import pygame
from os.path import join
from surfaces import create_default_surface
from spritesheet import Sprite_Sheet


# DroppedItems for visualization in window
class Dropped_Item(pygame.sprite.Sprite):
    def __init__(self, pos, item, spritesheets ,groups):
        super().__init__(groups)
        # Stores the item data
        self.item = item

        # Visuals
        self.original_image = self.create_item(spritesheets)
        if self.original_image is None:
            self.original_image = create_default_surface(32, 32, self.item["color"])
        self.image = self.original_image    
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        # Custom behavior (if any) when the dropped item is on the ground
        pass

    def create_item(self, spritesheets):
        # Get the sprite sheet based on the category
        sheet = spritesheets.get(self.item["category"])
        if sheet:
            # Create a Sprite_Sheet object to handle frame extraction
            sprite_sheet = Sprite_Sheet(sheet)
            # Get the image for the item using the frame index (e.g., random or predefined)
            return sprite_sheet.get_image(self.item["frame_index"])
        else:
            # Return default image if the frame is empty or out of range
            return create_default_surface() 

   