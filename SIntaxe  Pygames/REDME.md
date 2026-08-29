# Sintaxe e recursos do pygame usados no Corrida Guaxinim

Este documento explica cada função/conceito do pygame utilizado no jogo,
na ordem em que aparecem no código.

---

## Inicialização e janela

### `pygame.init()`
Inicializa todos os módulos internos do pygame (vídeo, áudio, fontes, etc).
Precisa ser chamado **antes** de qualquer outra função do pygame.

### `pygame.display.set_mode((largura, altura))`
Cria a janela do jogo com o tamanho em pixels informado, e devolve a
`Surface` principal (a "tela") onde tudo será desenhado.

```python
Tela = pygame.display.set_mode((800, 600))
```

### `pygame.display.set_caption("texto")`
Define o título que aparece na barra da janela.

### `pygame.display.flip()`
Atualiza a janela, mostrando na tela tudo o que foi desenhado desde o
último `flip()`. Sem essa chamada, os `draw`/`blit` ficam "invisíveis" —
eles desenham num buffer interno que só aparece de fato na tela depois do
`flip()`.

---

## Controle de tempo

### `pygame.time.Clock()`
Cria um "relógio" que ajuda a controlar a velocidade do jogo.

```python
Relogio = pygame.time.Clock()
```

### `Relogio.tick(60)`
Limita o loop principal a rodar no máximo 60 vezes por segundo (60 FPS).
Ele pausa a execução o tempo necessário para não passar desse limite,
independente de quão rápido o computador consiga processar cada volta do
loop.

### `pygame.time.delay(ms)` / `pygame.time.wait(ms)`
Pausam a execução do jogo inteiro por um número de milissegundos.
Diferença: `wait` libera a CPU pro sistema operacional durante a espera,
`delay` não. Na prática, ambos travam o processamento de eventos — não
usar durante o loop de jogo ativo, só em telas de pausa/fim de jogo.

```python
pygame.time.wait(10000)  # espera 10 segundos
```

---

## Fontes e texto

### `pygame.font.SysFont(nome, tamanho, bold=True)`
Cria uma fonte usando uma fonte **instalada no sistema operacional** (ex:
Arial). Depende do computador onde o jogo roda — pode não existir em toda
máquina.

### `pygame.font.Font(caminho, tamanho)`
Cria uma fonte a partir de um arquivo `.ttf`/`.otf`. Passar `None` no lugar
do caminho faz o pygame usar sua fonte embutida (`freesansbold.ttf`), que
sempre está disponível, não importa o sistema.

```python
FontePequena = pygame.font.Font(None, 20)
```

Fontes criadas com `Font()` não aceitam o parâmetro `bold=True` na
criação; use `.set_bold(True)` depois, se precisar.

### `Fonte.render(texto, antialias, cor)`
Transforma um texto em uma imagem (`Surface`) pronta pra ser desenhada na
tela. `antialias` (`True`/`False`) suaviza as bordas das letras.

```python
texto = FontePequena.render("G1", True, (0, 0, 0))
```

### `Surface.blit(outra_surface, posicao)`
"Cola" uma superfície (imagem, texto renderizado, etc) em cima de outra —
no jogo, sempre colando em cima da `Tela`.

```python
Tela.blit(texto, (100, 50))
```

### `Surface.get_rect(center=(x, y))`
Devolve um `Rect` (retângulo) do tamanho da superfície, já posicionado
para que seu **centro** fique nas coordenadas informadas — muito usado
pra centralizar texto sem calcular a posição manualmente.

```python
Tela.blit(texto, texto.get_rect(center=(400, 300)))
```

---

## Desenho de formas

### `pygame.draw.rect(superficie, cor, retangulo)`
Desenha um retângulo preenchido. `retangulo` pode ser uma tupla
`(x, y, largura, altura)` ou um objeto `pygame.Rect`.

```python
pygame.draw.rect(Tela, CorGrama, (EixoX, EixoY, 480, 480))
```

### `pygame.draw.line(superficie, cor, inicio, fim, espessura)`
Desenha uma linha reta entre dois pontos `(x, y)`.

```python
pygame.draw.line(Tela, CorLinha, (0, 0), (100, 0), 2)
```

