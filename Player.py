#Player Class
import pygame


class Player:
    def __init__(self):
        self.speed = 64
        self.texture = pygame.image.load("player.png")
        self.rect = pygame.Rect(128, 128, 64, 64)
    def draw(self, surface):
        surface.blit(self.texture, self.rect)
    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                self.rect.x -= self.speed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                self.rect.x += self.speed
            if event.key == pygame.K_UP or event.key == pygame.K_KP8:
                self.rect.y -= self.speed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                self.rect.y += self.speed
