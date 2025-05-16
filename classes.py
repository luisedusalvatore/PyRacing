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

        self.assets = assets
        self.original_image = assets['inimigo']
        self.base_width = WIDTH_CAR
        self.base_height = HEIGHT_CAR
        self.escala_min = 0.001
        self.escala_max = 1.0
        self.inicio_y = (HEIGHT) / 2
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH) / 2
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

        # Initialize image and rect with minimum scale
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        self.speedy = random.randint(2, 3)
        self.speedx = random.randint(-1, 1)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Interpolate x-position
        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Apply scaling
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Update rect, keeping center
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Reset if off-screen
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            new_width = int(self.base_width * self.escala_min)
            new_height = int(self.base_height * self.escala_min)
            self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.inicio_x
            self.rect.y = self.inicio_y
            self.rect.x = self.inicio_x
            self.speedy = random.randint(2, 3)
            self.speedx = random.randint(-1, 1)
            self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)  # Fixed typo: fim_x_x
            self.fim_y = HEIGHT
            self.mask = pygame.mask.from_surface(self.image)