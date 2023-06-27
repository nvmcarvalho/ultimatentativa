import pygame
import winsound
import sys
from tkinter import Tk, simpledialog
import json
pygame.init()
tamanho = 800, 600
tela = pygame.display.set_mode(tamanho)
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("bg.jpg")
pontos = []
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
fonte = pygame.font.Font(None, 24)

def abrirDialogo():
    root = Tk()
    root.withdraw()
    try:
        nome = simpledialog.askstring("Estrela", "Digite o nome da estrela:")
    except:
        nome = None
    root.destroy()
    return nome

def salvarPontos():
    with open("pontos.json", "w") as arquivo:
        json.dump(pontos, arquivo)

def carregarPontos():
    global pontos
    try:
        with open("pontos.json", "r") as arquivo:
            pontos = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        pontos = []

def deletarPontos():
    global pontos
    pontos = []

def desenharLinhas():
    for i in range(len(pontos) - 1):
        ponto1 = pontos[i]
        ponto2 = pontos[i + 1]
        x1, y1 = ponto1["coordenadas"]
        x2, y2 = ponto2["coordenadas"]
        pygame.draw.line(tela, branco, (x1, y1), (x2, y2), 2)
        meioX = (x1 + x2) // 2
        meioY = (y1 + y2) // 2
        somaX = x1 + x2
        somaY = y1 + y2
        textoSoma = fonte.render(f"({somaX}, {somaY})", True, vermelho)
        rectSoma = textoSoma.get_rect(center=(meioX, meioY))
        tela.blit(textoSoma, rectSoma)
        texto1 = fonte.render(f"({x1}, {y1})", True, branco)
        rect1 = texto1.get_rect(center=(x1, y1 - 20))
        tela.blit(texto1, rect1)
        texto2 = fonte.render(f"({x2}, {y2})", True, branco)
        rect2 = texto2.get_rect(center=(x2, y2 - 20))
        tela.blit(texto2, rect2)

carregarPontos()

direita = True
pygame.mixer.music.load("somDeEspaço.mp3")
pygame.mixer.music.play(-1)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvarPontos()
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                salvarPontos()
                pygame.quit()
                sys.exit()
            elif evento.key == pygame.K_F10:
                salvarPontos()
            elif evento.key == pygame.K_F11:
                carregarPontos()
            elif evento.key == pygame.K_F12:
                deletarPontos()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                try:
                    x, y = evento.pos
                except:
                    continue
                try:
                    nome = abrirDialogo()
                except:
                    nome = None
                ponto = {
                    "coordenadas": (x, y),
                    "nome": nome
                }
                pontos.append(ponto)
                winsound.Beep(500, 300)
    tela.blit(fundo, (0, 0))
    if len(pontos) > 1:
        desenharLinhas()
    for ponto in pontos:
        x, y = ponto["coordenadas"]
        nome = ponto["nome"]
        pygame.draw.circle(tela, branco, (x, y), 5)
        textoNome = fonte.render(nome, True, branco)
        rectNome = textoNome.get_rect(center=(x, y - 35))
        tela.blit(textoNome, rectNome)
    textoSalvar = fonte.render("Pressione F10 para salvar os pontos", True, branco)
    textoCarregar = fonte.render("Pressione F11 para carregar os pontos", True, branco)
    textoDeletar = fonte.render("Pressione F12 para deletar os pontos", True, branco)
    tela.blit(textoSalvar, (10, 10))
    tela.blit(textoCarregar, (10, 40))
    tela.blit(textoDeletar, (10, 70))

    pygame.display.flip()

