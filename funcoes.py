import pygame
from configuracoes import *
import os
from classes import *
from assets import load_assets

def triangulo (janela, imagem, inicio_y, fim_y, esquerda, direita, apice_x, apice_y):
    altura = fim_y - inicio_y
    largura = direita - esquerda
    superficie = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    pygame.draw.polygon(superficie, (0,0,0,0), [(apice_x,apice_y),(esquerda, altura),(direita,altura)])
    estrada_escala = pygame.transform.scale(imagem, (largura,altura))
    superficie.blit(estrada_escala, (0,0), special_flags=pygame.BLEND_RGBA_MIN)

    janela.blit(superficie, (0,0))