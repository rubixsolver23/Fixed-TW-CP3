import pygame
from pygame.locals import *
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
    def __init__(self):
        pass

    def create_empty_level(self, id, dimensions):
        level_list = []
        for i in range(dimensions[0]):
            level_list.append("B")
        for j in range(dimensions[1]-2):
            level_list.append(" ")
        for k in range(dimensions[0]):
            level_list.append("B")


        return Level()

class Level:
    def __init__(self, id, level_dict, block_size):
        self.id = id
        self.level_dict = level_dict
        self.block_object_list = []
        self.block_size = block_size

        self.create_block_objects()

    def create_block_objects(self):
        width = self.level_dict["width"]
        for idx, block in enumerate(self.level_dict["blocklist"]):
            if block == "B":
                block_color = (0,0,0)
                block_hitbox = pygame.Rect(0, 0, self.block_size, self.block_size)
                self.block_object_list.append(RegBlock(idx%width, idx//width, block_color, block_hitbox, self.block_size))



class LevelEditor:
    pass


class Block:
    def __init__(self, x, y, color, hitbox, blocksize):
        self.x = x
        self.y = y
        self.color = color
        self.hitbox = hitbox
        self.blocksize = blocksize

    def render(self, camera_pos):
        self.hitbox.centerx = self.x*self.blocksize - camera_pos[0]
        self.hitbox.centery = self.y*self.blocksize - camera_pos[1]
        pygame.draw.rect(windowSurface, self.color, self.hitbox)

class PlayerBlock(Block):
    pass

class RegBlock(Block):
    def __init__(self, x, y, color, hitbox, blocksize):
        super().__init__(x, y, color, hitbox, blocksize)

class LaserBlock(Block):
    pass

class BounceBlock(Block):
    pass

class WaterBlock(Block):
    pass

class ExitBlock(Block):
    pass

class Camera():
    pass

def main():

    level1 = Level(1, {
        "width": 3,
        "height": 3,
        "blocklist": [
            "B", " ", "B",
            " ", "B", " ",
            "B", " ", "B"
        ]
    }, 30)
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

        windowSurface.fill((255,255,255))
        for block in level1.block_object_list:
            block.render([0, 0])

        # LAST
        pygame.display.update()
        mainClock.tick(60)
        

main()
