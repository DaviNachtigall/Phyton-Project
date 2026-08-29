import pygame
import sys

from pygame.draw_py import draw_polygon

LarguraPixel= 800
AlturaPixel = 600
Grade = 8
TamSquare = 60 #

# Centraliza o tabuleiro na tela
EixoX = (LarguraPixel - (Grade * TamSquare)) // 2
EixoY = (AlturaPixel - (Grade * TamSquare)) // 2

# Cores (R, G, B)
CorFundo = (60, 150, 150)
CorLinha = (30, 60, 30)
CorGrama = (100, 200, 100)
CorG1 = (82, 86, 90)
CorG2 = (106, 86, 90)
CorLixo = (40, 70, 40)
CorText = (255, 255, 255)
CorFucinhoG1 = (51, 51, 51)
CorFucinhoG2 = (70, 51, 51)
CorBandanaG1 = (200, 40, 40)
CorBandanaG2 = (40, 40, 200)

pygame.init()
Tela = pygame.display.set_mode((LarguraPixel, AlturaPixel))
pygame.display.set_caption("Corrida Guaxinim - G1 vs G2")
Relogio = pygame.time.Clock()


FontePequena = pygame.font.SysFont("arial", 20, bold=True)
FonteGrande = pygame.font.SysFont("arial", 40, bold=True)

Campo = [[0 for y in range(Grade)] for i in range(Grade)]
Termino = 0
Turno = 1
PosG1 = [0, 3]
PosG2 = [7, 4]
InvalidezG1 = 0;
InvalidezG2 = 0;

# Define a posição inicial no campo numérico
Campo[PosG1[0]][PosG1[1]] = -1
Campo[PosG2[0]][PosG2[1]] = -2


def desenhar_grade():
    #fundo
    pygame.draw.rect(Tela, CorGrama, (EixoX, EixoY, Grade*TamSquare, Grade*TamSquare))

#linhas verticais
    for x in range(Grade +1):
        StartPosition = (EixoX + x * TamSquare, EixoY)
        EndPosition = (EixoX + x * TamSquare, EixoY + Grade * TamSquare)
        pygame.draw.line(Tela, CorLinha, StartPosition, EndPosition, 2)

#Horizontais
    for y in range(Grade +1):
        StartPosition = (EixoX, EixoY+  y * TamSquare)
        EndPosition = (EixoX + Grade *TamSquare, EixoY+ y * TamSquare)
        pygame.draw.line(Tela, CorLinha, StartPosition, EndPosition, 2)

def desenha_guaxinim(CorGuaxinin, CorFucinho, CorBandana, CentroX, CentroY, Raio):
    OrelhaTam = Raio/2

    OrelhaEsq = [
        (CentroX - Raio * 0.6, CentroY - Raio * 0.1),  # base interna
        (CentroX - Raio * 1.1, CentroY - Raio * 1.3),  # ponta
        (CentroX - Raio * 0.1, CentroY - Raio * 0.9),  # base externa
    ]
    OrelhaDir = [
        (CentroX + Raio * 0.6, CentroY - Raio * 0.1),
        (CentroX + Raio * 1.1, CentroY - Raio * 1.3),
        (CentroX + Raio * 0.1, CentroY - Raio * 0.9),
    ]
    Fucinho = [
        (CentroX - Raio * 0.45, CentroY + Raio * 0.3),  # base esquerda
        (CentroX + Raio * 0.45, CentroY + Raio * 0.3),  # base direita
        (CentroX , CentroY + Raio * 0.9),  # ponta (embaixo)
    ]

    FaixaAltura = Raio - 6
    RectBandana = pygame.Rect(0, 0, Raio * 2, FaixaAltura)
    RectBandana.center = (CentroX, CentroY - 2)
    pygame.draw.rect(Tela, CorBandana, RectBandana)

    # Orelhas
    pygame.draw.polygon(Tela, CorGuaxinin, OrelhaEsq)
    pygame.draw.polygon(Tela, CorGuaxinin, OrelhaDir)

    # Corpo
    pygame.draw.circle(Tela, CorGuaxinin, (CentroX, CentroY), Raio)

    # Bandana
    pygame.draw.rect(Tela, CorBandana, RectBandana)


    # Focinho
    pygame.draw.polygon(Tela, CorFucinho, Fucinho)

    # Olhos
    pygame.draw.circle(Tela, (0, 0, 0), (int(CentroX), int(CentroY + Raio * 0.9)), int(Raio * 0.15))

    pygame.draw.circle(Tela, CorText, (int(CentroX+8), int(CentroY-2)), int(Raio * 0.25))

    pygame.draw.circle(Tela, CorText, (int(CentroX - 8), int(CentroY - 2)), int(Raio * 0.25))

    pygame.draw.circle(Tela, (0,0,0), (int(CentroX + 8), int(CentroY - 2)), int(Raio * 0.15))

    pygame.draw.circle(Tela, (0,0,0), (int(CentroX - 8), int(CentroY - 2)), int(Raio * 0.15))

