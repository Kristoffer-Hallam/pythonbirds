"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por
outras duas classes:

1) Motor;
2) Direção;

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade;
2) Método acelerar que deverá incrementar a velocidade de 1 unidade;
3) Método frear que deverá decrementar a velocidade em 2 unidades;

A Direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
                      N
                    O   L
                      S
2) Método girar_a_direita
3) Método girar_a_esquerda

    Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'N'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'L'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'S'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'O'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'N'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'O'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'S'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'L'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'N'
    >>> carro = Carro(motor, direcao)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'N'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'L'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'N'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'O'
"""

NORTE = 'N'
SUL = 'S'
LESTE = 'L'
OESTE = 'O'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

if __name__ == '__main__':
    carro = Carro