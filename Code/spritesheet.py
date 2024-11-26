import pygame

class Sprite_Sheet():
    def __init__(self, image):
        self.sheet = image


    def get_item_image(self, frame, width= 32, height=32):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sheet, (0,0),((frame, * width),(frame * height), width, height))


        return image