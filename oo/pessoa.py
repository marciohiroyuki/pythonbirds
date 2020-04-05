class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    hiro.olhos=1
    del hiro.olhos
    Pessoa.olhos=3
    print(julia.__dict__)
    print(hiro.__dict__)
    print(Pessoa.olhos)
    print(julia.olhos)
    print(hiro.olhos)
    print(id(Pessoa.olhos), id(julia.olhos), id(hiro.olhos))
    print(Pessoa.metodo_estatico(), julia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), julia.nome_e_atributos_de_classe())