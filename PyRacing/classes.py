import pygame
import random
import assets
from configuracoes import*
from assets import *
from janela import *

class Piloto(pygame.sprite.Sprite):
    def __init__(self, groups, assets, cor):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['Carro_Piloto'][cor]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 5
        self.speedx = 0
        self.groups = groups
        self.assets = assets
        
        self.is_shaking = False
        self.shake_timer = 0
        self.shake_duration = 2500 
        self.shake_offset_x = 0
        self.shake_offset_y = 0
        self.shake_intensity = 5  

    def start_shake(self):
       
        self.is_shaking = True
        self.shake_timer = pygame.time.get_ticks()

    def update(self):
        
        self.rect.x += self.speedx

        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

       
        if self.is_shaking:
            now = pygame.time.get_ticks()
            if now - self.shake_timer > self.shake_duration:
                self.is_shaking = False
                self.shake_offset_x = 0
                self.shake_offset_y = 0
            else:
                # Apply random shake offset
                self.shake_offset_x = random.randint(-self.shake_intensity, self.shake_intensity)
                self.shake_offset_y = random.randint(-self.shake_intensity, self.shake_intensity)
        else:
            self.shake_offset_x = 0
            self.shake_offset_y = 0

class Carro(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        n = random.randint(0, 9)
        self.assets = assets
        self.original_image = assets['inimigo'][n]
        self.base_width = WIDTH_PILOT
        self.base_height = HEIGHT_PILOT
        self.escala_min = 0.02
        self.escala_max = 1
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

        
        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

      
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

      
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

       
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, assets):
        pygame.sprite.Sprite.__init__(self)
        self.explosao = assets[explosao]
        self.frame = 0
        self.image = self.explosao[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 50

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.explosao):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosao[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Vida(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.original_image = assets[vida]
        self.base_width = WIDTH_VIDA
        self.base_height = HEIGHT_VIDA
        self.escala_min = 0.02
        self.escala_max = 1
        self.inicio_y = (HEIGHT) / 2
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH) / 2
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

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

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

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
            self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)
            self.fim_y = HEIGHT
            self.mask = pygame.mask.from_surface(self.image)

class Esquerda(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.original_image = assets[esquerda]
        self.base_width = WIDTH_FAIXA
        self.base_height = HEIGHT_FAIXA
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = HEIGHT / 2
        self.fim_y = HEIGHT
        self.inicio_x = WIDTH / 2
        self.fim_x = WIDTH / 3

        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        self.speedy = 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Direita(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.original_image = assets[direita]
        self.base_width = WIDTH_FAIXA
        self.base_height = HEIGHT_FAIXA
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = HEIGHT / 2
        self.fim_y = HEIGHT
        self.inicio_x = WIDTH / 2
        self.fim_x = 2 * WIDTH / 3

        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        self.speedy = 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Oleo(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.original_image = assets[oleo]
        self.base_width = WIDTH_OLEO
        self.base_height = HEIGHT_OLEO
        self.escala_min = 0.02
        self.escala_max = 1
        self.inicio_y = (HEIGHT) / 2
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH) / 2
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

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

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

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
            self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)
            self.fim_y = HEIGHT
            self.mask = pygame.mask.from_surface(self.image)

class ArvoreE(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[arvore][n]
        self.base_width = WIDTH_ARVORE
        self.base_height = HEIGHT_ARVORE
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = (HEIGHT / 2)
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH / 2) - 300
        self.fim_x = 0 - 500

        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        self.speedy = 7
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class ArvoreD(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[arvore][n]
        self.base_width = WIDTH_ARVORE
        self.base_height = HEIGHT_ARVORE
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = (HEIGHT / 2)
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH / 2) + 300
        self.fim_x = WIDTH + 500

        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        self.speedy = 7
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.inicio_y <= self.rect.y <= self.fim_y + 15:
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Nuvem(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[nuvem][n]
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = -WIDTH_NUVEM
        self.rect.y = random.randint(50, 210)
        self.speedx = random.randint(1, 5)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:  # Kill when fully off-screen right
            self.kill()