import pygame
from configuracoes import *
from assets import *
clock = pygame.time.Clock()
def start(window):
    estado = False
    if estado == False:
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
    else: 
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Py Racing')
        assets = load_assets()
        background = assets[escolha]
        running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            if event.type == pygame.KEYDOWN:
                estado = True
            if event.type == pygame.K_1 and estado == True:
                cor = 0
            if event.type == pygame.K_2 and estado == True:
                cor = 1
            if event.type == pygame.K_3 and estado == True:
                cor = 1
            if event.type == pygame.K_4 and estado == True:
                cor = 3
                running = False
        window.fill(BLACK)
        window.blit(background, (0, 0))
        window.blit(title, title_rect)
        window.blit(instructions, instructions_rect)
        pygame.display.flip()
    return state
def game_over(window):
    assets = load_assets()
    font = assets[fonte]
    font2 = assets[fonte2]
    game_over_text = font.render("GAME OVER", True, RED)
    game_over_text2 = font2.render("Aperte qualquer tecla para voltar a jogar", True, RED)
    text_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 20))
    text_rect2 = game_over_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYUP:
                return INIT  # Go back to game screen
        window.fill(BLACK)
        window.blit(game_over_text, text_rect)  # Draw first text
        window.blit(game_over_text2, text_rect2)  # Draw second text
        pygame.display.flip()