import pygame

class Sprite_Sheet():
    def __init__(self, image, frame_width=32, frame_height= 32):
        self.sheet = image
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.columns = self.sheet.get_width() // self.frame_width
        self.rows = self.sheet.get_height() // self.frame_height


    def get_item_image(self, frame_index):
        # Calculate total frames in the spritesheet
        total_frames = self.columns * self.rows
        # Ensure the frame index is within range
        if frame_index >= total_frames or frame_index < 0:
            return None  # Out of range
        # Calculate x and y position based on frame index
        x = (frame_index % self.columns) * self.frame_width
        y = (frame_index // self.columns) * self.frame_height
        
        # Extract the frame
        image = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, self.frame_width, self.frame_height))
        
        # Check if the frame contains any visible pixels
        if not self.has_visible_pixels(image):
            return None  # Empty frame
        return image

    def has_visible_pixels(self, image):
        # Check if there are any non-transparent pixels
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                if image.get_at((x, y))[3] > 0:  # Alpha channel > 0
                    return True
        return False