def desenhar_elementos():
    for x in range(Grade):
        for y in range(Grade):
            CentroX = EixoX + x * TamSquare + TamSquare //  2
            CentroY = EixoY + y * TamSquare + TamSquare // 2

            valor = Campo[x][y]

            #G1
            if valor == -1:
                desenha_guaxinim(CorG1, CorFucinhoG1, CorBandanaG1, CentroX, CentroY, TamSquare // 3)


                #G2
            elif valor == -2:
                desenha_guaxinim(CorG2, CorFucinhoG2, CorBandanaG2, CentroX, CentroY, TamSquare // 3)


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
        if Turno == 1 and InvalidezG1 == 1:
            TextoInvalidez = FonteGrande.render("G1 sem movimento válido!!", True, CorBandanaG1)
            Tela.blit(TextoInvalidez, TextoInvalidez.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))

        elif Turno == 2 and InvalidezG2 == 1:
            TextoInvalidez = FonteGrande.render("G2 sem movimento válido!!", True, CorBandanaG2)
            Tela.blit(TextoInvalidez, TextoInvalidez.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))

        else:
            CorTurno = CorBandanaG1 if Turno == 1 else CorBandanaG2
            TextoTurno = FontePequena.render(f"Turno: Jogador {Turno}", True, CorTurno)
            Tela.blit(TextoTurno, TextoTurno.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))

    else:
        if Termino == 1:
            CorTermino = CorBandanaG1
            TextoVitoria = FonteGrande.render("Guaxinim 1 venceu!!", True, CorTermino)
            Tela.blit(TextoVitoria, TextoVitoria.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))


        else:
            CorTermino = CorBandanaG2
            TextoVitoria = FonteGrande.render("Guaxinim 2 venceu!!", True, CorTermino)
            Tela.blit(TextoVitoria, TextoVitoria.get_rect(center=(LarguraPixel // 2, AlturaPixel - 40)))


    # Instruções laterais

    Instr1 = [

        "G1 (Vermelho)",

        "Movimento:","AWSD",

        "Objetivo:", "Chegar na Dir."

    ]

    Instr2 = [

        "G2 (Azul)",

        "Movimento:","SETAS",

        "Objetivo:", "Chegar na Esq."

    ]

    # Instruções Laterais
    # Percorre as listas de texto usando enumerate() para obter a frase e o índice da linha (indice = 0, 1, 2...).
    # A fórmula '100 + idx * 25' calcula a posição vertical (Y) de cada frase, pulando 25 pixels por linha
    # para que os textos fiquem organizados verticalmente e não sejam desenhados uns sobre os outros.
    # G1 é desenhado na margem esquerda (X = 20) e G2 na margem direita (X = LARGURA_TELA - 150).

    for indice, linha in enumerate(Instr1):

        Txt = FontePequena.render(linha, True, CorText)

        Tela.blit(Txt, (20, 100 + indice * 25))

    for indice, linha in enumerate(Instr2):

        Txt = FontePequena.render(linha, True, CorText)

        Tela.blit(Txt, (LarguraPixel - 150, 100 + indice * 25))

def esta_bloqueado(Posicao, GuaxininNum):
    global InvalidezG1, InvalidezG2

    Direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in Direcoes:
        NovoX = Posicao[0] + dx
        NovoY = Posicao[1] + dy

        # Se pelo menos uma direção é válida, não está bloqueado
        if 0 <= NovoX <= 7 and 0 <= NovoY <= 7 and Campo[NovoX][NovoY] == 0:
            if(GuaxininNum) == -1:
                InvalidezG1 = 0
            else:
                InvalidezG2 = 0

            return False

    if (GuaxininNum) == -1:
        InvalidezG1 = 1
    else:
        InvalidezG2 = 1

    return True



def jogada(dx,dy):
    global PosG1, PosG2, Turno

    GuaxininNum = -1 if Turno == 1 else -2

    PosAtual = PosG1 if Turno == 1 else PosG2

    if esta_bloqueado(PosAtual, GuaxininNum):
        return -3

    PosNovaX = PosAtual[0] + dx
    PosNovaY = PosAtual[1] + dy

    if PosNovaX > 7 or PosNovaX < 0 or PosNovaY > 7 or PosNovaY < 0 or Campo[PosNovaX][PosNovaY] != 0:
        print("Movimento inválido!")
        return False

    else:
        Campo[PosAtual[0]][PosAtual[1]] = 20  # Deixa lixo
        # Atualiza
        Campo[PosNovaX][PosNovaY] = GuaxininNum

        if(GuaxininNum == -1):
            PosG1 = [PosNovaX, PosNovaY]
        else:
            PosG2 = [PosNovaX, PosNovaY]

        return True

def renovar_lixo():

    for x in range(Grade):
        for y in range(Grade):
            if Campo[x][y] > 0:
                Campo[x][y] -= 1
    return


def checar_vitoria():
    global Termino

    if PosG1[0] == 7:
        Termino = 1
    elif PosG2[0] == 0:
        Termino = 2
    else:
        return

def main():
    global Turno, Termino, InvalidezG1, InvalidezG2


while Termino == 0:
    MovimentoFeito = False
    dx, dy = 0, 0

    # verifica se algum evento/condicao faz o jogo terminar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN and Termino == 0:
            dx, dy = 0, 0

            # AWSD Tipo de jogada de G1


            if Turno == 1 and jogada(dx, dy) != -3:
                InvalidezG1 = 0
                if event.key == pygame.K_w:
                    dy = -1
                elif event.key == pygame.K_s:
                    dy = 1
                elif event.key == pygame.K_a:
                    dx = -1
                elif event.key == pygame.K_d:
                    dx = 1

            # JKIL tipo de jogada de G2
            elif Turno == 2 and jogada(dx, dy) != -3:
                InvalidezG2 = 0
                if event.key == pygame.K_UP:
                    dy = -1
                elif event.key == pygame.K_DOWN:
                    dy = 1
                elif event.key == pygame.K_LEFT:
                    dx = -1
                elif event.key == pygame.K_RIGHT:
                    dx = 1

            # atualizar variavel MovimentoFeito
            if dx != 0 or dy != 0:
                if jogada(dx, dy) != False:
                    MovimentoFeito = True

            elif Turno == 2 and InvalidezG2 == 1:
                MovimentoFeito = True

            elif Turno == 1 and InvalidezG1 == 1:
                MovimentoFeito = True


    if MovimentoFeito:
        renovar_lixo()
        checar_vitoria()
        if Termino == 0 and Turno == 1:
            Turno = 2
        else:
            Turno = 1


    Tela.fill(CorFundo)
    desenhar_grade()
    desenhar_elementos()
    desenhar_interface()
    # Atualiza a tela gráfica
    pygame.display.flip()


    Relogio.tick(60)




pygame.time.wait(10000)
if __name__ == "__main__":
    main()


