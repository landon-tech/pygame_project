import pygame
from settings import *


def display(player):
  font = pygame.font.Font(None, 50)
  ammo_surf = font.render(f"Ammo: {player.ammo}",True, (0,0,0))
  ammo_rect = ammo_surf.get_frect(bottomright = (WINDOW_WIDTH - 20, WINDOW_HEIGHT -20) )
  health_surf = font.render(f"Health: {player.health}",True, (0,0,0))
  health_rect = ammo_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT -20) )
  screen.blit(ammo_surf, ammo_rect)
  screen.blit(health_surf, health_rect)