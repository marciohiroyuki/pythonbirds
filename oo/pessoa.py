class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    hiro = Pessoa(nome='Hiro')
    julia = Pessoa(hiro, nome='Julia')
    print(Pessoa.cumprimentar(julia))
    print(id(julia))
    print(julia.cumprimentar())
    print(julia.idade)
    for filho in julia.filhos:
        print(filho.nome)
    julia.sobrenome='Masuno'
    del julia.filhos
    print(julia.sobrenome)
    print(julia.__dict__)
    print(hiro.__dict__)