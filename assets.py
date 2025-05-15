import pygame
from configuracoes import *
fundo = 'fundo'

def load_assets():
    assets = {}
    assets[fundo] = pygame.image.load('files/images/main_field.png').convert()
    assets['Carro_Piloto'] = pygame.image.load('files/images/piloto.png').convert_alpha()
    return assets