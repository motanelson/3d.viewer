import pygame
import json
import os
# Inicializar Pygame
pygame.init()

# Criar a janela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("game")

# Fonte e cores
fonte = pygame.font.Font(None, 14)
yellows = (255, 255, 0)
black = (0, 0, 0)

def carregar_nivel(s):
    
    
    f1=open(s,"r")
    r=f1.read()
    f1.close()
    rr=r.split("\n")
    ss=s.replace(".txt",".mp4")
    os.system("explorer "+ss)

    return rr

def desenhar_menu(nivel):
    """Desenha o menu gráfico do nível."""
    tela.fill(yellows)
    
    # Texto do nível
    texto = fonte.render("game", True, yellows)
    tela.blit(texto, (50, 50))

    # Desenhar opções como botões
    botoes = []
    y = 150
    
    for opcao in nivel:
        botao = pygame.Rect(50, y, 700, 50)
        pygame.draw.rect(tela, (0, 0, 0), botao)
        texto_botao = fonte.render(opcao.split("=")[0], True, yellows)
        tela.blit(texto_botao, (60, y + 10))
        botoes.append((botao,opcao.split("=")[0]))
        y += 70

    pygame.display.flip()
    return botoes

def main():
    """Loop principal do jogo."""
    nivel_atual = "main.txt"
    nivel = carregar_nivel(nivel_atual)

    rodando = True
    count=0
    while rodando:
        botoes = desenhar_menu(nivel)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                count=0
                for botao, proximo in botoes:
                    if count<len(nivel):
                        sss=nivel[count].split("=")
                    else:
                        sss=[""]
                    if len(sss)>1:
                        proximo=sss[1]
                    else:
                        proximo=""
                    if botao.collidepoint(x, y):
                        if proximo == "":
                            rodando = False
                        else:
                            if proximo.find(".txt")>-1:
                                nivel = carregar_nivel(proximo)
                                print(nivel)
                            else:
                                print(proximo)
                    count=count+1
    pygame.quit()

main()