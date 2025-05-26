"""Configurações gerais do jogo PyRacing.

Este arquivo define constantes para dimensões da tela, tamanhos de sprites,
cores, caminhos de arquivos e estados do jogo.
"""

from os import path

# Define os caminhos para os diretórios de recursos
# Diretório para imagens
IMG_DIR = path.join(path.dirname(__file__), 'files', 'img')
# Diretório para sons
SND_DIR = path.join(path.dirname(__file__), 'files', 'snd')
# Diretório para fontes
FNT_DIR = path.join(path.dirname(__file__), 'files', 'font')

# Configurações gerais do jogo
# Largura da tela em pixels
WIDTH = 1280
# Altura da tela em pixels
HEIGHT = 720
# Frames por segundo
FPS = 60
# Largura do sprite do carro inimigo
WIDTH_CAR = 200
# Altura do sprite do carro do inimigo
HEIGHT_CAR = 200
# Largura do sprite do caminhão (inimigo)
WIDTH_CAMINHAO = 500
# Altura do sprite do caminhão (inimigo)
HEIGHT_CAMINHAO = 500
# Largura do sprite do piloto
WIDTH_PILOT = 150
# Altura do sprite do piloto
HEIGHT_PILOT = 150
# Largura do sprite de vida
WIDTH_VIDA = 50
# Altura do sprite de vida
HEIGHT_VIDA = 50
# Largura do sprite das faixas laterais
WIDTH_FAIXA = 50
# Altura do sprite das faixas laterais
HEIGHT_FAIXA = 100
# Largura do sprite das árvores
WIDTH_ARVORE = 500
# Altura do sprite das árvores
HEIGHT_ARVORE = 500
# Largura do sprite da mancha de óleo
WIDTH_OLEO = 50
# Altura do sprite da mancha de óleo
HEIGHT_OLEO = 50
# Largura do sprite das nuvens
WIDTH_NUVEM = 200
# Altura do sprite das nuvens
HEIGHT_NUVEM = 200

# Definição de cores básicas (RGB)
WHITE = (255, 255, 255)  # Cor branca
BLACK = (0, 0, 0)        # Cor preta
RED = (255, 0, 0)        # Cor vermelha
GREEN = (0, 255, 0)      # Cor verde
BLUE = (0, 0, 255)       # Cor azul
YELLOW = (255, 255, 0)   # Cor amarela

# Estados do jogo para controle do fluxo
INIT = 0        # Estado inicial (tela de início)
GAME = 1        # Estado de jogo ativo
QUIT = 2        # Estado de saída do jogo
GAME_OVER = 3   # Estado de fim de jogo