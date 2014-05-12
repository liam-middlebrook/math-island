#!/usr/bin/python
import pygame
import Player
from level import Level
from gi.repository import Gtk


class MathIsland:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        print 'Initializing MathIsland'
        self.clock = pygame.time.Clock()

        self.tile_size = 64
        self.board_x = 0
        self.board_y = 0

        self.paused = False
        self.direction = 1
        
        self.player = Player.Player()

        self.font_obj = pygame.font.Font('content/fonts/DroidSans.ttf', 32)

        self.load_map(1)

    def load_map(self, mapNum):
        self.LevelID = mapNum
        self.level = Level('content/levels/00' + str(mapNum) + '.ilv')
        print "Loading levels/001.ilv"
        board_width = self.level.width
        board_height = self.level.height
        print "board_width: " + str(board_width)
        print "board_height: " + str(board_height)

        self.board = []
        for x in range(board_width):
            self.board.append([])
            for y in range(board_height):
                if self.level[x,y].image == None:
                    print '[' + str(y) + ',' + str(x) + ']: Nonetype'
                    self.board[x].append(pygame.image.load("content/tiles/grass.png"))
                else:
                    print '[' + str(y) + ',' + str(x) + ']: ' + self.level[x,y].image
                    self.board[x].append(pygame.image.load(self.level[x,y].image))
                    
        self.player.rect.x = self.level.start.x * 64
        self.player.rect.y = self.level.start.y * 64
        self.player.fuel = self.level.startfuel

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

        image = pygame.image.load("content/tiles/grass.png").convert()

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                self.player.update(event, self)
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.direction = -1
                    elif event.key == pygame.K_RIGHT:
                        self.direction = 1

            # Clear Display
            screen.fill((255, 255, 255))  # 255 for white
            
            # Draw the game board
            for x in range(len(self.board)):
                for y in range(len(self.board[0])):
                    screen.blit(self.board[x][y], 
                            (self.board_x + self.tile_size * x,
                             self.board_y + self.tile_size * y))

            #TODO: draw the fuel, other special objects

            # Draw text and stats and stuff
            fuel_text_obj = self.font_obj.render(
                    'Fuel: ' + str(self.player.fuel), 
                    False, 
                    pygame.Color(0,0,0) )
            fuel_text_rect = fuel_text_obj.get_rect()
            fuel_text_rect.topleft = (self.level.width * 64, 10)
            screen.blit(fuel_text_obj, fuel_text_rect)

            #draw the player
            self.player.draw(screen)

            # Flip Display
            pygame.display.flip()

            pygame.display.update()

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
