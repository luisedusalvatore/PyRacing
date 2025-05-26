"""Gerenciamento das telas de início e game over do jogo PyRacing.

Este arquivo contém funções para exibir a tela inicial, onde o jogador escolhe
a cor do carro, e a tela de game over, exibida quando o jogo termina.
"""

import pygame
from configuracoes import *
from assets import *
# Inicializa o relógio para controlar o FPS
clock = pygame.time.Clock()

def start(window):
    """Exibe a tela inicial do jogo e permite ao jogador escolher a cor do carro.

    Args:
        window (pygame.Surface): Janela principal do Pygame onde a tela é renderizada.

    Returns:
        tuple: Estado do jogo (QUIT ou GAME) e a cor escolhida (None ou índice de 0 a 3).
    """
    # Carrega os assets do jogo
    assets = load_assets()
    # Imagem de fundo da tela inicial
    background_initial = assets['fundo']
    # Imagem de fundo da tela de escolha de cor
    background_escolha = assets['escolha']
    # Define a fonte para o texto
    font = pygame.font.SysFont(None, 48)
    # Renderiza o título "PyRacing"
    title = font.render('PyRacing', True, WHITE)
    # Centraliza o título na tela
    title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/3))
    # Renderiza a instrução para começar
    instructions = font.render('Press Any Key to Start', True, WHITE)
    # Centraliza a instrução na tela
    instructions_rect = instructions.get_rect(center=(WIDTH/2, HEIGHT/2))

    # Controle do loop da tela inicial
    running = True
    # Estado inicial da tela (início ou escolha de cor)
    estado = 'initial'
    # Cor do carro (inicialmente None)
    cor = None

    # Loop da tela inicial
    while running:
        # Controla a taxa de quadros por segundo
        clock.tick(FPS)
        # Processa eventos do Pygame
        for event in pygame.event.get():
            # Fecha o jogo ao clicar no botão de fechar
            if event.type == pygame.QUIT:
                return QUIT, None
            # Estado inicial: aguarda pressionar uma tecla para ir à escolha de cor
            if estado == 'initial':
                if event.type == pygame.KEYDOWN:
                    estado = 'escolha'
            # Estado de escolha: seleciona a cor do carro
            elif estado == 'escolha':
                if event.type == pygame.KEYDOWN:
                    # Escolhe a cor com base na tecla pressionada
                    if event.key == pygame.K_1:
                        cor = 0
                        running = False
                    elif event.key == pygame.K_2:
                        cor = 1
                        running = False
                    elif event.key == pygame.K_3:
                        cor = 2
                        running = False
                    elif event.key == pygame.K_4:
                        cor = 3
                        running = False

        # Preenche a tela com preto
        window.fill(BLACK)
        # Renderiza a tela inicial
        if estado == 'initial':
            window.blit(background_initial, (0, 0))
            window.blit(title, title_rect)
            window.blit(instructions, instructions_rect)
        # Renderiza a tela de escolha de cor
        elif estado == 'escolha':
            window.blit(background_escolha, (0, 0))

        # Atualiza a tela
        pygame.display.flip()

    # Retorna o estado do jogo e a cor escolhida
    return GAME, cor

def game_over(window):
    """Exibe a tela de game over quando o jogador perde todas as vidas.

    Args:
        window (pygame.Surface): Janela principal do Pygame onde a tela é renderizada.

    Returns:
        int: Estado do jogo (QUIT ou INIT).
    """
    # Carrega os assets do jogo
    assets = load_assets()
    # Define as fontes para os textos
    font = assets[fonte]
    font2 = assets[fonte2]
    # Renderiza o texto "GAME OVER"
    game_over_text = font.render("GAME OVER", True, RED)
    # Renderiza a instrução para reiniciar
    game_over_text2 = font2.render("Aperte qualquer tecla para voltar a jogar", True, RED)
    # Centraliza o texto "GAME OVER"
    text_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 20))
    # Centraliza a instrução de reinício
    text_rect2 = game_over_text2.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 20))
    # Controle do loop da tela de game over
    running = True

    # Loop da tela de game over
    while running:
        # Controla a taxa de quadros por segundo
        clock.tick(FPS)
        # Processa eventos do Pygame
        for event in pygame.event.get():
            # Fecha o jogo ao clicar no botão de fechar
            if event.type == pygame.QUIT:
                return QUIT
            # Volta para a tela inicial ao pressionar uma tecla
            if event.type == pygame.KEYUP:
                return INIT
        # Preenche a tela com preto
        window.fill(BLACK)
        # Desenha os textos na tela
        window.blit(game_over_text, text_rect)
        window.blit(game_over_text2, text_rect2)
        # Atualiza a tela
        pygame.display.flip()