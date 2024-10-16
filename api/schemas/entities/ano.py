class Ano():

    def __init__(self, ano, atual):
        self.__ano = ano
        self.__atual = atual

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def atual(self):
        return self.__atual

    @atual.setter
    def cpf(self, atual):
        self.__atual = atual
