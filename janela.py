import pygame
from configuracoes import *
from assets import *
clock = pygame.time.Clock()
def start(window):
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Py Racing')
    assets = load_assets()
    background = assets[fundo]
    font = pygame.font.SysFont(None, 48)
    title = font.render('PyRacing', True, WHITE)
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/3))
    instructions = font.render('Press Any Key to Start', True, WHITE)
    instructions_rect = instructions.get_rect(center=(WIDTH/2, HEIGHT/2))
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        window.fill(BLACK)
        window.blit(background, (0, 0))
        window.blit(title, title_rect)
        window.blit(instructions, instructions_rect)
        pygame.display.flip()

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