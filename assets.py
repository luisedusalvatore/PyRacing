import pygame
from configuracoes import *
import os
fundo = 'fundo'
explosao = 'explosao'
home = 'home'
vida = 'vida'
vida2  = 'vida2'
esquerda = 'esquerda'
direita = 'direita'
oleo = 'oleo'
arvore = 'arvore'
estrada = 'estrada'
grama = 'grama'
ceu = 'ceu'
nuvem = 'nuvem'
def load_assets():
    assets = {}
    assets[estrada] = pygame.transform.scale(pygame.image.load('files/img/estrada.png').convert_alpha(),(WIDTH - 300,HEIGHT/2))
    assets[ceu] =  pygame.transform.scale(pygame.image.load('files/img/Ceu_azul.png').convert(),(WIDTH, HEIGHT/2))           
    assets[grama] =  pygame.transform.scale(pygame.image.load('files/img/Grama_Dia.png').convert(),(WIDTH,HEIGHT/2))
    assets[fundo] = pygame.transform.scale(pygame.image.load('files/img/main_field.png').convert(),(WIDTH,HEIGHT))
    assets[home] = pygame.transform.scale(pygame.image.load('files/img/home.png').convert(),(WIDTH,HEIGHT))
    assets['Carro_Piloto'] = pygame.transform.scale( pygame.image.load('files/img/piloto.png').convert_alpha(), (WIDTH_PILOT,HEIGHT_PILOT))
    assets['inimigo'] = pygame.transform.scale( pygame.image.load('files/img/inimigo.png').convert_alpha(), (WIDTH_CAR,HEIGHT_CAR))
    assets[vida] = pygame.transform.scale(pygame.image.load('files/img/vida.png').convert_alpha(),(WIDTH_VIDA, HEIGHT_VIDA))
    assets[vida2] = pygame.transform.scale(pygame.image.load('files/img/vida.png').convert_alpha(),(WIDTH_VIDA, HEIGHT_VIDA))
    assets[esquerda] = pygame.transform.scale(pygame.image.load('files/img/pista_esquerda.png').convert_alpha(),(WIDTH_FAIXA, HEIGHT_FAIXA))
    assets[direita] = pygame.transform.scale(pygame.image.load('files/img/pista_direita.png').convert_alpha(),(WIDTH_FAIXA, HEIGHT_FAIXA))
    assets[arvore] = [
        pygame.transform.scale(pygame.image.load('files/img/arvore.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/arvore2.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/arvore3.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE))
        ]
    assets[nuvem] = [
        pygame.transform.scale(pygame.image.load('files/img/Nuvem1.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/Nuvem2.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/Nuvem3.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE))
    ]
    assets[oleo] = pygame.transform.scale(pygame.image.load('files/img/oleo.png').convert_alpha(),(WIDTH_OLEO, HEIGHT_OLEO))
    explosion_anim = []
    for i in range(9):
         #Os arquivos de animação são numerados de 00 a 08   
        filename = os.path.join(IMG_DIR, 'pixel_art_explosion_0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (WIDTH_CAR, HEIGHT_CAR))
        explosion_anim.append(img)
    assets[explosao] = explosion_anim 
    return assets
