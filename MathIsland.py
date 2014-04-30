#!/usr/bin/python
import pygame
from gi.repository import Gtk


class MathIsland:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.tile_size = 64
        self.board_x = 0
        self.board_y = 0

        self.paused = False
        self.direction = 1

    def load_map(self):
        self.level = Level('levels/001.ilv')
        board_width = self.level.width
        board_height = self.level.height

        self.board = []
        for i in range(board_width):
            self.board.append([])
            for j in range(board_height):
                self.board.append(pygame.image.load(self.level[i,j].image))

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1
            
            # Draw the game board
            for x in range(len(self.board)):
                for y in range(len(self.board[0])):
                    screen.blit(self.board[x][y], 
                            (self.board_x + self.tile_size * x,
                             self.board_y * self.tile_size * y))

            #TODO: draw the fuel, other special objects

            #TODO: draw the player

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white

            # Draw the ball
            pygame.draw.circle(screen, (255, 0, 0), (screen.get_width() / 2, screen.get_height() / 2), 100)

            # Flip Display
            pygame.display.flip()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./TestGame.py
def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = MathIsland()
    game.run()

if __name__ == '__main__':
    main()
