import pygame

def desenha_pista():
    nova_lista = []
    for y in linhas_pista:
        proporcao = y / ALTURA
        largura_linha = int(2 + proporcao * 20)  # aumenta a largura com a profundidade
        altura_linha = int(2 + proporcao * 6)    # idem para altura
        x = LARGURA // 2 - largura_linha // 2
        pygame.draw.rect(TELA, BRANCO, (x, y, largura_linha, altura_linha))

        # Atualiza a posição da linha com base na profundidade
        velocidade_linha = 2 + proporcao * 8  # linhas mais próximas descem mais rápido
        y += velocidade_linha

        # Reinicia do topo se passar da tela
        if y < ALTURA:
            nova_lista.append(y)
        else:
            nova_lista.append(0)
    return nova_lista