# 🚀 Gamezinho — Jogo de Nave Espacial

Um jogo simples de nave espacial desenvolvido em **Python**, utilizando as bibliotecas **Turtle**, **Pygame** e **Pillow**.

O objetivo é controlar a nave, destruir os inimigos com lasers e acumular pontos enquanto tenta não ser atingido pelas pedras espaciais.

## 🎮 Sobre o jogo

O jogador controla uma nave espacial que pode se movimentar pela tela e disparar lasers contra um inimigo que desce pelo espaço.

A cada inimigo destruído:

* ⭐ O jogador ganha pontos.
* 🚀 O inimigo volta para o topo em uma nova posição aleatória.
* 📈 Conforme o jogador avança, a velocidade do inimigo aumenta.
* 🏆 Novas fases são alcançadas conforme a pontuação aumenta.

O jogador começa com **3 vidas**. Quando o inimigo encosta na nave, uma vida é perdida.

Quando todas as vidas acabam, o jogo termina e aparece a tela de **GAME OVER** com a pontuação final.

---

## 🕹️ Controles

| Tecla    | Ação                  |
| -------- | --------------------- |
| `W`      | Mover para cima       |
| `A`      | Mover para a esquerda |
| `S`      | Mover para baixo      |
| `D`      | Mover para a direita  |
| `↑`      | Mover para cima       |
| `←`      | Mover para a esquerda |
| `↓`      | Mover para baixo      |
| `→`      | Mover para a direita  |
| `ESPAÇO` | Disparar laser        |

---

## ❤️ Sistema de vidas

O jogo possui um sistema de **3 vidas**.

```python
vida = 3
```

Quando o inimigo encosta na nave, o jogador perde uma vida:

```python
if dInimigo < 20:
    vida -= 1
```

A quantidade de vidas é atualizada na tela.

Quando:

```python
vida <= 0
```

o jogo termina e a tela de **GAME OVER** é exibida.

---

## ⭐ Sistema de pontuação

Cada inimigo destruído aumenta a pontuação em 1 ponto:

```python
pontos += 1
pontosf += 1
```

A pontuação atual é exibida no canto superior esquerdo da tela.

Ao final da partida, a pontuação final também é apresentada.

---

## 📈 Sistema de fases

O jogo possui um sistema de progressão de fases.

A velocidade do inimigo aumenta conforme o jogador avança:

```python
inimigo_vel += 0.25
```

A partir da fase 5, o inimigo passa a ficar ainda mais rápido conforme os pontos aumentam.

Isso deixa o jogo progressivamente mais difícil.

---

## 🔫 Sistema de laser

O laser possui dois estados:

```python
laser_estado = "pronto"
```

e:

```python
laser_estado = "disparado"
```

O jogador só pode disparar quando o laser está pronto.

Quando o laser ultrapassa o topo da tela, ele volta a ficar disponível para um novo disparo.

Quando o laser atinge o inimigo, o inimigo é reposicionado e o jogador recebe um ponto.

---

## 💥 Colisão

As colisões são verificadas utilizando a distância entre os objetos.

Para verificar se o laser atingiu o inimigo:

```python
distancia = math.sqrt(
    (laser.xcor() - inimigo.xcor()) ** 2 +
    (laser.ycor() - inimigo.ycor()) ** 2
)
```

Se a distância for menor que `20`, o jogo considera que houve uma colisão.

O mesmo princípio é utilizado para verificar quando o inimigo encosta na nave.

---

## 🌌 Efeito Parallax

O fundo possui várias estrelas se movimentando para baixo.

Cada estrela recebe uma velocidade baseada em seu tamanho:

```python
estrela.velocidade = tam * 7
```

Isso cria uma sensação de **profundidade e movimento**, semelhante ao efeito Parallax.

---

## 🔊 Sistema de áudio

O jogo utiliza o **Pygame Mixer** para reproduzir efeitos sonoros.

Existem efeitos para:

* 🔫 Disparo do laser
* 💀 Game Over
* 🎵 Música do jogo

Caso algum arquivo de áudio não seja encontrado, o jogo continua funcionando sem aquele som.

---

## 📁 Estrutura do projeto

A estrutura esperada do projeto é:

```text
Game/
│
├── Gamezinho.py
│
├── gif/
│   ├── espaco.gif
│   ├── nave.gif
│   ├── pedra.gif
│   └── laser.gif
│
├── sons/
│   ├── laser.mp3
│   └── gameover.mp3
│
└── README.md
```

> Os nomes e caminhos dos arquivos precisam corresponder aos utilizados no código.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Turtle** — criação da janela, objetos e movimentação.
* **Math** — cálculos de distância e colisão.
* **Random** — geração de posições aleatórias.
* **Pillow (PIL)** — suporte e configuração para imagens.
* **Pygame** — reprodução dos efeitos sonoros.

---

## 📦 Instalação

### 1. Instale o Python

Baixe e instale uma versão recente do Python.

### 2. Instale as bibliotecas necessárias

No terminal, execute:

```bash
pip install pillow pygame
```

A biblioteca `turtle` já faz parte da instalação padrão do Python.

### 3. Organize os arquivos

Certifique-se de que as pastas `gif` e `sons` estejam no mesmo diretório do arquivo principal do jogo.

### 4. Execute o jogo

```bash
python main.py
```

---

## 🎯 Objetivo

O objetivo é conseguir a maior pontuação possível sem perder as 3 vidas.

**Destrua os inimigos, avance pelas fases e tente sobreviver o máximo possível!**

---

## 🏆 Funcionalidades

* [x] Movimentação da nave
* [x] Controle por teclado
* [x] Sistema de laser
* [x] Inimigos com posição aleatória
* [x] Sistema de pontuação
* [x] Sistema de vidas
* [x] Sistema de fases
* [x] Aumento da dificuldade
* [x] Colisão entre laser e inimigo
* [x] Colisão entre inimigo e nave
* [x] Tela de Game Over
* [x] Efeitos sonoros
* [x] Fundo espacial
* [x] Efeito Parallax

---

## 👨‍💻 Projeto

Projeto desenvolvido para praticar conceitos de **Python, lógica de programação, funções, estruturas de repetição, colisões, controle de teclado e desenvolvimento de jogos**.