### `pygame.draw.circle(superficie, cor, centro, raio)`
Desenha um círculo preenchido. `centro` é uma tupla `(x, y)` — precisa ser
número inteiro, por isso é comum usar `int(...)` ao calcular as
coordenadas.

```python
pygame.draw.circle(Tela, CorG1, (CentroX, CentroY), 20)
```

### `pygame.draw.polygon(superficie, cor, lista_de_pontos)`
Desenha uma forma preenchida a partir de uma lista de pontos `(x, y)`
(usado no jogo pra desenhar as orelhas e o focinho triangulares dos
guaxinins).

```python
Fucinho = [
    (CentroX - 20, CentroY + 10),
    (CentroX + 20, CentroY + 10),
    (CentroX, CentroY + 40),
]
pygame.draw.polygon(Tela, CorFucinho, Fucinho)
```

### `pygame.Rect(x, y, largura, altura)` e `.center`
Objeto que representa um retângulo. Pode ser criado "vazio" e depois
posicionado atribuindo `.center`, `.midbottom`, `.topleft`, etc — o
pygame recalcula `x`/`y` automaticamente a partir da propriedade usada.

```python
RectBandana = pygame.Rect(0, 0, 40, 20)
RectBandana.center = (CentroX, CentroY)  # centraliza o retângulo
```

### `Tela.fill(cor)`
Pinta a tela inteira com uma cor sólida — usado no início de cada frame
pra "limpar" o desenho do frame anterior antes de redesenhar tudo.

```python
Tela.fill(CorFundo)
```

---

## Eventos e teclado

### `pygame.event.get()`
Devolve a lista de todos os eventos ocorridos desde a última chamada
(teclas pressionadas, fechar janela, mouse, etc). Precisa ser consumida a
cada volta do loop, senão os eventos se acumulam.

```python
for event in pygame.event.get():
    ...
```

### `event.type`
Indica o tipo do evento. Os dois usados no jogo:
- `pygame.QUIT` → o jogador clicou no X da janela
- `pygame.KEYDOWN` → uma tecla foi pressionada

⚠️ **Importante**: `event.key` só existe em eventos do tipo `KEYDOWN` (ou
`KEYUP`). Tentar ler `event.key` em outro tipo de evento (como `QUIT` ou
movimento do mouse) causa `AttributeError` — por isso todo código que lê
`event.key` precisa estar dentro de um `if event.type == pygame.KEYDOWN:`.

### `event.key`
Identifica **qual** tecla foi pressionada, comparado com as constantes do
pygame:

| Constante | Tecla |
|---|---|
| `pygame.K_w` | W |
| `pygame.K_a` | A |
| `pygame.K_s` | S |
| `pygame.K_d` | D |
| `pygame.K_UP` | Seta pra cima |
| `pygame.K_DOWN` | Seta pra baixo |
| `pygame.K_LEFT` | Seta pra esquerda |
| `pygame.K_RIGHT` | Seta pra direita |

```python
if event.key == pygame.K_w:
    dy = -1
```

### `pygame.quit()` / `sys.exit()`
`pygame.quit()` desliga os módulos internos do pygame de forma limpa.
`sys.exit()` (do módulo padrão `sys`, não do pygame) encerra o programa
Python. Os dois são usados juntos ao fechar o jogo pelo `QUIT`.

---

## Conceitos gerais de estrutura usados no jogo

### Loop principal (`while`)
Todo jogo em pygame roda dentro de um laço que se repete continuamente
até alguma condição de saída (`Termino != 0`, no caso deste jogo). A cada
volta do loop = um "frame":

1. Processa eventos (teclado, fechar janela)
2. Atualiza o estado do jogo (posições, turno, lixo)
3. Redesenha a tela inteira
4. `pygame.display.flip()`
5. `Relogio.tick(60)` pra manter o ritmo de 60 FPS

### Variáveis globais e `global`
Como o loop e as funções de desenho/jogada precisam ler e alterar as
mesmas variáveis de estado (`Turno`, `Termino`, `PosG1`, `PosG2`,
`InvalidezG1`, `InvalidezG2`), essas variáveis são declaradas fora de
qualquer função, e cada função que **altera** (não só lê) uma delas
precisa declarar `global nome_da_variavel` no início.

```python
def jogada(dx, dy):
    global PosG1, PosG2, Turno
    ...
```
