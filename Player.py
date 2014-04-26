#Player Class
import pygame


class Player:
    def __init__(self):
        self.x = 128
        self.y = 128
        self.speed = 64
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 64, 64))
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.KP_LEFT:
                self.x -= self.speed
            elif event.key == pygame.K_RIGHT or event.key == pygam.KP_RIGHT:
                self.x += self.speed
            if event.key == pygame.K_UP or event.key == pygame.KP_UP:
                self.y -= self.speed
            elif event.key == pygame.K_DOWN or event.key == pygame.KP_DOWN:
                self.y += self.speed
