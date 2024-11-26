from pygame import image, Surface, SRCALPHA
from os.path import join

def create_surface_png(folder: str, png: str):
  try:
    return image.load(join(folder, png +".png")).convert_alpha() 
  except FileNotFoundError:
    print(f"No route found with {join(folder, png + '.png' )}. A plain surface has been created instead.")
    return None