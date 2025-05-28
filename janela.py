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
    assets[musica_inicio].play(-1)  # Toca a música de fundo da tela inicial
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

    assets[musica_inicio].stop()  # Para a música de fundo
    return GAME, cor

def game_over(window, score):
    """Exibe a tela de game over com a pontuação do jogador e os 5 melhores scores.

    Args:
        window (pygame.Surface): Janela principal do Pygame onde a tela é renderizada.
        score (int): Pontuação do jogador na partida.

    Returns:
        int: Estado do jogo (QUIT ou INIT).
    """
    # Carrega os assets do jogo
    assets = load_assets()
    # Para a música do jogo
    pygame.mixer.music.stop()
    # Define as fontes para os textos
    font = assets[fonte]
    font_small = assets[fonte2]
    # Toca a música de game over
    assets[musica_game_over].play(-1)
    # Controle do loop da tela de game over
    running = True

    while running:
        # Controla a taxa de quadros por segundo
        clock.tick(FPS)
        # Processa eventos do Pygame
        for event in pygame.event.get():
            # Fecha o jogo ao clicar no botão de fechar
            if event.type == pygame.QUIT:
                assets[musica_game_over].stop()
                return QUIT
            # Volta para a tela inicial ao pressionar uma tecla
            if event.type == pygame.KEYDOWN:
                assets[musica_game_over].stop()
                return INIT

        # Preenche a tela com preto
        window.fill(BLACK)
        # Renderiza o texto "GAME OVER"
        game_over_text = font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(WIDTH / 2, HEIGHT / 6))
        window.blit(game_over_text, text_rect)

        # Exibe a pontuação atual do jogador
        current_score_text = font_small.render(f"Your Score: {score}", True, WHITE)
        current_score_rect = current_score_text.get_rect(center=(WIDTH/2, HEIGHT/4))
        window.blit(current_score_text, current_score_rect)

        # Exibe os 5 melhores scores
        for i, hs_score in enumerate(sorted(main_score, reverse=True)):
            if hs_score > 0:  # Mostra apenas scores não nulos
                text = font_small.render(f"{i+1}. {hs_score}", True, WHITE)
                text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/3 + i * 40))
                window.blit(text, text_rect)

        # Instrução para reiniciar
        instruction = font_small.render("Press any key to restart", True, WHITE)
        instruction_rect = instruction.get_rect(center=(WIDTH/2, HEIGHT - 50))
        window.blit(instruction, instruction_rect)

        # Atualiza a tela
        pygame.display.flip()

    return INIT