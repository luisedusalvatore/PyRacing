import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets

def fade(janela, atual, proximo, pos, duracao, passado):
    """Aplica um efeito de transição (fade) entre duas imagens.

    Args:
        janela (pygame.Surface): Janela onde a transição será renderizada.
        atual (pygame.Surface): Imagem atual (origem da transição).
        proximo (pygame.Surface): Imagem destino da transição.
        pos (tuple): Posição (x, y) onde as imagens serão desenhadas.
        duracao (int): Duração total da transição em milissegundos.
        passado (int): Tempo decorrido desde o início da transição em milissegundos.

    Returns:
        None
    """
    # Calcula o valor de alpha para a transição (0 a 255)
    alpha = min(255, max(0, 255 * (passado / duracao)))  # Restringe alpha entre 0 e 255
    # Define a transparência da imagem atual (desaparecendo)
    atual.set_alpha(255 - alpha)
    # Define a transparência da próxima imagem (aparecendo)
    proximo.set_alpha(alpha)
    # Desenha a imagem atual na posição especificada
    janela.blit(atual, pos)
    # Desenha a próxima imagem na mesma posição
    janela.blit(proximo, pos)