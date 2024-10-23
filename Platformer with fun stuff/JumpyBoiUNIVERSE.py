import pygame
import os, sys

mainClock = pygame.time.Clock()
pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Jumpy Boi UNIVERSE")

# Make a UML diagram of all the classes
# Classes like:
'''
Block, which has children like PlayerBlock and LavaBlock
Camera, associated with PlayerBlock 
LevelEditor, which is associated with camera
Level, which has blocks in it
Particle
SoundManager
'''
class LevelManager:
    pass

class Level:
    def __init__(self, id, size, block_list):
        self.id = id
        self.size = size
        self.block_list = block_list

class LevelEditor:
    pass


class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def render(self):
        pass

class PlayerBlock(Block):
    pass

class RegBlock(Block):
    pass

class LaserBlock(Block):
    pass

class BounceBlock(Block):
    pass

class WaterBlock(Block):
    pass

class ExitBlock(Block):
    pass

def main():

    level1 = Level(1, [20, 20], {})
    while True:
        # FIRST
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        # then other stuff



        # LAST
        pygame.display.update()
        mainClock.tick(60)
        


