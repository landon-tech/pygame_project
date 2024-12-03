from pygame.display import set_mode
from os.path import join

ITEM_SPRITE_SHEET_FOLDER =  join("Assets", "items")
RESOURCE_SPRITE_SHEET_FOLDER = join("Assets", "resources")

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 780

screen = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))