"""Definição das classes de sprites para o jogo PyRacing.

Este arquivo contém as classes que representam os objetos do jogo, como o carro do jogador,
inimigos, vidas, faixas, óleo, árvores, nuvens e explosões.
"""

import pygame
import random
import assets
from configuracoes import *
from assets import *
from janela import *

class Piloto(pygame.sprite.Sprite):
    """Classe que representa o carro controlado pelo jogador.

    Attributes:
        image (pygame.Surface): Imagem do carro do jogador.
        rect (pygame.Rect): Retângulo que define a posição e tamanho do carro.
        speedx (int): Velocidade horizontal do carro.
        is_shaking (bool): Indica se o carro está tremendo (efeito de colisão com óleo).
        shake_offset_x (int): Deslocamento horizontal para o efeito de trepidação.
        shake_offset_y (int): Deslocamento vertical para o efeito de trepidação.
    """
    def __init__(self, groups, assets, cor):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada do jogador (acima de todos)
        self._layer = 3  # ALTERAÇÃO: Camada 3 para o jogador
        # Define a imagem do carro com base na cor escolhida
        self.image = assets['Carro_Piloto'][cor]
        # Cria uma máscara para colisões precisas
        self.mask = pygame.mask.from_surface(self.image)
        # Define o retângulo da imagem
        self.rect = self.image.get_rect()
        # Posiciona o carro no centro horizontal da tela
        self.rect.centerx = WIDTH / 2
        # Posiciona o carro próximo à base da tela
        self.rect.bottom = HEIGHT - 5
        # Velocidade horizontal inicial
        self.speedx = 0
        # Armazena os grupos de sprites
        self.groups = groups
        # Armazena os assets do jogo
        self.assets = assets
        
        # Controle do efeito de trepidação
        self.is_shaking = False
        self.shake_timer = 0
        # Duração do efeito de trepidação (ms)
        self.shake_duration = 2500 
        self.shake_offset_x = 0
        self.shake_offset_y = 0
        # Intensidade do efeito de trepidação
        self.shake_intensity = 5  

    def start_shake(self):
        """Inicia o efeito de trepidação do carro."""
        # Ativa o efeito de trepidação
        self.is_shaking = True
        # Registra o tempo de início
        self.shake_timer = pygame.time.get_ticks()

    def update(self):
        """Atualiza a posição e o estado do carro."""
        # Move o carro horizontalmente
        self.rect.x += self.speedx

        # Limita o movimento dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        # Gerencia o efeito de trepidação
        if self.is_shaking:
            now = pygame.time.get_ticks()
            # Verifica se o tempo de trepidação acabou
            if now - self.shake_timer > self.shake_duration:
                self.is_shaking = False
                self.shake_offset_x = 0
                self.shake_offset_y = 0
            else:
                # Aplica deslocamentos aleatórios para simular trepidação
                self.shake_offset_x = random.randint(-self.shake_intensity, self.shake_intensity)
                self.shake_offset_y = random.randint(-self.shake_intensity, self.shake_intensity)
        else:
            self.shake_offset_x = 0
            self.shake_offset_y = 0

