import pygame, sys, math, random, time
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Glidey Fowl")

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
SKY = (0, 150, 200)

windowSurface.fill(SKY)

bird_size = 50
pipe_thickness = 60

class Fowl:
    def __init__(self, sprite, hitbox, gravity, boinginess):
        self.sprite = sprite
        self.hitbox = hitbox
        self.gravity = gravity
        self.boinginess = boinginess
        self.jumpButtons = []
        self.spawn = (175, 275)
        self.velocity = [0, 0]
    
    def fall(self):
        self.velocity[1] -= self.gravity

    def update_pos(self):
        self.hitbox.centerx += self.velocity[0]
        self.hitbox.centery -= self.velocity[1]

    def boing(self):
        self.velocity[1] = self.boinginess

def main():
    player = Fowl(None, pygame.Rect(175, 275, bird_size, bird_size), 0.4, 10)
    player.jumpButtons = [K_UP, K_SPACE, K_w]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in player.jumpButtons:
                    player.boing()


        player.fall()
        player.update_pos()

        
        windowSurface.fill(SKY)
        pygame.draw.rect(windowSurface, YELLOW, player.hitbox)

        # ALWAYS AT THE END

        pygame.display.update()
        mainClock.tick(60)

time.sleep(1)
main()