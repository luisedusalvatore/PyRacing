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
        self.rect.bottom = HEIGHT - 5
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
        self.base_width = WIDTH_PILOT
        self.base_height = HEIGHT_PILOT
        self.escala_min = 0.0001
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

class Explosion (pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__ (self,center, assets):
        # Criador do Sprite
        pygame.sprite.Sprite.__init__(self)
        # Animação da explosao guardada
        self.explosao = assets[explosao]

        # Inicia a animação, colocando posicionando a explosao no display.
        self.frame = 0 # Armazena o índica atual
        self.image = self.explosao[self.frame] # Primeira imagem da explosao
        self.rect =self.image.get_rect() 
        self.rect.center = center # Centraliza a imagem no centro do sprite

        # Contar o tempo do programa
        self.last_update = pygame.time.get_ticks()
        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50
    def update(self):
        # Verificação da contagem atual
        # tempo que a função está rodando
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosao):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosao[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
