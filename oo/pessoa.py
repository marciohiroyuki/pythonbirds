class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        return f'Aperto de mão'

class Mulher(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Sinal Spock.'

if __name__ == '__main__':
    hiro = Mutante(nome='Hiro')
    julia = Mulher(hiro, nome='Julia')
    print(Pessoa.cumprimentar(julia))
    print(id(julia))
    print(julia.cumprimentar())
    print(julia.idade)
    for filho in julia.filhos:
        print(filho.nome)
    julia.sobrenome='Masuno'
    del julia.filhos
    print(julia.sobrenome)
    hiro.olhos=1
    del hiro.olhos
    print(julia.__dict__)
    print(hiro.__dict__)
    print(Pessoa.olhos)
    print(julia.olhos)
    print(hiro.olhos)
    print(id(Pessoa.olhos), id(julia.olhos), id(hiro.olhos))
    print(Pessoa.metodo_estatico(), julia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), julia.nome_e_atributos_de_classe())
    p = Pessoa(nome='Anonimo')
    print(isinstance(p, Pessoa))
    print(isinstance(p, Homem))
    print(isinstance(hiro, Pessoa))
    print(isinstance(hiro, Homem))
    print(hiro.olhos)
    print(hiro.cumprimentar())
    print(julia.cumprimentar())