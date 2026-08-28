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
            CentroX = EixoX + j * TamSquare + TamSquare //  2
            CentroY = EixoY + i * TamSquare + TamSquare // 2

            valor = Campo[i][j]

            #G1
            if valor == -1:
                pygame.draw.circle(Tela, CorG1, (CentroX, CentroY), TamSquare // 3)
                texto = FontePequena.render("G1", True, (0, 0, 0))
                Tela.blit(texto, (CentroX, CentroY))

            #G2
            elif valor == -2:
                pygame.draw.circle(Tela, CorG2, (CentroX, CentroY), TamSquare // 3)
                texto = FontePequena.render("G2", True, (0, 0, 0))
                Tela.blit(texto, (CentroX, CentroY))

            #Lixo
            elif valor > 0:
                TamanhoLixo = int((TamSquare // 2) * (valor / 20) + 5)
                RectLixo = pygame.Rect(0, 0, TamanhoLixo, TamanhoLixo)
                RectLixo.center = (CentroX, CentroY)
                pygame.draw.rect(Tela, CorLixo, RectLixo)

                TextoTempo = FontePequena.render(str(valor), True, CorText)
                Tela.blit(TextoTempo, TextoTempo.get_rect(center=(CentroX, CentroY + TamanhoLixo // 2 + 5)))

def desenhar_interface():
    TextoTitulo = FonteGrande.render("CORRIDA GUAXINIM", True, CorText)
    Tela.blit(TextoTitulo, TextoTitulo.get_rect(center=(LarguraPixel // 2, 40)))

    if Termino == 0:
        CorTurno = CorG1 if Turno == 1 else CorG2
        TextoTurno = FontePequena.render(f"Turno: Jogador {Turno}", True, CorTurno)
        Tela.blit(TextoTurno, TextoTurno.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))

    else:
        if Termino == 1:
            CorTermino = CorG1
            TextoVitoria = FonteGrande.render("Guaxinim 1 venceu!!", True, CorTermino)
            Tela.blit(TextoVitoria, TextoVitoria.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))
        else:
            CorTermino = CorG2
            TextoVitoria = FonteGrande.render("Guaxinim 2 venceu!!", True, CorTermino)
            Tela.blit(TextoVitoria, TextoVitoria.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))

    # Instruções laterais

    Instr1 = [

        "G1 (Verde)",

        "W: Cima", "S: Baixo",

        "A: Esq", "D: Dir",

        "Objetivo:", "Chegar na Dir."

    ]

    Instr2 = [

        "G2 (Azul)",

        "I: Cima", "K: Baixo",

        "J: Esq", "L: Dir",

        "Objetivo:", "Chegar na Esq."

    ]

    # Instruções Laterais
    # Percorre as listas de texto usando enumerate() para obter a frase e o índice da linha (indice = 0, 1, 2...).
    # A fórmula '100 + idx * 25' calcula a posição vertical (Y) de cada frase, pulando 25 pixels por linha
    # para que os textos fiquem organizados verticalmente e não sejam desenhados uns sobre os outros.
    # G1 é desenhado na margem esquerda (X = 20) e G2 na margem direita (X = LARGURA_TELA - 150).

    for indice, linha in enumerate(Instr1):

        Txt = FontePequena.render(linha, True, CorG1)

        Tela.blit(Txt, (20, 100 + indice * 25))

    for indice, linha in enumerate(Instr2):

        Txt = FontePequena.render(linha, True, CorG1)

        Tela.blit(Txt, (LarguraPixel - 150, 100 + indice * 25))

def jogada(dx,dy):
    global PosG1, PosG2, Turno

    GuaxininNum = -1 if Turno == 1 else -2

    PosAtual = PosG1 if Turno == 1 else PosG2

    PosNovaX = PosAtual[0] + dx
    PosNovaY = PosAtual[1] + dy

    if PosNovaX > 7 or PosNovaX < 0 or PosNovaY > 7 or PosNovaY < 0 or Campo[PosNovaX][PosNovaY] != 0:
        print("Movimento inválido!")
        return False

    else:
        Campo[PosAtual[0]][PosAtual[1]] = 20  # Deixa lixo
        # Atualiza posicao
        Campo[PosNovaX][PosNovaY] = GuaxininNum

        if(GuaxininNum == -1):
            PosG1 = [PosNovaX, PosNovaY]
        else:
            PosG2 = [PosNovaX, PosNovaY]

        return True

def renovar_lixo():

    for i in range(Grade):
        for j in range(Grade):
            if Campo[i][j] > 0:
                Campo[i][j] -= 1
    return


def checar_vitoria():
    if PosG1[0] == 7:
        Termino = 1
    elif PosG2[1] == 0:
        Termino = 2
    else:
        return

def main():
    global Turno, Termino
    while Termino == 0:
        MovimentoFeito = False
        #verifica se algum evento/condicao faz o jogo terminar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN and Termino == 0:
            dx, dy = 0, 0

            #AWSD Tipo de jogada de G1
            if Turno == 1:
                if event.key == pygame.K_w:
                    dy = -1
                elif event.key == pygame.K_s:
                    dy = 1
                elif event.key == pygame.K_a:
                    dx = -1
                elif event.key == pygame.K_d:
                    dx = 1

            #JKIL tipo de jogada de G2
            elif Turno == 2:
                if event.key == pygame.K_i:
                    dy = -1
                elif event.key == pygame.K_k:
                    dy = 1
                elif event.key == pygame.K_j:
                    dx = -1
                elif event.key == pygame.K_l:
                    dx = 1

            #atualizar variavel MovimentoFeito
            if dx != 0 or dy != 0:
                if jogada(dx, dy):
                    MovimentoFeito = True

            if MovimentoFeito:
                renovar_lixo()
                checar_vitoria()


            if Termino == 0 and Turno == 1: Turno = 2
            else: Turno = 1

            # 3. Desenho (Renderização)
            Tela.fill(CorFundo)
            desenhar_grade()
            desenhar_elementos()
            desenhar_interface()

            # Atualiza a tela gráfica
            pygame.display.flip()

            # Mantém o jogo rodando a 60 FPS (quadros por segundo)
            Relogio.tick(60)

    if __name__ == "__main__":
        main()


