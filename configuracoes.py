from os import path
# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'files', 'img')
SND_DIR = path.join(path.dirname(__file__), 'files', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'files', 'font')

# Dados gerais do jogo.
WIDTH = 1280 # Largura da tela
HEIGHT = 720 # Altura da tela
FPS = 60 # Frames por segundo
WIDTH_CAR = 200
HEIGHT_CAR = 200
WIDTH_PILOT = 150
HEIGHT_PILOT = 150
WIDTH_VIDA = 50
HEIGHT_VIDA = 50
WIDTH_FAIXA = 50
HEIGHT_FAIXA = 100
WIDTH_ARVORE = 500
HEIGHT_ARVORE = 500
WIDTH_OLEO = 50
HEIGHT_OLEO = 50
WIDTH_NUVEM = 200
HEIGHT_NUVEM = 200

# Cores porque sim
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
