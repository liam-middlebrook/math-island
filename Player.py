#Player Class
import pygame


class Player:
    def __init__(self):
        self.speed = 64
        self.texture = pygame.image.load("player.png")
        self.rect = pygame.Rect(128, 128, 64, 64)
    def draw(self, surface):
        surface.blit(self.texture, self.rect)
    def update(self, event, level):
        self.mapRect = pygame.Rect(self.rect.x/self.speed, self.rect.y/self.speed, 0, 0)
        if event.type == pygame.KEYDOWN:
            if self.fuel > 0:
                if event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                    if level[self.mapRect.x - 1, self.mapRect.y].passable:
                        self.fuel = self.fuel - level.getcost(self.mapRect.x - 1, self.mapRect.y)
                        self.rect.x -= self.speed
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                    if level[self.mapRect.x + 1, self.mapRect.y].passable:
                        self.fuel = self.fuel - level.getcost(self.mapRect.x + 1, self.mapRect.y)
                        self.rect.x += self.speed
                if event.key == pygame.K_UP or event.key == pygame.K_KP8:
                    if level[self.mapRect.x, self.mapRect.y - 1].passable:
                        self.fuel = self.fuel - level.getcost(self.mapRect.x, self.mapRect.y - 1)
                        self.rect.y -= self.speed
                elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                    if level[self.mapRect.x, self.mapRect.y + 1].passable:
                        self.fuel = self.fuel - level.getcost(self.mapRect.x, self.mapRect.y + 1)
                        self.rect.y += self.speed
