import pygame
from configuracoes import *
clock = pygame.time.Clock()
def start(window):
    # ----- Gera tela principal
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Py Racing')
    pygame.display.update()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        window.fill(BLACK)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip

    return state
def game_over(window):
    # ----- Gera tela principal
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Py Racing')
    pygame.display.update()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        window.fill(BLACK)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip

    return state
def janela(window):
    # ----- Gera tela principal
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Py Racing')
    pygame.display.update()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
        window.fill(BLACK)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip

    return state