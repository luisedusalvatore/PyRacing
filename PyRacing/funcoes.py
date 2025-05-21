import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets

def fade(janela, atual, proximo, pos, duracao, passado):
    alpha = min(255, max(0, 255 * (passado / duracao)))  # Clamp alpha to 0–255
    atual.set_alpha(255 - alpha)
    proximo.set_alpha(alpha)
    janela.blit(atual, pos)
    janela.blit(proximo, pos)