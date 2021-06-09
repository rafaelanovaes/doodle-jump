#Importando as bibliotecas necessárias utilizadas no código
import os
import random
import sys
import pygame

#Definindo o tamanho da tela do jogo
WIN_WIDTH = 400
WIN_HEIGHT = 533

#Carregando as imagens pro jogo
BG_IMG = pygame.image.load(os.path.join("images", "cenarioPyGame.png"))
DOODLE_IMG = pygame.image.load(os.path.join("images", "DoodleEngineer.png"))
PLAT_IMG = pygame.image.load(os.path.join("images", "Plat_4.png"))

#Definindo as plataformas em função para facilitar a repetição das mesmas
class Plat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Tela de inicio do game
def show_go_screen():
    win.blit(BG_IMG, (0, 0))
    draw_text(win, "DOODLE ENGINEER GAME!", 40, WIN_WIDTH / 2, WIN_HEIGHT / 4)
    draw_text(win, "Use as setas do teclado para se movimentar ", 22, WIN_WIDTH / 2, WIN_HEIGHT / 2)
    draw_text(win, "para a direita ou esquerda.", 22, WIN_WIDTH / 2, WIN_HEIGHT / 1.9)
    draw_text(win, "Pressione qualquer tecla para começar!", 25, WIN_WIDTH / 2, WIN_HEIGHT * 3 /4)
    pygame.display.flip()
    wainting = True
    while wainting:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                wainting = False
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#Colocando o nome do jogo no topo da tela
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Doodle Engineer Jump!")

#Definindo a letra e tamanho do placar de pontuação e tela de inicio e game over
pygame.font.init()
SCORE_FONT = pygame.font.SysFont("comicsans", 30)
font_name = pygame.font.match_font('VT323')

#Função que gera as plataformas de forma aleatória
plates = [Plat(random.randrange(0, WIN_WIDTH), random.randrange(0, WIN_HEIGHT - 4)) for i in range(10)]

#Inicializando variáveis
x = 100                  #Dimensão dos objetos
y = 100                  #Dimensão dos objetos
dy = 0.0                 #Impulso doodle (2 tipos)
h = 200                  #Altura
score = 0                #Pontuação
game_over = True         #Tela de inicio ou fim
GREEN = (0, 180, 0)      #Define cor

#Inicio do loop do jogo
while True:
    #Introduzindo tela inicial e atualizando o display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_over :
        show_go_screen()
        game_over = False
    event = pygame.event.get()

    # Checando os cantos da tela (Doodle consegue passar de um lado para o outro)
    if x < 0:
        x = 400
    if x > 400:
        x = 0

    #blit = Basicamente copia os pixels de uma tela na outra, nesse caso ele pega os pixels da sprite(imagem importada) e copia na tela do jogo
    win.blit(BG_IMG, (0, 0))
    #introduzindo a sprite da plataforma dentro da função plates (define as dimensões da plataforma)
    for plat in plates:
        win.blit(PLAT_IMG, (plat.x, plat.y))
    #Definindo teclas utilizadas no jogo (para direita e esquerda) e quanto o doodle irá ser deslocado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 3
        DOODLE_IMG = pygame.image.load(os.path.join("images", "DoodleEngineer.png"))
    if keys[pygame.K_RIGHT]:
        x += 3
        #Fazendo o flip na imagem do doodle para que quando a tecla for pressionada a sprite vire também
        DOODLE_IMG = pygame.transform.flip(pygame.image.load(os.path.join("images", "DoodleEngineer.png")), True, False)

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
        dy = -1           #Impulso de colisão com o chão
    for event in event:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Definindo dimensões de colisão da plataforma com o doodle
    for plat in plates:
        if (x + 40 > plat.x) and (x + 40 < plat.x + 150) and (y + 80 > plat.y) and (y + 70 < plat.y + 14) and dy > 0:
            dy = -10      #Impulso de colisão com a plataforma

    text = SCORE_FONT.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 25))
    win.blit(DOODLE_IMG, (x, y))

    pygame.display.update()