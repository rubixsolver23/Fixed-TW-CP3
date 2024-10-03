import pygame, sys, math, random, time
from pygame.locals import *

mainClock = pygame.time.Clock()
pygame.init()

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Glidey Fowl")

score_font = pygame.font.Font("GlideyFowl\\numeric_font.ttf", 100)

GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
SKY = (0, 150, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

windowSurface.fill(SKY)

bird_size = 50
pipe_thickness = 70
pipe_gap = 176
pipe_distance = 300
pipe_length = 500
pipe_speed = 2

class Fowl:
    def __init__(self, sprite, hitbox, gravity, boinginess):
        self.sprite = sprite
        self.hitbox = hitbox
        self.gravity = gravity
        self.boinginess = boinginess
        self.jumpButtons = []
        self.score = 0
        self.spawn = (175, 275)
        self.velocity = 0
        self.dead = False
    
    def fall(self):
        self.velocity -= self.gravity

    def update_pos(self):
        self.hitbox.centery -= self.velocity

    def boing(self):
        self.velocity = self.boinginess
    
    def check_death(self, pipes):
        self.collisions = self.hitbox.collidelist(pipes)
        if self.collisions != -1:
            return True
        
        if self.hitbox.top < 0 or self.hitbox.bottom > 600:
            return True

        
class PipeGenerator:
    def __init__(self, pipe_distance, x_pos, thickness, gap, length, speed, sprite):
        self.pipe_distance = pipe_distance
        self.thickness = thickness
        self.gap = gap
        self.length = length
        self.pipe_distance_to_center = gap/2
        self.speed = speed
        self.sprite = sprite
        self.pos = x_pos
    
    def generatePipe(self):
        return Pipe(random.randint(95, 505), self.thickness, self.gap, self.length, self.speed, self.sprite, self.pos)

class Pipe:
    def __init__(self, y_pos, thickness, gap, length, speed, sprite, x_pos):
        self.y_pos = y_pos
        self.thickness = thickness
        self.gap = gap
        self.length = length
        self.pipe_distance_to_center = gap/2
        self.speed = speed
        self.sprite = sprite
        self.scored = False
        self.top_pipe_hitbox = pygame.Rect(x_pos, -self.length+y_pos-self.pipe_distance_to_center, self.thickness, self.length)
        self.bottom_pipe_hitbox = pygame.Rect(x_pos, y_pos+self.pipe_distance_to_center, self.thickness, self.length)
    
    def move(self):
        self.top_pipe_hitbox.centerx -= self.speed
        self.bottom_pipe_hitbox.centerx -= self.speed

def main():
    pipe_timer = 0

    player = Fowl(None, pygame.Rect(175, 275, bird_size, bird_size), 0.4, 9)
    player.jumpButtons = [K_UP, K_SPACE, K_w]

    pipe_generator = PipeGenerator(pipe_distance, 650, pipe_thickness, pipe_gap, pipe_length, pipe_speed, None)
    pipes = []
    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in player.jumpButtons:
                    player.boing()
                    break


        
        windowSurface.fill(SKY)
        pygame.draw.rect(windowSurface, YELLOW, player.hitbox)


        # ALWAYS AT THE END

        pygame.display.update()
        mainClock.tick(60)
        if player.velocity != 0:
            break
        
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


        # Pipe updates
        if pipe_timer > pipe_distance/pipe_speed:
            pipe_timer = 0
            pipes.append(pipe_generator.generatePipe())

        for pipe in pipes:
            pipe.move()
            if pipe.top_pipe_hitbox.centerx < -(pipe_thickness/2):
                pipes.remove(pipe)
            elif pipe.top_pipe_hitbox.centerx < player.hitbox.centerx and not pipe.scored:
                pipe.scored = True
                player.score += 1
                print(player.score)



        pipe_hitboxes = []
        for pipe in pipes:
            pipe_hitboxes.append(pipe.top_pipe_hitbox)
            pipe_hitboxes.append(pipe.bottom_pipe_hitbox)
        # Player updates
        player.fall()
        player.update_pos()
        if player.check_death(pipe_hitboxes):
            break

        score_text = score_font.render(str(player.score), False, BLACK, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = 300
        score_rect.centery = 50

        windowSurface.fill(SKY)
        pygame.draw.rect(windowSurface, YELLOW, player.hitbox)

        for pipe in pipes:
            pygame.draw.rect(windowSurface, GREEN, pipe.top_pipe_hitbox)
            pygame.draw.rect(windowSurface, GREEN, pipe.bottom_pipe_hitbox)

        windowSurface.blit(score_text, score_rect)


        # ALWAYS AT THE END

        pipe_timer  += 1
        pygame.display.update()
        mainClock.tick(60)


    # Player death

    player.velocity = 6
    while player.hitbox.top < 600:
        player.fall()
        player.update_pos()
        windowSurface.fill(SKY)
        pygame.draw.rect(windowSurface, YELLOW, player.hitbox)

        for pipe in pipes:
            pygame.draw.rect(windowSurface, GREEN, pipe.top_pipe_hitbox)
            pygame.draw.rect(windowSurface, GREEN, pipe.bottom_pipe_hitbox)



        # ALWAYS AT THE END

        pygame.display.update()
        mainClock.tick(60)




while True:
    main()
    time.sleep(0.5)