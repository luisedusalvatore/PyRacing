import pygame
from configuracoes import *  # Importa configurações globais (como WIDTH, HEIGHT, etc.)
import os

# Constantes que servem como chaves para os ativos (imagens, sons, fontes)
fundo = 'fundo'
explosao = 'explosao'

vida = 'vida'
vida2 = 'vida2'
esquerda = 'esquerda'
direita = 'direita'
oleo = 'oleo'
arvore = 'arvore'
estrada = 'estrada'
grama = 'grama'
ceu = 'ceu'
nuvem = 'nuvem'
pista = 'pista'
musica = 'musica'
explosao_som = 'explosao_som'
fonte = 'fonte'
fonte2 = 'fonte2'
vida_som = 'vida_som'
oleo_som = 'oleo_som'
escolha = 'escolha'

def load_assets():
    """
    Carrega todos os recursos visuais e sonoros do jogo e retorna um dicionário com esses ativos.

    Retorna:
        dict: Dicionário contendo imagens, sons e fontes utilizados no jogo.
    """
    assets = {}

    # Imagens principais
    assets[estrada] = pygame.transform.scale(
        pygame.image.load('files/img/estrada.png').convert_alpha(),
        (WIDTH - 200, HEIGHT / 2)
    )

    # Imagens de diferentes céus para variações de tempo ou turno
    assets[ceu] = [
        pygame.transform.scale(pygame.image.load('files/img/Ceu_azul.png').convert(), (WIDTH, HEIGHT / 2)), # Imagem parcialmente gerada por IA
        pygame.transform.scale(pygame.image.load('files/img/Por_do_Sol.png').convert(), (WIDTH, HEIGHT / 2)), # Imagem gerada por IA
        pygame.transform.scale(pygame.image.load('files/img/Noite.png').convert(), (WIDTH, HEIGHT / 2)) # Imagem gerada por IA
    ]

    # Imagens de grama para o ambiente
    assets[grama] = [
        pygame.transform.scale(pygame.image.load('files/img/Grama_Dia.png').convert(), (WIDTH, HEIGHT / 2)), # Imagem gerada por IA
        pygame.transform.scale(pygame.image.load('files/img/Grama_noite.png').convert(), (WIDTH, HEIGHT / 2)) # Imagem gerada por IA
    ]

    # Outros fundos e telas
    assets[fundo] = pygame.transform.scale(pygame.image.load('files/img/main_field.png').convert(), (WIDTH, HEIGHT))
    assets[escolha] = pygame.transform.scale(pygame.image.load('files/img/escolha_carro.jpg').convert_alpha(), (WIDTH, HEIGHT))

    # Carros controlados pelo jogador
    assets['Carro_Piloto'] = [
        pygame.transform.scale(pygame.image.load('files/img/piloto.png').convert_alpha(), (WIDTH_PILOT, HEIGHT_PILOT)),
        pygame.transform.scale(pygame.image.load('files/img/azul.png').convert_alpha(), (WIDTH_PILOT, HEIGHT_PILOT)),
        pygame.transform.scale(pygame.image.load('files/img/roxo.png').convert_alpha(), (WIDTH_PILOT, HEIGHT_PILOT)),
        pygame.transform.scale(pygame.image.load('files/img/verde.png').convert_alpha(), (WIDTH_PILOT, HEIGHT_PILOT))
    ]

    # Carros inimigos com variações
    assets['inimigo'] = [
        pygame.transform.scale(pygame.image.load(f'files/img/{nome}.png').convert_alpha(), (WIDTH_CAR, HEIGHT_CAR))
        for nome in ['inimigo', 'Fusca', 'uno', 'caminhao_amarelo', 'kwid_creme', 'fusca_verde', 'fusca_vermelho', 'renegade_amarelo', 'renegade_rosa']
    ] + [
        pygame.transform.scale(pygame.image.load('files/img/caminhao.png').convert_alpha(), (WIDTH_CAMINHAO, HEIGHT_CAMINHAO))
    ]

    # Vida, obstáculos e elementos de cenário
    assets[vida] = pygame.transform.scale(pygame.image.load('files/img/vida.png').convert_alpha(), (WIDTH_VIDA, HEIGHT_VIDA))
    assets[vida2] = pygame.transform.scale(pygame.image.load('files/img/vida.png').convert_alpha(), (WIDTH_VIDA, HEIGHT_VIDA))
    assets[esquerda] = pygame.transform.scale(pygame.image.load('files/img/pista_esquerda.png').convert_alpha(), (WIDTH_FAIXA, HEIGHT_FAIXA))
    assets[direita] = pygame.transform.scale(pygame.image.load('files/img/pista_direita.png').convert_alpha(), (WIDTH_FAIXA, HEIGHT_FAIXA))

    assets[arvore] = [
        pygame.transform.scale(pygame.image.load('files/img/Arvore1.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/arvore.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/arvore2.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE)),
        pygame.transform.scale(pygame.image.load('files/img/arvore3.png').convert_alpha(),(WIDTH_ARVORE, HEIGHT_ARVORE))
        ]
    assets[nuvem] = [
        pygame.transform.scale(pygame.image.load('files/img/Nuvem1.png').convert_alpha(),(WIDTH_NUVEM, HEIGHT_NUVEM)),
        pygame.transform.scale(pygame.image.load('files/img/Nuvem2.png').convert_alpha(),(WIDTH_NUVEM, HEIGHT_NUVEM)),
        pygame.transform.scale(pygame.image.load('files/img/Nuvem3.png').convert_alpha(),(WIDTH_NUVEM, HEIGHT_NUVEM))
    ]
    assets[oleo] = pygame.transform.scale(pygame.image.load('files/img/oleo.png').convert_alpha(),(WIDTH_OLEO, HEIGHT_OLEO))
    
      # Música de fundo
    assets[musica] = pygame.mixer.music.load('files/music/musica.mp3') # Musica criada por Emmraan
    pygame.mixer.music.set_volume(0.4)
    

     # Efeitos sonoros
    assets[explosao_som] = pygame.mixer.Sound('files/music/explosao.wav') # Criado por Prof.Mudkip
    assets[vida_som] = pygame.mixer.Sound('files/music/vida_up.mp3')
    assets[oleo_som] = pygame.mixer.Sound('files/music/escorregar.mp3')

     # Animação de explosão
    explosion_anim = []  # Imagens da explosão geradas por IA
    for i in range(9):
         #Os arquivos de animação são numerados de 00 a 08   
        filename = os.path.join(IMG_DIR, 'pixel_art_explosion_0{}.png'.format(i))
        img = pygame.image.load(filename).convert_alpha()
        img = pygame.transform.scale(img, (WIDTH_CAR, HEIGHT_CAR))
        explosion_anim.append(img)
    assets[explosao] = explosion_anim 
    # Fontes usadas no jogo
    assets[fonte] = pygame.font.Font(('files/font/PressStart2P.ttf'), 48)
    assets[fonte2] = pygame.font.Font(('files/font/PressStart2P.ttf'), 24)
    return assets