class Carro(pygame.sprite.Sprite):
    """Classe que representa os carros inimigos.

    Attributes:
        image (pygame.Surface): Imagem do carro inimigo.
        rect (pygame.Rect): Retângulo que define a posição e tamanho do carro.
        speedy (int): Velocidade vertical do carro.
        speedx (int): Velocidade horizontal do carro.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada dos carros inimigos (acima das faixas)
        self._layer = 2  # ALTERAÇÃO: Camada 2 para carros inimigos
        # Escolhe uma imagem aleatória para o inimigo
        n = random.randint(0, 9)
        self.assets = assets
        self.original_image = assets['inimigo'][n]
        # Dimensões base do sprite
        self.base_width = WIDTH_PILOT
        self.base_height = HEIGHT_PILOT
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.02
        self.escala_max = 1
        # Posição inicial vertical (meio da tela)
        self.inicio_y = (HEIGHT) / 2
        # Posição final vertical (base da tela)
        self.fim_y = HEIGHT
        # Posição inicial horizontal (centro da tela)
        self.inicio_x = (WIDTH) / 2
        # Posição final horizontal (aleatória dentro dos limites)
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min) 
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define velocidades inicial
        self.speedy = random.randint(2, 3)
        self.speedx = random.randint(-1, 1)
        # Cria uma máscara para colisões
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara do carro inimigo."""
        # Move o carro nas direções x e y
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Remove o sprite se sair da tela
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    """Classe que representa a animação de explosão.

    Attributes:
        image (pygame.Surface): Imagem atual da animação.
        rect (pygame.Rect): Retângulo que define a posição da explosão.
        frame (int): Índice do quadro atual da animação.
    """
    def __init__(self, center, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada da explosão (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para explosões
        # Lista de imagens da animação de explosão
        self.explosao = assets[explosao]
        self.frame = 0
        # Define a imagem inicial
        self.image = self.explosao[self.frame]
        self.rect = self.image.get_rect()
        # Posiciona a explosão no centro especificado
        self.rect.center = center
        # Registra o tempo do último quadro
        self.last_update = pygame.time.get_ticks()
        # Intervalo entre quadros (ms)
        self.frame_ticks = 50

    def update(self):
        """Atualiza a animação da explosão."""
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update

        # Avança para o próximo quadro após o intervalo
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            # Remove o sprite se a animação terminar
            if self.frame == len(self.explosao):
                self.kill()
            else:
                # Atualiza a imagem e mantém o centro
                center = self.rect.center
                self.image = self.explosao[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Vida(pygame.sprite.Sprite):
    """Classe que representa os itens de vida coletáveis.

    Attributes:
        image (pygame.Surface): Imagem do item de vida.
        rect (pygame.Rect): Retângulo que define a posição e tamanho do item.
        speedy (int): Velocidade vertical do item.
        speedx (int): Velocidade horizontal do item.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das vidas (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para vidas
        self.assets = assets
        self.original_image = assets[vida]
        # Dimensões base do sprite
        self.base_width = WIDTH_VIDA
        self.base_height = HEIGHT_VIDA
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.02
        self.escala_max = 1
        self.inicio_y = (HEIGHT) / 2
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH) / 2
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min) 
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define velocidades iniciais
        self.speedy = random.randint(2, 3)
        self.speedx = random.randint(-1, 1)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara do item de vida."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Reposiciona o sprite se sair da tela
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
    """Classe que representa as faixas laterais à esquerda da estrada.

    Attributes:
        image (pygame.Surface): Imagem da faixa lateral.
        rect (pygame.Rect): Retângulo que define a posição e tamanho da faixa.
        speedy (int): Velocidade vertical da faixa.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das faixas (abaixo de todos)
        self._layer = 0  # ALTERAÇÃO: Camada 0 para faixas
        self.assets = assets
        self.original_image = assets[esquerda]
        # Dimensões base do sprite
        self.base_width = WIDTH_FAIXA
        self.base_height = HEIGHT_FAIXA
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = HEIGHT / 2
        self.fim_y = HEIGHT
        self.inicio_x = WIDTH / 2
        # Posiciona a faixa à esquerda da estrada
        self.fim_x = WIDTH / 3

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define a velocidade vertical
        self.speedy = 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara da faixa esquerda."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Remove o sprite se sair da tela
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Direita(pygame.sprite.Sprite):
    """Classe que representa as faixas laterais à direita da estrada.

    Attributes:
        image (pygame.Surface): Imagem da faixa lateral.
        rect (pygame.Rect): Retângulo que define a posição e tamanho da faixa.
        speedy (int): Velocidade vertical da faixa.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das faixas (abaixo de todos)
        self._layer = 0  # ALTERAÇÃO: Camada 0 para faixas
        self.assets = assets
        self.original_image = assets[direita]
        # Dimensões base do sprite
        self.base_width = WIDTH_FAIXA
        self.base_height = HEIGHT_FAIXA
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = HEIGHT / 2
        self.fim_y = HEIGHT
        self.inicio_x = WIDTH / 2
        # Posiciona a faixa à direita da estrada
        self.fim_x = 2 * WIDTH / 3

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define a velocidade vertical
        self.speedy = 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara da faixa direita."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Remove o sprite se sair da tela
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Oleo(pygame.sprite.Sprite):
    """Classe que representa as manchas de óleo na pista.

    Attributes:
        image (pygame.Surface): Imagem da mancha de óleo.
        rect (pygame.Rect): Retângulo que define a posição e tamanho do óleo.
        speedy (int): Velocidade vertical do óleo.
        speedx (int): Velocidade horizontal do óleo.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada do óleo (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para óleo
        self.assets = assets
        self.original_image = assets[oleo]
        # Dimensões base do sprite
        self.base_width = WIDTH_OLEO
        self.base_height = HEIGHT_OLEO
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.02
        self.escala_max = 1
        self.inicio_y = (HEIGHT) / 2
        self.fim_y = HEIGHT
        self.inicio_x = (WIDTH) / 2
        self.fim_x = random.randint(40, WIDTH - WIDTH_CAR - 40)

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define velocidades iniciais
        self.speedy = random.randint(2, 3)
        self.speedx = random.randint(-1, 1)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara da mancha de óleo."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Reposiciona o sprite se sair da tela
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
    """Classe que representa as árvores à esquerda da pista.

    Attributes:
        image (pygame.Surface): Imagem da árvore.
        rect (pygame.Rect): Retângulo que define a posição e tamanho da árvore.
        speedy (int): Velocidade vertical da árvore.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das árvores (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para árvores
        # Escolhe uma imagem aleatória para a árvore
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[arvore][n]
        # Dimensões base do sprite
        self.base_width = WIDTH_ARVORE
        self.base_height = HEIGHT_ARVORE
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = (HEIGHT / 2)
        self.fim_y = HEIGHT
        # Posiciona a árvore à esquerda da pista
        self.inicio_x = (WIDTH / 2) - 300
        self.fim_x = 0 - 500

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define a velocidade vertical
        self.speedy = 7
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara da árvore à esquerda."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Remove o sprite se sair da tela
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class ArvoreD(pygame.sprite.Sprite):
    """Classe que representa as árvores à direita da pista.

    Attributes:
        image (pygame.Surface): Imagem da árvore.
        rect (pygame.Rect): Retângulo que define a posição e tamanho da árvore.
        speedy (int): Velocidade vertical da árvore.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das árvores (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para árvores
        # Escolhe uma imagem aleatória para a árvore
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[arvore][n]
        # Dimensões base do sprite
        self.base_width = WIDTH_ARVORE
        self.base_height = HEIGHT_ARVORE
        # Escala mínima e máxima para efeito de perspectiva
        self.escala_min = 0.2
        self.escala_max = 1.0
        self.inicio_y = (HEIGHT / 2)
        self.fim_y = HEIGHT
        # Posiciona a árvore à direita da pista
        self.inicio_x = (WIDTH / 2) + 300
        self.fim_x = WIDTH + 500

        # Inicializa a imagem com a escala mínima
        new_width = int(self.base_width * self.escala_min)
        new_height = int(self.base_height * self.escala_min)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.inicio_x
        self.rect.y = self.inicio_y

        # Define a velocidade vertical
        self.speedy = 7
        self.speedx = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição, escala e máscara da árvore à direita."""
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Ajusta a posição e escala com base na perspectiva
        if self.inicio_y <= self.rect.y <= self.fim_y + 15: # Equação de escalonamento gerada por IA
            proporcao = (self.rect.y - self.inicio_y) / (self.fim_y - self.inicio_y)
            self.rect.centerx = self.inicio_x + (self.fim_x - self.inicio_x) * proporcao
            scale = self.escala_min + (self.escala_max - self.escala_min) * proporcao
        else:
            scale = self.escala_min

        # Redimensiona a imagem com base na escala
        new_width = int(self.base_width * scale)
        new_height = int(self.base_height * scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.mask = pygame.mask.from_surface(self.image)

        # Mantém o centro do retângulo após redimensionamento
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

        # Remove o sprite se sair da tela
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class Nuvem(pygame.sprite.Sprite):
    """Classe que representa as nuvens no céu.

    Attributes:
        image (pygame.Surface): Imagem da nuvem.
        rect (pygame.Rect): Retângulo que define a posição e tamanho da nuvem.
        speedx (int): Velocidade horizontal da nuvem.
    """
    def __init__(self, assets):
        # Inicializa a classe base de sprite do Pygame
        pygame.sprite.Sprite.__init__(self)
        # Define a camada das nuvens (mesma camada de outros objetos)
        self._layer = 1  # ALTERAÇÃO: Camada 1 para nuvens
        # Escolhe uma imagem aleatória para a nuvem
        n = random.randint(0, 2)
        self.assets = assets
        self.original_image = assets[nuvem][n]
        self.image = self.original_image
        self.rect = self.image.get_rect()
        # Posiciona a nuvem fora da tela à esquerda
        self.rect.x = -WIDTH_NUVEM
        # Posiciona a nuvem em uma altura aleatória
        self.rect.y = random.randint(50, 210)
        # Define a velocidade horizontal
        self.speedx = random.randint(1, 5)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """Atualiza a posição da nuvem."""
        self.rect.x += self.speedx
        # Remove a nuvem se sair da tela à direita
        if self.rect.left > WIDTH:
            self.kill()