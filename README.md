#  Corrida Guaxinim

Crédito da criação do enunciado: Professor Jean Felipe Cheiran

Jogo de tabuleiro para 2 jogadores, feito em Python com **pygame**, que
simula a corrida de dois guaxinins  tentando invadir o
território um do outro para roubar o estoque de comida enquanto deixam
uma trilha de lixo pelo caminho para atrapalhar o adversário.

## Print do jogo

<img width="803" height="595" alt="image" src="https://github.com/user-attachments/assets/3e8f12fe-a46b-4919-bea0-a0e1cfdd6fe0" />




## O terreno

O jogo ocorre em uma **matriz 8x8**, representando um terreno baldio entre
os territórios dos dois guaxinins. Cada guaxinim começa em um lado oposto
do tabuleiro:

- **G1** começa do lado esquerdo do terreno.
- **G2** começa do lado direito do terreno.

## Objetivo

- **G1** vence o jogo se chegar em **qualquer espaço da última coluna**
  (o território do oponente).
- **G2** vence o jogo se chegar em **qualquer espaço da primeira coluna**.

## Como jogar

O **guaxinim G1 sempre joga primeiro**, e os turnos se alternam entre os
dois jogadores a partir daí.

Os guaxinins se movem **uma casa por vez**, apenas na horizontal ou na
vertical (sem diagonais):

| Ação | G1 | G2 |
|---|---|---|
| Mover para cima | `W` | `↑` |
| Mover para baixo | `S` | `↓` |
| Mover para esquerda | `A` | `←` |
| Mover para direita | `D` | `→` |

Um guaxinim **não pode passar por cima do outro guaxinim**, nem por cima
de obstáculos (trilhas de lixo).

## Trilha de lixo

Toda vez que um guaxinim se move, a casa onde ele **estava** vira uma
pilha de lixo — um obstáculo que bloqueia a passagem tanto de quem a
gerou quanto do oponente.

Essas pilhas de lixo não duram para sempre: elas passam a ser consumidas
por ratazanas, que demoram **20 turnos** (ou seja, 20 trocas de vez entre
os jogadores) para liberar completamente aquele espaço para movimento
novamente.

## Guaxinim sem movimento válido

Se um guaxinim ficar completamente cercado por lixo, pelo outro guaxinim
ou pelas bordas do tabuleiro (sem nenhuma casa livre nas 4 direções), ele
**perde a vez de jogar** naquele turno — o jogo mostra uma mensagem na
tela avisando que o guaxinim está sem movimento válido, e passa a vez
automaticamente para o oponente.

<img width="803" height="595" alt="image" src="https://github.com/user-attachments/assets/3dee84d7-4f9a-4fa2-ac20-941f89864628" />

## Fim de jogo

Quando a partida termina com um vencedor, o jogo exibe uma mensagem na
tela informando **qual guaxinim venceu: G1 ou G2**.

## Requisitos

- Python 3
- Biblioteca `pygame`

```bash
pip install pygame
```

## Como executar

```bash
python corrida_guaxinim.py
```

Uma janela de 800x600 abre com o tabuleiro. O jogo roda a 60 quadros por
segundo e termina automaticamente assim que um guaxinim vence.

## Estrutura interna do tabuleiro

Internamente, o tabuleiro é representado por uma matriz `Campo[x][y]`,
onde cada posição pode valer:

- `0` → casa vazia
- `-1` → posição atual do G1
- `-2` → posição atual do G2
- qualquer número `> 0` → quantos turnos faltam para aquela pilha de
  lixo sumir (contagem regressiva)

## Visual dos guaxinins

Cada guaxinim é desenhado combinando formas simples do pygame: corpo
(círculo), duas orelhas (triângulos), focinho (triângulo com uma bolinha
na ponta) e uma bandana colorida (retângulo) que identifica o jogador —
vermelha para G1, azul para G2.

## Documentação relacionada

Para detalhes de sintaxe e funções do pygame usadas na implementação,
veja o diretório Sintaxe Pygames.
