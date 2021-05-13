import os
import random
import sys
import pygame

WIN_WIDTH = 400
WIN_HEIGHT = 533

BG_IMG = pygame.image.load(os.path.join("F:\.Faculdade\pythonGAME", "Cenario PyGame.png"))
DOODLE_IMG = pygame.image.load(os.path.join("F:\.Faculdade\pythonGAME", "DoodleEngineer.png"))
PLAT_IMG = pygame.image.load(os.path.join("F:\.Faculdade\pythonGAME", "plat.png"))


class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Doodle Engineer Jump!")

pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 30)

plates = [Plat(random.randrange(0, WIN_WIDTH), random.randrange(0, WIN_HEIGHT)) for i in range(10)]

x = 100
y = 100
dy = 0.0
h = 200
score = 0

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(BG_IMG, (0, 0))

    for plat in plates:
        win.blit(PLAT_IMG, (plat.x, plat.y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 4
        DOODLE_IMG = pygame.image.load(os.path.join("F:\.Faculdade\pythonGAME", "DoodleEngineer.png"))
    if keys[pygame.K_RIGHT]:
        x += 4
        DOODLE_IMG = pygame.transform.flip(pygame.image.load(os.path.join("F:\.Faculdade\pythonGAME", "DoodleEngineer.png")), True, False)

    if y < h:
        y = h
        for plat in plates:
            plat.y = plat.y - dy
            if plat.y > WIN_HEIGHT:
                plat.y = 0
                plat.x = random.randrange(0, WIN_WIDTH)
                score += 1
                print(score)

    dy += 0.2
    y += dy
    if y > WIN_HEIGHT:
        dy = -6

    for plat in plates:
        if (x + 50 > plat.x) and (x + 20 < plat.x + 150) and (y + 70 > plat.y) and (y + 70 < plat.y + 14) and dy > 0:
            dy = -10

    text = SCORE_FONT.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 25))

    win.blit(DOODLE_IMG, (x, y))

    pygame.display.update()