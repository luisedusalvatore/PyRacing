import pygame
from configuracoes import *
import os
fundo = 'fundo'
explosao = 'explosao'
home = 'home'
def load_assets():
    assets = {}
    assets[fundo] = pygame.transform.scale(pygame.image.load('files/img/main_field.png').convert(),(WIDTH,HEIGHT))
    assets[home] = pygame.transform.scale(pygame.image.load('files/img/home.png').convert(),(WIDTH,HEIGHT))
    assets['Carro_Piloto'] = pygame.transform.scale( pygame.image.load('files/img/piloto.png').convert_alpha(), (WIDTH_PILOT,HEIGHT_PILOT))
    assets['inimigo'] = pygame.transform.scale( pygame.image.load('files/img/inimigo.png').convert_alpha(), (WIDTH_CAR,HEIGHT_CAR))
    explosion_anim = []
    for i in range(9):
         #Os arquivos de animação são numerados de 00 a 08   
        filename = os.path.join(IMG_DIR, 'pixel_art_explosion_0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (WIDTH_CAR, HEIGHT_CAR))
        explosion_anim.append(img)
    assets[explosao] = explosion_anim 
    return assets
