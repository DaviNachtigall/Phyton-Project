import pygame
import sys


LarguraPixel= 800
AlturaPixel = 600
Grade = 8
TamSquare = 60 # Tamanho de cada célula do tabuleiro

# Centraliza o tabuleiro na tela
EixoX = (LarguraPixel - (Grade * TamSquare)) // 2
EixoY = (AlturaPixel - (Grade * TamSquare)) // 2

# Cores (R, G, B)
CorFundo = (20, 20, 30)       # Azul escuro
CorLinha = (100, 100, 120)    # Cinza para a grade
CorGrama = (40, 60, 40)       # Verde escuro para o fundo do grid
CorG1 = (100, 255, 100) # Verde brilhante
CorG2 = (100, 100, 255) # Azul brilhante
CorLixo = (150, 100, 50)      # Marrom para o rastro
CorText = (255, 255, 255)    # Branco

pygame.init()
Tela = pygame.display.set_mode((LarguraPixel, AlturaPixel))
pygame.display.set_caption("Corrida Guaxinim - G1 vs G2")
Relogio = pygame.time.Clock()

# Fonte para textos (interface e rastro)
FontePequena = pygame.font.SysFont("arial", 20, bold=True)
FonteGrande = pygame.font.SysFont("arial", 40, bold=True)

Campo = [[0 for _ in range(Grade)] for _ in range(Grade)]
Termino = 0
Turno = 1
PosG1 = [3, 0]
PosG2 = [4, 7]

# Define a posição inicial no campo numérico
Campo[PosG1[0]][PosG1[1]] = -1
Campo[PosG2[0]][PosG2[1]] = -2


def desenhar_grade():
    #fundo
    pygame.draw.rect(Tela, CorGrama, (EixoX, EixoY, Grade*TamSquare))

#linhas verticais
    for x in range(Grade +1):
        StartPosition = (EixoX + x * TamSquare, EixoY)
        EndPosition = (EixoX + x * TamSquare, EixoY + Grade * TamSquare)
        pygame.draw.line(Tela, CorLinha, StartPosition, EndPosition, 2)

#Horizontais
    for y in range(Grade +1):
        StartPosition = (EixoX, EixoY+  y * TamSquare)
        EndPosition = (EixoX + Grade *TamSquare, EixoY+ y * TamSquare)
        pygame.draw.line(Tela, CorGrama, StartPosition, EndPosition, 2)


def desenhar_elementos():
    for i in range(Grade):
        for j in range(Grade):
            CentroX = EixoX + j * TamSquare + TamSquare //   2
            CentroY = EixoY + i * TamSquare + TamSquare // 2

            valor = Campo[i][j]

            #G1
            if valor == -1:
                pygame.draw.circle(Tela, CorG1, (CentroX, CentroY), TamSquare // 3)
                texto = FontePequena.render("G1", True, (0, 0, 0))
                Tela.blit(texto, (CentroX, CentroY))