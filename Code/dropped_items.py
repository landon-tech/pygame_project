import pygame
from os.path import join
from surfaces import create_surface_png

# DroppedItems for visualization in window
class Dropped_Item(pygame.sprite.Sprite):
    def __init__(self, pos, item_data, groups):
        super().__init__(groups)
        self.data = item_data
        self.name = item_data.get("name")
        self.type = item_data.get("type")
        self.category = item_data.get("category")
        self.color = item_data.get("color", (255, 255, 255))
        self.amount = 1

        # Visuals
        self.original_image = create_surface_png(join("Assets", "items"),self.category)
        if self.original_image == None:
            self.image = self.create_default_surface()
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        # Custom behavior (if any) when the dropped item is on the ground
        pass


    def create_default_surface(self):
            surface = pygame.Surface((30, 30), pygame.SRCALPHA)  # Transparent background
            surface.fill(self.color)  # Grayish fill to indicate a missing item
            pygame.draw.line(surface, (255, 0, 0), (0, 0), (30, 30), 7)  # Red "X" pattern
            pygame.draw.line(surface, (255, 0, 0), (30, 0), (0, 30), 7)
            return surface