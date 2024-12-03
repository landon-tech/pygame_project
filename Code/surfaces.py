from pygame import image, Surface, SRCALPHA, draw
from os.path import join

def create_surface_png(folder: str, png: str):
  try:
    return image.load(join(folder, png +".png")).convert_alpha() 
  except FileNotFoundError:
    print(f"No route found with {join(folder, png + '.png' )}. A plain surface has been created instead.")
    return None
  
def create_default_surface(width, height, color=(100, 100, 100)):
  # draws a red "X" pattern
  surface = Surface((width, height))  
  surface.fill(color)  # Fills the colore based on the item data color
  draw.line(surface, (255, 0, 0), (0, 0), (width, height), 7)  
  draw.line(surface, (255, 0, 0), (width, 0), (0, height), 7)
  return surface
