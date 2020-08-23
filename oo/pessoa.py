class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return 'Olá'
if __name__ == '__main__':
    p = Pessoa('Amanda')
    print(p.cumprimentar())
    p.nome = 'Kristoffer'
    print(p.nome)
    print(p.idade)