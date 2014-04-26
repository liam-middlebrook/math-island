#Player Class
import pygame


class Player:
    def __init__:
        self.x = 0
        self.y = 0
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 64, 64))
