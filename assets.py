import pygame
from configuracoes import *
fundo = 'fundo'

def load_assets():
    assets = {}
    assets[fundo] = pygame.transform.scale(pygame.image.load('files/images/main_field.png').convert(),(WIDTH,HEIGHT))
    assets['Carro_Piloto'] = pygame.transform.scale( pygame.image.load('files/images/piloto.png').convert_alpha(), (WIDTH_CAR,HEIGHT_CAR))
    assets['inimigo'] = pygame.transform.scale( pygame.image.load('files/images/inimigo.png').convert_alpha(), (WIDTH_CAR,HEIGHT_CAR))
    return assets