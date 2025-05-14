import pygame
import random
from configuracoes import *
from assets import *
class Piloto(pygame.sprite.Sprite):
    def __init__(self,groups, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['Carro_Piloto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.groups = groups
        self.asstes = assets
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0