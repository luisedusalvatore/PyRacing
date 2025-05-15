import pygame
import random
import assets
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
class Carro(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['inimigo']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-WIDTH_CAR)
        self.rect.y = int(HEIGHT/2)
        self.speedy = random.randint(2, 9)
        self.speedx = 0

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o carro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.image = assets['inimigo']
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, WIDTH-WIDTH_CAR)
            self.rect.y = int(HEIGHT/2)
            self.speedy = random.randint(2, 9)
            self.speedx = 0