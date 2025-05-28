import pygame
from configuracoes import *
import os
import random
from classes import *
from assets import load_assets
from funcoes import *
from janela import *

def game_screen(window, cor):
    """Tela principal do jogo PyRacing, responsável pela lógica do jogo.

    Args:
        window (pygame.Surface): Janela principal do Pygame onde o jogo é renderizado.
        cor (int): Índice da cor do carro do jogador (0 a 3).

    Returns:
        int: Estado do jogo (QUIT, GAME_OVER ou DONE).
    """
    # Carrega os assets do jogo
    assets = load_assets()
    # Inicializa o relógio para controlar o FPS
    clock = pygame.time.Clock()
    # Define as imagens de fundo (grama e céu)
    grass = assets[grama][0]
    sky = assets[ceu][0]
    # Define a imagem da pista
    pista = assets[estrada]
    # Grupos de sprites para gerenciar objetos do jogo
    all_sprites = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_vidas = pygame.sprite.Group()
    all_faixas = pygame.sprite.Group()
    all_oil = pygame.sprite.Group()
    all_arvores = pygame.sprite.Group()

    # Dicionário para armazenar todos os grupos de sprites
    groups = {}
    groups['all_enemies'] = all_enemies
    groups['all_sprites'] = all_sprites
    groups['all_vidas'] = all_vidas
    groups["all_faixas"] = all_faixas
    groups['background.extend'] = pista
    groups['all_arvores'] = all_arvores

    # Cria o sprite do jogador (piloto)
    player = Piloto(groups, assets, cor)
    all_sprites.add(player)

    # Cria as faixas laterais da estrada
    left = Esquerda(assets)
    right = Direita(assets)
    all_sprites.add(left, right)
    all_faixas.add(left, right)

    # Estados do jogo
    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    # Estados do ciclo de dia e noite
    dia = 'dia'
    por_do_sol = 'por do sol'
    nascer_do_sol = 'nascer do sol'
    noite = 'noite'
    # Pontuação inicial
    score = 0
    # Vidas iniciais do jogador
    lives = 3
    # Máximo de vidas permitidas
    max_lives = 5
    # Tempo da última explosão
    explosion_tick = 0
    # Duração da animação de explosão (ms)
    explosion_duration = 850
    # Tempo do último spawn de vida
    last_vida_spawn = pygame.time.get_ticks()
    # Intervalo para spawn de vidas (ms)
    vida_spawn_interval = random.randint(10000, 30000)
    # Intervalo para spawn de faixas (ms)
    faixa_spawn_interval = 250
    # Tempo do último spawn de faixa
    last_faixa_spawn = pygame.time.get_ticks()
    # Tempo do último spawn de inimigo
    last_enemy_spawn = pygame.time.get_ticks()
    # Intervalo para spawn de inimigos (ms)
    enemy_spawn_interval = random.randint(1000, 4000)
    # Tempo do último spawn de óleo
    oleo_spawn = pygame.time.get_ticks()
    # Intervalo para spawn de óleo (ms)
    oleo_spawn_interval = random.randint(5000, 30000)
    # Intervalo para spawn de árvores à esquerda
    arvoree_spawn_interval = random.randint(5000, 10000)
    # Tempo do último spawn de árvore à esquerda
    arvoree_spawn = pygame.time.get_ticks()
    # Intervalo para spawn de árvores à direita
    arvored_spawn_interval = random.randint(1000, 5000)
    # Tempo do último spawn de árvore à direita
    arvored_spawn = pygame.time.get_ticks()
    # Intervalo para spawn de nuvens
    nuvem_spawn_interval = random.randint(5000, 10000)
    # Tempo do último spawn de nuvem
    nuvem_spawn = pygame.time.get_ticks()
    # Tempo do último incremento de pontuação
    ultimo_incremento = pygame.time.get_ticks()
    # Duração do efeito de perda de controle (ms)
    tempo_sem_c = 2500
    # Tempo de início fora da pista
    inicio_fora_pista = None
    # Delay para penalidade fora da pista (ms)
    delay_fora_pista = 1000
    # Duração dos períodos do ciclo de dia e noite (ms)
    horarios = {
        'dia': 30000,
        'por do sol': 10000,
        'nascer do sol': 10000,
        'noite': 30000
    }
    # Momento atual do ciclo de dia e noite
    momento = 'dia'
    # Tempo do início do momento atual
    hora = pygame.time.get_ticks()
    # Controle normal ou invertido do carro
    controle = True
    # Estado de transição de ciclo de dia/noite
    esta_transicionando = False
    # Tempo de início da transição
    inicio_transicao = 0
    # Duração da transição (ms)
    duracao_transicao = 3000
    # Próximo momento do ciclo
    proximo_momento = None
    # Próximo céu para transição
    proximo_ceu = None
    # Próxima grama para transição
    proxima_grama = None

    # Toca a música de fundo em loop
    pygame.mixer.music.play(loops=-1)

    # Loop principal do jogo
    while state != DONE:
        # Controla a taxa de quadros por segundo
        clock.tick(FPS)

        # Processa eventos do Pygame
        for event in pygame.event.get():
            # Fecha o jogo ao clicar no botão de fechar
            if event.type == pygame.QUIT:
                return QUIT
            # Se o jogo está no estado PLAYING
            if state == PLAYING:
                # Controle normal do carro
                if controle == True:
                    if event.type == pygame.KEYDOWN:
                        # Move o carro para a esquerda
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx -= 12
                        # Move o carro para a direita
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx += 12
                    if event.type == pygame.KEYUP:
                        # Para o movimento horizontal ao soltar a tecla
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx = 0
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx = 0
                # Controle invertido (após colisão com óleo)
                else:
                    if event.type == pygame.KEYDOWN:
                        # Inverte o movimento para a esquerda
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx += 12
                        # Inverte o movimento para a direita
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx -= 12
                    if event.type == pygame.KEYUP:
                        # Para o movimento horizontal ao soltar a tecla
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            player.speedx = 0
                        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            player.speedx = 0

        # Lógica do jogo no estado PLAYING
        if state == PLAYING:
            now = pygame.time.get_ticks()
            # Incrementa a pontuação a cada 10 segundos
            if now - ultimo_incremento >= 10000:
                score += 100
                ultimo_incremento = now

            # Inicia transição de ciclo de dia/noite
            if not esta_transicionando and now - hora > horarios[momento]:
                esta_transicionando = True
                inicio_transicao = now
                # Define o próximo momento e assets para transição
                if momento == dia:
                    proximo_momento = por_do_sol
                    proximo_ceu = assets[ceu][1]
                    proxima_grama = assets[grama][0]
                elif momento == por_do_sol:
                    proximo_momento = noite
                    proximo_ceu = assets[ceu][2]
                    proxima_grama = assets[grama][1]
                elif momento == noite:
                    proximo_momento = nascer_do_sol
                    proximo_ceu = assets[ceu][1]
                    proxima_grama = assets[grama][0]
                elif momento == nascer_do_sol:
                    proximo_momento = dia
                    proximo_ceu = assets[ceu][0]
                    proxima_grama = assets[grama][0]

            # Gerencia a transição de ciclo
            if esta_transicionando:
                passado = now - inicio_transicao
                if passado >= duracao_transicao:
                    momento = proximo_momento
                    sky = proximo_ceu
                    grass = proxima_grama
                    hora = now
                    esta_transicionando = False
                    # Bônus de pontuação ao completar o ciclo diurno
                    if momento == dia:
                        score += 1000
                    proximo_momento = None
                    proximo_ceu = None
                    proxima_grama = None

            # Spawna novas faixas laterais
            if now - last_faixa_spawn > faixa_spawn_interval:
                left = Esquerda(assets)
                right = Direita(assets)
                # Aumenta a velocidade com base na pontuação
                right.speedy += score // 250
                left.speedy += score // 250
                all_sprites.add(left, right)
                all_faixas.add(left, right)
                last_faixa_spawn = now
            # Spawna novas vidas
            if now - last_vida_spawn > vida_spawn_interval:
                vida = Vida(assets)
                vida.speedy += score // 250
                all_sprites.add(vida)
                all_vidas.add(vida)
                last_vida_spawn = now
                vida_spawn_interval = random.randint(5000, 15000)
            # Spawna novos inimigos
            if now - last_enemy_spawn > enemy_spawn_interval:
                enemy = Carro(assets)
                enemy.speedy += score // 250
                all_sprites.add(enemy)
                all_enemies.add(enemy)
                last_enemy_spawn = now
                enemy_spawn_interval = random.randint(1000, 2000)
            # Spawna manchas de óleo
            if now - oleo_spawn > oleo_spawn_interval:
                oil = Oleo(assets)
                oil.speedy += score // 250
                all_sprites.add(oil)
                all_oil.add(oil)
                oleo_spawn = now
                oleo_spawn_interval = random.randint(5000, 50000)
            # Spawna árvores à esquerda
            if now - arvoree_spawn > arvoree_spawn_interval:
                arvoree = ArvoreE(assets)
                arvoree.speedy += score // 250
                all_sprites.add(arvoree)
                all_arvores.add(arvoree)
                arvoree_spawn = now
                arvoree_spawn_interval = random.randint(1000, 5000)
            # Spawna árvores à direita
            if now - arvored_spawn > arvored_spawn_interval:
                arvored = ArvoreD(assets)
                arvored.speedy += score // 250
                all_sprites.add(arvored)
                all_arvores.add(arvored)
                arvored_spawn = now
                arvored_spawn_interval = random.randint(1000, 5000)
            # Spawna nuvens
            if now - nuvem_spawn > nuvem_spawn_interval:
                nuvem = Nuvem(assets)
                all_sprites.add(nuvem)
                nuvem_spawn = now
                nuvem_spawn_interval = random.randint(1000, 10000)

            # Verifica colisões com inimigos
            hits = pygame.sprite.spritecollide(player, all_enemies, True, pygame.sprite.collide_mask)
            for hit in hits:
                explosao = Explosion(hit.rect.center, assets)
                all_sprites.add(explosao)
                if lives > 0:
                    assets[explosao_som].play()
                lives -= 1
                if lives == 0:
                    explosao = Explosion(player.rect.center, assets)
                    all_sprites.add(explosao)
                    player.kill()
                    state = EXPLODING
                    explosion_tick = pygame.time.get_ticks()

            # Verifica colisões com vidas
            vida_hits = pygame.sprite.spritecollide(player, all_vidas, True, pygame.sprite.collide_mask)
            for vida in vida_hits:
                score += 100
                assets[vida_som].play()
                if lives <= max_lives:
                    lives += 1
                    assets[vida_som].play()

            # Verifica colisões com óleo
            oil_hits = pygame.sprite.spritecollide(player, all_oil, True, pygame.sprite.collide_mask)
            for oil in oil_hits:
                controle = False
                assets[oleo_som].play()
                player.start_shake()
                s_controle = pygame.time.get_ticks()
            # Restaura o controle normal após o tempo definido
            if not controle and now - s_controle > tempo_sem_c:
                controle = True

            # Verifica colisões com árvores
            arvore_hits = pygame.sprite.spritecollide(player, all_arvores, False, pygame.sprite.collide_mask)
            for arvore in arvore_hits:
                assets[explosao_som].play()
                explosao = Explosion(player.rect.center, assets)
                all_sprites.add(explosao)
                player.kill()
                state = EXPLODING
                explosion_tick = pygame.time.get_ticks()

            # Verifica se o jogador saiu da pista
            if player.rect.x >= WIDTH - 160 or player.rect.x <= 160:
                if inicio_fora_pista == None:
                    inicio_fora_pista = now
                if now - inicio_fora_pista > delay_fora_pista:
                    lives -= 1
                    inicio_fora_pista = None
                    if lives == 0:
                        explosao = Explosion(player.rect.center, assets)
                        all_sprites.add(explosao)
                        player.kill()
                        state = EXPLODING
                        explosion_tick = now
                    else:
                        inicio_fora_pista = None
        # Gerencia o estado de explosão
        elif state == EXPLODING:
            now = pygame.time.get_ticks()
            if now - explosion_tick > explosion_duration:
                return GAME_OVER

        # Renderiza a tela
        window.fill(BLACK)
        # Aplica transição de fundo se necessário
        if esta_transicionando and proximo_ceu is not None:
            fade(window, sky, proximo_ceu, (0, 0), duracao_transicao, passado)
            if proxima_grama is not None and proxima_grama != grass:
                fade(window, grass, proxima_grama, (0, HEIGHT/2), duracao_transicao, passado)
            else:
                window.blit(grass, (0, HEIGHT/2))
        else:
            window.blit(sky, (0, 0))
            window.blit(grass, (0, HEIGHT/2))
        window.blit(pista, (75, HEIGHT/2))

        # Desenha as faixas primeiro (abaixo de todos)
        for faixa in all_faixas:
            window.blit(faixa.image, faixa.rect)
        
        # Desenha os outros sprites, exceto o jogador e as faixas
        for sprite in all_sprites:
            if sprite != player and sprite not in all_faixas:
                window.blit(sprite.image, sprite.rect)
        
        # Desenha o jogador com offset de trepidação, se aplicável
        if state == PLAYING:
            window.blit(player.image, (player.rect.x + player.shake_offset_x, player.rect.y + player.shake_offset_y))
        
        # Desenha os ícones de vidas
        for i in range(lives):
            window.blit(assets[vida2], (10 + i * 60, 10))

        # Renderiza a pontuação
        text_surface = assets[fonte].render(str(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.topright = (WIDTH - 100, 20)
        window.blit(text_surface, text_rect)

        # Atualiza todos os sprites
        all_sprites.update()
        # Atualiza a tela
        pygame.display.update()

    return DONE